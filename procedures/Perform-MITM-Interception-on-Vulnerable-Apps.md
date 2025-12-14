---
id: proc-mitm-intercept-mobile-001
tags:
  - mitm
  - data-interception
  - ssl-bypass
  - android
  - ios
type: procedure
tools:
  - '[[tools/themeninthemiddle-com]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Android
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:24:39.708Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[LLMNR-NBT-NS Poisoning and SMB Relay]]'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Perform-MITM-Interception-on-Vulnerable-Apps

## Summary

This procedure exploits identified SSL certificate validation flaws in mobile apps to set up a man-in-the-middle attack, intercepting and potentially exfiltrating sensitive data like passwords and credit card information over HTTPS.

## Description

Targeting vulnerable apps on Android (e.g., Outlook.com, Zappos) and iOS, this involves configuring a proxy to forge certificates that bypass validation. The attack scenario assumes network proximity (e.g., public Wi-Fi). Prerequisites: Vulnerable app confirmed, MITM tool ready, device routing setup. Outcomes include decrypted traffic capture, enabling data theft. Root cause: Disabled validation or WebView misconfigurations.

## Requirements

1. Confirmed vulnerable app from prior testing.
2. MITM proxy tool (e.g., mitmproxy) and controlled network.
3. Device access for proxy configuration (e.g., via ADB or settings).

## Defense

Defensive measures and detection strategies:

- Enforce certificate pinning in apps to reject forged certs.
- Detect proxy usage via app integrity checks or network monitoring.
- Use VPNs with strong validation on devices.

## Objectives

1. Decrypt and intercept app traffic without detection.
2. Capture sensitive data transmissions.
3. Demonstrate impact for disclosure or patching.

## Instructions

### Step 1: Configure MITM Proxy

**Context**: Set up the proxy to intercept traffic and present invalid certificates.

Run mitmproxy in transparent mode:

```bash
mitmproxy --mode transparent --set upstream_cert=false --listen-port 8080
```

> This starts the proxy; configure device to route through it (e.g., Wi-Fi proxy settings).

### Step 2: Route Device Traffic

**Context**: Direct the target's app traffic through the proxy.

For Android:

```bash
adb shell settings put global http_proxy host_ip:8080
```

> Replace host_ip with proxy machine IP. Launch the app and trigger HTTPS actions.

### Step 3: Intercept and Analyze Data

**Context**: Monitor proxy for decrypted payloads.

Interact with app (e.g., login); view flows in mitmproxy interface.

> Expected output: Plaintext requests/responses, e.g., {"card_number": "1234-..."}.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Sub-Techniques

- [[LLMNR-NBT-NS Poisoning and SMB Relay]] Traffic Signaling

## Commands Used

-

## Tools Used

- [[tools/themeninthemiddle-com]]

## Tags

- [[mitm]]
- [[data-interception]]
- [[android]]
- [[ios]]
