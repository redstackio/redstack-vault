---
tags:
  - proxy
  - ssl-pinning-bypass
  - traffic-interception
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Mobile (iOS)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:35.192Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 3edb6955-2d6d-4771-8e57-a889f05ed547
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Mobile-API-Traffic-with-Proxy

## Summary

This procedure sets up a proxy tool like Burp Suite to intercept HTTPS traffic from the MyMTN NG iOS app, including bypassing SSL certificate pinning to enable request capture and modification.

## Description

Mobile apps often use SSL pinning to prevent man-in-the-middle attacks, but this can be bypassed using tools like Frida or Objection. The procedure configures the device's proxy to route traffic through Burp Suite, installs the necessary CA certificate, and verifies interception. It's essential for analyzing and altering API calls in a controlled environment, targeting endpoints like /api/v2/rechargeTransactionHistory.

## Requirements

1. Burp Suite Professional installed on a connected machine (Mac/Windows/Linux)
2. iOS device or simulator with MyMTN NG app logged in
3. USB connection or same-network setup for proxy routing
4. Optional: Frida/Objection for pinning bypass

## Defense

Defensive measures and detection strategies:

- Implement certificate pinning with runtime checks and app hardening
- Detect proxy usage via network anomaly monitoring (e.g., non-standard TTLs)
- Use runtime integrity checks to identify hooking tools like Frida

## Objectives

1. Route app traffic through a controllable proxy
2. Bypass security measures to decrypt HTTPS
3. Enable real-time inspection of API requests/responses

## Instructions

### Step 1: Configure Burp Suite Proxy

**Context**: Start Burp and set up the listener for mobile traffic.

No specific command; GUI-based.

> In Burp, go to Proxy > Options, add listener on 127.0.0.1:8080 or device IP:8080. Export Burp CA certificate.

### Step 2: Setup Device Proxy and Certificate

**Context**: Point iOS device to proxy and trust the CA.

No command; device settings.

> On iOS: Settings > Wi-Fi > Configure Proxy > Manual, enter Burp IP:8080. Download and install Burp CA via Safari, then trust in Settings > General > VPN & Device Management.

### Step 3: Bypass SSL Pinning

**Context**: Use a tool to disable pinning if the app rejects the proxy certificate.

Example with Objection (requires setup):

```bash
objection -g com.mtn.mymtn explore
ios sslpinning disable
```

> Run Objection to hook the app process and disable pinning. Restart app and verify traffic flows through Burp without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/objection-bypass-pinning]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- proxy
- ssl-pinning-bypass
- traffic-interception
