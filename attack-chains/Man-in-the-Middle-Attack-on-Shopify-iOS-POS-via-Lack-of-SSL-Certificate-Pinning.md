---
id: ac-uuid-001
tags:
  - mitm
  - ssl-pinning
  - certificate-spoofing
  - ios
  - shopify
  - pos
type: attack_chain
tools:
  - '[[tools/Burp-Proxy]]'
  - '[[tools/mitmproxy]]'
tactics:
  - '[[Defense Evasion]]'
verified: false
platforms:
  - iOS
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Install-Malicious-Certificate-on-iOS-Device]]'
  - '[[procedures/Proxy-iOS-App-Traffic-Through-Interception-Tool]]'
  - '[[procedures/Verify-MitM-Success-by-Intercepting-App-Traffic]]'
step_count: 3
techniques:
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:24:39.467Z'
description: >-
  Demonstrates how an attacker can perform a MitM attack on the Shopify iOS POS
  app by exploiting the absence of SSL certificate pinning, allowing
  interception of sensitive data like cardholder information.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Man-in-the-Middle Attack on Shopify iOS POS via Lack of SSL Certificate Pinning

The Shopify iOS POS application does not implement SSL certificate pinning, relying only on the iOS keychain for validation without confirming the certificate's association with Shopify. This allows attackers to perform Man-in-the-Middle (MitM) attacks by installing a trusted malicious certificate on the device, enabling interception of all app traffic, including sensitive cardholder data (CHD). The attack requires physical or social engineering access to the device to install the certificate and configure proxying.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Install Malicious Certificate] --> B[Proxy App Traffic]
    B --> C[Intercept and Verify Traffic]
    C --> D[Exfiltrate Sensitive Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Proxy]]
- [[tools/mitmproxy]]

### Target Environment

- iOS device running Shopify POS app
- Physical access to the device or ability to trick user into installing a profile
- No specific ports or services beyond standard HTTPS (port 443)

### Initial Access Requirements

- User interaction to install and trust the malicious certificate
- Attacker's machine on the same network for proxying
- No prior credentials needed, but device unlock may be required

## Detailed Attack Procedures

### Step 1: Install Malicious Certificate
procedure: [[procedures/Install-Malicious-Certificate-on-iOS-Device]]

**Objective**: Gain the ability to impersonate Shopify's servers by installing and trusting a fake SSL certificate on the target iOS device.

**Instructions**: Create or obtain a malicious certificate (e.g., via a self-signed CA) and deliver it to the device as a configuration profile. Use social engineering to prompt the user to install it, then navigate to Settings > General > VPN & Device Management to trust the profile.

**Expected Output**: The certificate appears in the trusted certificates list, allowing the device to accept connections validated by the attacker's CA.

**Success Indicators**:
- Certificate installed and trusted in iOS settings
- No errors when browsing HTTPS sites with the fake cert

### Step 2: Proxy iOS App Traffic
procedure: [[procedures/Proxy-iOS-App-Traffic-Through-Interception-Tool]]

**Objective**: Route all Shopify POS app traffic through the attacker's proxy to enable interception using the trusted malicious certificate.

**Instructions**: On the iOS device, go to Settings > Wi-Fi, tap the network, and set the HTTP Proxy to Manual, entering the attacker's IP and port (e.g., 8080 for Burp). Launch the Shopify POS app and perform actions like processing a payment to generate traffic.

**Expected Output**: App traffic begins flowing through the proxy without connection errors.

**Success Indicators**:
- Proxy logs show incoming connections from the iOS device
- No SSL handshake failures in the app

### Step 3: Verify MitM and Intercept Traffic
procedure: [[procedures/Verify-MitM-Success-by-Intercepting-App-Traffic]]

**Objective**: Confirm the app trusts the malicious certificate, allowing decryption and inspection of sensitive communications, including CHD.

**Instructions**: In the proxy tool, observe decrypted HTTPS requests from the app. Interact with the app (e.g., scan a card) and check for unencrypted payloads containing sensitive data.

**Expected Output**: Cleartext traffic visible in proxy, showing API calls to Shopify endpoints with CHD.

**Success Indicators**:
- Successful decryption of app traffic
- Visibility of sensitive data like card numbers in transit

## Attack Chain Summary

### Key Achievements

1. Bypassed SSL validation by exploiting lack of pinning
2. Intercepted and decrypted POS app communications
3. Enabled potential exfiltration of cardholder data via MitM

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Adversary-in-the-Middle]]

### MITRE ATT&CK Tactics

- [[Defense Evasion]]

---
*Last updated: 2023-10-01T00:00:00Z*
