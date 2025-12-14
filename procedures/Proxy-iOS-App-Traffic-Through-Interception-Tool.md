---
id: proc-uuid-002
tags:
  - mitm
  - proxy
  - traffic-interception
  - ios
type: procedure
tools:
  - '[[tools/Burp-Proxy]]'
  - '[[tools/mitmproxy]]'
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:24:39.444Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Proxy-iOS-App-Traffic-Through-Interception-Tool

## Summary

This procedure configures an iOS device's network settings to route Shopify POS app traffic through a proxy tool like Burp or mitmproxy, leveraging the trusted malicious certificate to avoid SSL errors and enable interception.

## Description

With the malicious certificate trusted, the iOS device can be set to proxy all Wi-Fi traffic to the attacker's machine running Burp Proxy or mitmproxy on a specific port. The Shopify POS app, lacking pinning, will not detect the interception and will send HTTPS traffic that the proxy can decrypt using the attacker's CA. This step assumes the attacker is on the same network and requires manual proxy configuration on the device.

## Requirements

1. Malicious certificate already installed and trusted on iOS
2. Attacker's machine with proxy tool running and CA imported
3. Same Wi-Fi network for device and attacker

## Defense

Defensive measures and detection strategies:

- Enforce certificate pinning in the app to break proxy interception
- Monitor for manual proxy settings in Wi-Fi configurations
- Use network monitoring to detect anomalous traffic routing to unauthorized proxies

## Objectives

1. Redirect app traffic to attacker's proxy
2. Ensure seamless HTTPS handling without app crashes
3. Position for traffic decryption in the next step

## Instructions

### Step 1: Start Proxy Tool

**Context**: Launch the interception tool on the attacker's machine.

For Burp Proxy:

```bash
# Launch Burp Suite and configure listener on 0.0.0.0:8080
# Import malicious CA into Burp's trust store
```

> Expected output: Proxy listening; CA imported for signing responses.

For mitmproxy:

```bash
mitmproxy --mode transparent --listen-port 8080
```

> Expected output: mitmproxy console showing readiness.

### Step 2: Configure iOS Proxy

**Context**: Set the device's Wi-Fi to manual proxy.

On iOS: Settings > Wi-Fi > Tap (i) next to network > Configure Proxy > Manual > Server: attacker-IP, Port: 8080.

**Expected Output**: Proxy settings saved; no immediate errors.

### Step 3: Launch App and Generate Traffic

**Context**: Test routing by using the app.

Open Shopify POS, log in, and perform an action like viewing inventory.

**Expected Output**: Proxy logs show incoming requests from device IP.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Adversary-in-the-Middle]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Proxy]]
- [[tools/mitmproxy]]

## Tags

- mitm
- proxy
- ios
