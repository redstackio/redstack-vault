---
id: ac-twitter-ios-mitm-001
tags:
  - mitm
  - ssl-tls
  - certificate-validation
  - oauth-leak
  - twitter
  - ios
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/iptables]]'
tactics:
  - '[[Defense Evasion]]'
verified: false
platforms:
  - iOS
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Set-Up-Transparent-Proxy-with-Burp-Suite]]'
  - '[[procedures/Configure-Rogue-WiFi-Access-Point]]'
  - '[[procedures/Redirect-HTTPS-Traffic-Using-iptables]]'
  - '[[procedures/Connect-iOS-Device-to-Rogue-WiFi]]'
  - '[[procedures/Launch-Twitter-App-on-iOS-Device]]'
  - '[[procedures/Observe-Intercepted-Traffic-in-Proxy]]'
step_count: 6
techniques:
  - '[[Adversary-in-the-Middle]]'
  - '[[LLMNR-NBT-NS Poisoning and SMB Relay]]'
updated_at: '2025-12-14T17:24:44.866Z'
description: >-
  A multi-stage attack exploiting improper SSL/TLS certificate validation in the
  Twitter iOS app to perform a MITM attack, intercepting sensitive OAuth tokens
  and authentication details without installing custom CA certificates.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
  - '[[LLMNR-NBT-NS Poisoning and SMB Relay]]'
---
# Man-in-the-Middle Attack on Twitter iOS App via Rogue WiFi and Transparent Proxy

The Twitter iOS app (versions 6.62 or 6.62.1) fails to properly validate SSL/TLS server certificates when connecting to api.twitter.com, enabling a man-in-the-middle (MITM) attack through a transparent proxy without requiring custom CA certificates on the device. This attack involves setting up a rogue WiFi access point on a Linux machine, redirecting HTTPS traffic to a proxy like Burp Suite, and capturing sensitive data such as OAuth tokens, client UUIDs, device IDs, and authentication details. The vulnerability stems from the app's non-validation of certificates, possibly due to race conditions in Apple's networking stack (URLSession or ATS), and failure to honor HSTS headers, allowing downgrades to HTTP. Impacts include account compromise, arbitrary redirects to non-TLS endpoints, and injection of malicious responses like modified settings.json, potentially leading to XSS or further exploits.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Set Up Proxy] --> B[Start Rogue WiFi]
    B --> C[Redirect Traffic]
    C --> D[Connect Device]
    D --> E[Launch App]
    E --> F[Intercept Data]

    style A fill:#e74c3c
    style B fill:#e74c3c
    style C fill:#f39c12
    style D fill:#f39c12
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- [[tools/iptables]]

### Target Environment

- iOS device (stock iPhone on iOS 9.3.3 or 9.3.5, no jailbreak or custom profiles)
- Twitter iOS app (version 6.62 or 6.62.1)
- Linux machine for attacker setup (with wlan0 interface)
- Services/ports: api.twitter.com on port 443 (HTTPS)

### Initial Access Requirements

- Physical proximity to target device for WiFi connection
- No credentials needed; relies on user joining rogue WiFi
- Attacker machine must support WiFi AP and proxy hosting

## Detailed Attack Procedures

### Step 1: Set Up Transparent Proxy
procedure: [[procedures/Set-Up-Transparent-Proxy-with-Burp-Suite]]

**Objective**: Configure a transparent proxy to intercept HTTPS traffic without client-side certificate trust, generating per-host CA-signed certificates for MITM.

**Instructions**: Launch Burp Suite and enable transparent mode. Configure it to generate CA-signed certificates for intercepted hosts like api.twitter.com.

**Expected Output**: Proxy listening on port 8080, ready to sign fake certificates.

**Success Indicators**:
- Burp Suite interface shows transparent proxy active
- No errors in proxy logs

### Step 2: Configure Rogue WiFi Access Point
procedure: [[procedures/Configure-Rogue-WiFi-Access-Point]]

**Objective**: Create a fake WiFi network on the attacker machine to lure the target iOS device into connecting, routing traffic through the local proxy.

**Instructions**: Set up the access point using hostapd or similar on the Linux machine with wlan0 interface, ensuring it's on the same host as the proxy.

**Expected Output**: Rogue WiFi SSID visible and joinable.

**Success Indicators**:
- iOS device detects the network
- Connection accepted without authentication

### Step 3: Redirect HTTPS Traffic Using iptables
procedure: [[procedures/Redirect-HTTPS-Traffic-Using-iptables]]

**Objective**: Use network rules to transparently forward all incoming HTTPS traffic from the rogue WiFi to the local proxy for interception.

**Instructions**: Apply iptables rules to DNAT and REDIRECT port 443 traffic from wlan0 to the proxy. Execute [[commands/iptables-dnat-https-to-proxy]] followed by [[commands/iptables-redirect-https-to-port]]:

```bash
iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 443 -j DNAT --to $BURP_IP:8080
iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 443 -j REDIRECT --to-port 8080
```

**Expected Output**: No output if successful; traffic is silently redirected.

**Success Indicators**:
- iptables rules listed with `iptables -t nat -L -v -n`
- Test ping or HTTP from another device routes through proxy

### Step 4: Connect iOS Device to Rogue WiFi
procedure: [[procedures/Connect-iOS-Device-to-Rogue-WiFi]]

**Objective**: Lure the target device onto the controlled network to route its traffic through the attacker setup.

**Instructions**: On the stock iPhone, join the rogue WiFi network without any custom profiles or jailbreak.

**Expected Output**: Device connected to the network, internet access appears functional.

**Success Indicators**:
- WiFi icon shows connection
- Basic connectivity tests (e.g., browsing) work but route through proxy

### Step 5: Launch Twitter App on iOS Device
procedure: [[procedures/Launch-Twitter-App-on-iOS-Device]]

**Objective**: Trigger the vulnerable app connections to api.twitter.com, initiating HTTPS requests that bypass certificate validation.

**Instructions**: Open the Twitter app on the connected iOS device, which will attempt to connect to endpoints like /1.1/help/settings.json.

**Expected Output**: App loads without SSL errors, sending requests.

**Success Indicators**:
- App interface appears normal
- No certificate warnings on device

### Step 6: Observe Intercepted Traffic in Proxy
procedure: [[procedures/Observe-Intercepted-Traffic-in-Proxy]]

**Objective**: Capture and analyze sensitive data from the app's requests, including OAuth tokens and headers, confirming the MITM success.

**Instructions**: Monitor Burp Suite for intercepted requests to api.twitter.com, viewing headers like Authorization (OAuth) and responses with security headers.

**Expected Output**: Logs show GET requests with tokens, e.g., 304 Not Modified responses.

**Success Indicators**:
- OAuth tokens visible in plain text
- Ability to modify or replay requests

## Attack Chain Summary

### Key Achievements

1. Successful MITM without CA installation on iOS device
2. Interception of OAuth tokens and auth details for potential account takeover
3. Demonstration of HSTS bypass and HTTP downgrade risks

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle
- [[LLMNR-NBT-NS Poisoning and SMB Relay]] LLMNR/NBT-NS Poisoning and Relay (adapted for WiFi proxying)

### MITRE ATT&CK Tactics

- [[Defense Evasion]] Defense Evasion

---

*Last updated: 2023-10-01T00:00:00Z*
