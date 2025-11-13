#!/usr/bin/env python3
"""
Analyze NoFraud export data to identify fraud patterns
"""

import csv
import re
from collections import Counter, defaultdict
from datetime import datetime
from ipaddress import ip_address, IPv6Address
import json

# Known freight forwarder addresses and patterns
FREIGHT_FORWARDERS = {
    '13542 Briarmoor Ct': 'Orlando freight forwarder',
    '6 SHEA WAY': 'Newark DE freight forwarder',
    '2721 Forsyth Rd': 'Winter Park FL freight forwarder',
}

# Common disposable email domains
DISPOSABLE_EMAIL_DOMAINS = [
    'mail.ru', 'guerrillamail.com', 'tempmail.com', '10minutemail.com',
    'throwaway.email', 'mohmal.com', 'trashmail.com', 'mailinator.com',
    'yopmail.com', 'getnada.com', 'temp-mail.org', 'fakemailgenerator.com'
]

def is_disposable_email(email):
    """Check if email domain is likely disposable"""
    if not email:
        return False
    domain = email.split('@')[-1].lower()
    return any(d in domain for d in DISPOSABLE_EMAIL_DOMAINS)

def is_freight_forwarder(address):
    """Check if address matches known freight forwarder pattern"""
    if not address:
        return False
    for key, desc in FREIGHT_FORWARDERS.items():
        if key.lower() in address.lower():
            return True
    # Check for suite numbers in residential areas (common freight forwarder pattern)
    if re.search(r'suite\s+\d+', address.lower()) and any(city in address.lower() for city in ['orlando', 'newark', 'winter park']):
        return True
    return False

def is_foreign_ip(ip_str):
    """Check if IP is likely foreign (outside US)"""
    if not ip_str or ip_str == 'N/A':
        return None
    # This is simplified - would need geoip library for accuracy
    # But IPv6 addresses and some patterns suggest foreign
    if ':' in ip_str:  # IPv6
        return True
    try:
        ip = ip_address(ip_str)
        # Could add geoip lookup here
        return False
    except:
        return None

def analyze_transactions(filename):
    transactions = []
    
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            transactions.append(row)
    
    print(f"Total transactions analyzed: {len(transactions)}\n")
    print("=" * 80)
    print("FRAUD PATTERN ANALYSIS")
    print("=" * 80)
    
    # 1. Temporal analysis
    print("\n1. TEMPORAL PATTERNS")
    print("-" * 80)
    dates = []
    for t in transactions:
        try:
            # Parse date: NOV  6 08:13pm 2023
            date_str = t['created date']
            dt = datetime.strptime(date_str, '%b %d %I:%M%p %Y')
            dates.append(dt)
        except:
            pass
    
    if dates:
        dates.sort()
        print(f"Date range: {dates[0].strftime('%Y-%m-%d')} to {dates[-1].strftime('%Y-%m-%d')}")
        print(f"Days covered: {(dates[-1] - dates[0]).days + 1}")
        print(f"Transactions per day: {len(transactions) / ((dates[-1] - dates[0]).days + 1):.1f}")
    
    # 2. IP address patterns
    print("\n2. IP ADDRESS PATTERNS")
    print("-" * 80)
    ip_counts = Counter()
    ipv6_count = 0
    foreign_ip_indicators = 0
    
    for t in transactions:
        ip = t.get('customer ip', '').strip()
        if ip and ip != 'N/A':
            ip_counts[ip] += 1
            if ':' in ip:
                ipv6_count += 1
            if is_foreign_ip(ip):
                foreign_ip_indicators += 1
    
    print(f"Unique IPs: {len(ip_counts)}")
    print(f"IPv6 addresses: {ipv6_count} ({ipv6_count/len(transactions)*100:.1f}%)")
    print(f"\nMost common IPs:")
    for ip, count in ip_counts.most_common(10):
        print(f"  {ip}: {count} transactions ({count/len(transactions)*100:.1f}%)")
    
    # 3. Email patterns
    print("\n3. EMAIL PATTERNS")
    print("-" * 80)
    email_counts = Counter()
    email_domains = Counter()
    disposable_count = 0
    
    for t in transactions:
        email = t.get('email', '').strip().lower()
        if email and email != 'n/a':
            email_counts[email] += 1
            domain = email.split('@')[-1]
            email_domains[domain] += 1
            if is_disposable_email(email):
                disposable_count += 1
    
    print(f"Unique emails: {len(email_counts)}")
    print(f"Disposable emails: {disposable_count} ({disposable_count/len(transactions)*100:.1f}%)")
    print(f"\nMost common email domains:")
    for domain, count in email_domains.most_common(15):
        print(f"  {domain}: {count} transactions ({count/len(transactions)*100:.1f}%)")
    
    print(f"\nEmails used multiple times:")
    multi_email = {e: c for e, c in email_counts.items() if c > 1}
    for email, count in sorted(multi_email.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {email}: {count} transactions")
    
    # 4. Shipping address patterns
    print("\n4. SHIPPING ADDRESS PATTERNS")
    print("-" * 80)
    shipping_addresses = Counter()
    freight_forwarder_count = 0
    address_mismatch_count = 0
    
    for t in transactions:
        ship_addr = t.get('shipping address', '').strip()
        bill_addr = t.get('billing address', '').strip()
        
        if ship_addr and ship_addr != 'N/A':
            shipping_addresses[ship_addr] += 1
            if is_freight_forwarder(ship_addr):
                freight_forwarder_count += 1
        
        if ship_addr != bill_addr and ship_addr != 'N/A' and bill_addr != 'N/A':
            address_mismatch_count += 1
    
    print(f"Unique shipping addresses: {len(shipping_addresses)}")
    print(f"Freight forwarder addresses: {freight_forwarder_count} ({freight_forwarder_count/len(transactions)*100:.1f}%)")
    print(f"Billing/shipping address mismatches: {address_mismatch_count} ({address_mismatch_count/len(transactions)*100:.1f}%)")
    
    print(f"\nMost common shipping addresses:")
    for addr, count in shipping_addresses.most_common(10):
        print(f"  {addr[:70]}... ({count} transactions)")
        if is_freight_forwarder(addr):
            print(f"    ⚠️  FREIGHT FORWARDER")
    
    # 5. Card patterns
    print("\n5. PAYMENT CARD PATTERNS")
    print("-" * 80)
    card_last4 = Counter()
    avs_results = Counter()
    cvv_results = Counter()
    
    for t in transactions:
        last4 = t.get('card last4', '').strip()
        if last4 and last4 != 'N/A' and last4 != '0000':
            card_last4[last4] += 1
        
        avs = t.get('avs', '').strip()
        if avs and avs != 'N/A':
            avs_results[avs] += 1
        
        cvv = t.get('cvv', '').strip()
        if cvv and cvv != 'N/A':
            cvv_results[cvv] += 1
    
    print(f"Unique card last4: {len(card_last4)}")
    print(f"\nAVS results:")
    for result, count in avs_results.most_common():
        meaning = {
            'Y': 'Address and ZIP match',
            'N': 'Neither address nor ZIP match',
            'Z': 'ZIP matches, address does not',
            'U': 'Unavailable/unverified',
            'A': 'Address matches, ZIP does not'
        }
        print(f"  {result}: {count} ({count/len(transactions)*100:.1f}%) - {meaning.get(result, 'Unknown')}")
    
    print(f"\nCVV results:")
    for result, count in cvv_results.most_common():
        meaning = {
            'M': 'Match',
            'N': 'No match',
            'U': 'Unavailable/unverified'
        }
        print(f"  {result}: {count} ({count/len(transactions)*100:.1f}%) - {meaning.get(result, 'Unknown')}")
    
    cards_used_multiple = {c: cnt for c, cnt in card_last4.items() if cnt > 1}
    if cards_used_multiple:
        print(f"\nCards used multiple times: {len(cards_used_multiple)}")
        for card, count in sorted(cards_used_multiple.items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"  ****{card}: {count} transactions")
    
    # 6. Name patterns
    print("\n6. NAME PATTERNS")
    print("-" * 80)
    billing_names = Counter()
    shipping_names = Counter()
    name_mismatch_count = 0
    
    for t in transactions:
        bill_name = t.get('billing name', '').strip().lower()
        ship_name = t.get('shipping name', '').strip().lower()
        
        if bill_name and bill_name != 'n/a':
            billing_names[bill_name] += 1
        
        if ship_name and ship_name != 'n/a':
            shipping_names[ship_name] += 1
        
        if bill_name != ship_name and bill_name != 'n/a' and ship_name != 'n/a':
            name_mismatch_count += 1
    
    print(f"Unique billing names: {len(billing_names)}")
    print(f"Unique shipping names: {len(shipping_names)}")
    print(f"Billing/shipping name mismatches: {name_mismatch_count} ({name_mismatch_count/len(transactions)*100:.1f}%)")
    
    # 7. Amount analysis
    print("\n7. TRANSACTION AMOUNT ANALYSIS")
    print("-" * 80)
    amounts = []
    for t in transactions:
        try:
            amt = float(t.get('amount', 0))
            amounts.append(amt)
        except:
            pass
    
    if amounts:
        amounts.sort()
        print(f"Total amount: ${sum(amounts):,.2f}")
        print(f"Average: ${sum(amounts)/len(amounts):,.2f}")
        print(f"Median: ${amounts[len(amounts)//2]:,.2f}")
        print(f"Min: ${min(amounts):,.2f}")
        print(f"Max: ${max(amounts):,.2f}")
    
    # 8. Composite fraud indicators
    print("\n8. COMPOSITE FRAUD RISK INDICATORS")
    print("-" * 80)
    
    high_risk_count = 0
    medium_risk_count = 0
    
    risk_factors = defaultdict(int)
    
    for t in transactions:
        risk_score = 0
        risk_reasons = []
        
        # Check various risk factors
        email = t.get('email', '').lower()
        if is_disposable_email(email):
            risk_score += 2
            risk_reasons.append('disposable_email')
        
        ship_addr = t.get('shipping address', '').lower()
        if is_freight_forwarder(ship_addr):
            risk_score += 3
            risk_reasons.append('freight_forwarder')
        
        bill_addr = t.get('billing address', '').lower()
        ship_addr_lower = t.get('shipping address', '').lower()
        if bill_addr != ship_addr_lower and bill_addr and ship_addr_lower:
            risk_score += 1
            risk_reasons.append('address_mismatch')
        
        avs = t.get('avs', '').strip()
        if avs in ['N', 'Z', 'U']:
            risk_score += 1
            if avs == 'N':
                risk_reasons.append('avs_fail')
        
        cvv = t.get('cvv', '').strip()
        if cvv == 'N':
            risk_score += 2
            risk_reasons.append('cvv_fail')
        
        ip = t.get('customer ip', '')
        if ip and ':' in ip:  # IPv6 might indicate proxy/VPN
            risk_score += 1
            risk_reasons.append('ipv6')
        
        if risk_score >= 5:
            high_risk_count += 1
        elif risk_score >= 3:
            medium_risk_count += 1
        
        for reason in risk_reasons:
            risk_factors[reason] += 1
    
    print(f"High risk transactions (score >= 5): {high_risk_count} ({high_risk_count/len(transactions)*100:.1f}%)")
    print(f"Medium risk transactions (score 3-4): {medium_risk_count} ({medium_risk_count/len(transactions)*100:.1f}%)")
    
    print(f"\nRisk factor frequency:")
    for factor, count in sorted(risk_factors.items(), key=lambda x: x[1], reverse=True):
        print(f"  {factor}: {count} ({count/len(transactions)*100:.1f}%)")
    
    # 9. Suspicious patterns
    print("\n9. MOST SUSPICIOUS PATTERNS")
    print("-" * 80)
    
    # Find transactions with multiple risk factors
    suspicious = []
    for t in transactions:
        score = 0
        flags = []
        
        email = t.get('email', '').lower()
        if is_disposable_email(email):
            score += 2
            flags.append('Disposable email')
        
        if is_freight_forwarder(t.get('shipping address', '').lower()):
            score += 3
            flags.append('Freight forwarder')
        
        if t.get('cvv') == 'N':
            score += 2
            flags.append('CVV fail')
        
        if t.get('avs') == 'N':
            score += 2
            flags.append('AVS fail')
        
        if email_counts.get(email, 1) > 1:
            score += 1
            flags.append(f'Reused email ({email_counts[email]}x)')
        
        if score >= 4:
            suspicious.append((score, t, flags))
    
    suspicious.sort(reverse=True, key=lambda x: x[0])
    
    print("Top 10 most suspicious transactions:")
    for i, (score, t, flags) in enumerate(suspicious[:10], 1):
        print(f"\n{i}. Score: {score} | Order: {t.get('invoice number')} | ${t.get('amount')}")
        print(f"   Email: {t.get('email')}")
        print(f"   Flags: {', '.join(flags)}")
    
    # 10. Summary and conclusions
    print("\n" + "=" * 80)
    print("SUMMARY & CONCLUSIONS")
    print("=" * 80)
    
    total_fraud_indicators = (
        freight_forwarder_count + 
        (address_mismatch_count * 0.8) +  # Not all mismatches are fraud
        sum(1 for t in transactions if t.get('cvv') == 'N') +
        sum(1 for t in transactions if t.get('avs') == 'N')
    )
    
    print(f"\nKey findings:")
    print(f"• {len(ip_counts)} unique IPs for {len(transactions)} transactions (ratio: {len(transactions)/max(len(ip_counts),1):.2f}x)")
    print(f"• {len(email_counts)} unique emails (ratio: {len(transactions)/max(len(email_counts),1):.2f}x)")
    print(f"• {freight_forwarder_count} transactions ({freight_forwarder_count/len(transactions)*100:.1f}%) to freight forwarders")
    print(f"• High/medium risk: {high_risk_count + medium_risk_count} transactions ({(high_risk_count + medium_risk_count)/len(transactions)*100:.1f}%)")
    
    # Check for organized fraud rings
    print(f"\nOrganized fraud indicators:")
    if len(transactions) / max(len(ip_counts), 1) > 10:
        print("  ⚠️  HIGH: Many transactions per IP suggests botting/automation")
    
    if freight_forwarder_count > len(transactions) * 0.1:
        print(f"  ⚠️  HIGH: {freight_forwarder_count/len(transactions)*100:.1f}% to freight forwarders suggests organized reshipping fraud")
    
    if sum(1 for t in transactions if t.get('cvv') == 'N') > len(transactions) * 0.2:
        cvv_fail_pct = sum(1 for t in transactions if t.get('cvv') == 'N') / len(transactions) * 100
        print(f"  ⚠️  HIGH: {cvv_fail_pct:.1f}% CVV failures suggests card testing/stolen cards")
    
    return transactions

if __name__ == '__main__':
    analyze_transactions('nofraud-export-ID_258431c36f.csv')

