---
id: proc-ssl-test-mobile-001
tags:
  - ssl-validation
  - mitm-testing
  - android
  - ios
type: procedure
tools:
  - '[[tools/themeninthemiddle-com]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Android
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1417]]'
updated_at: '2025-12-14T17:24:39.715Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1417]]'
---
# Test-SSL-Certificate-Validation-in-Mobile-Apps

## Summary

This procedure tests mobile applications for improper SSL/TLS certificate validation, specifically failures in verifying certificate authorities (CA) and hostnames, which can enable man-in-the-middle attacks. It is used to identify vulnerable apps during security assessments or bug bounty hunting.

## Description

In this procedure, you systematically evaluate popular Android and iOS apps by simulating invalid certificates using man-in-the-middle techniques. The target environment includes HTTPS communications in apps like Uber, Authy, and Capital One Spark Pay. Prerequisites include an Android/iOS device or emulator, network control for proxying, and access to testing tools. Expected outcomes are confirmation of validation bypasses, allowing attackers to intercept sensitive data without user warnings. This flaw often stems from developers disabling validation for testing or misconfiguring WebView components.

## Requirements

1. Android or iOS device/emulator with target apps installed.
2. Network setup for traffic interception (e.g., Wi-Fi hotspot or ADB for Android).
3. Testing tool like themeninthemiddle.com to simulate invalid certificates.

## Defense

Defensive measures and detection strategies:

- Implement proper certificate pinning and hostname verification in app code.
- Use tools like OWASP ZAP or Burp Suite to test validation during development.
- Monitor for anomalous network traffic or proxy usage on devices.

## Objectives

1. Identify apps that fail to validate SSL certificates, enabling MITM.
2. Document vulnerable endpoints and data flows.
3. Recommend fixes like enabling strict CA and hostname checks.

## Instructions

### Step 1: Setup Testing Environment

**Context**: Prepare the device to route app traffic through a testing proxy or site that presents invalid certificates.

For Android, use ADB to set a proxy:

```bash
adb shell settings put global http_proxy 127.0.0.1:8080
```

> This command configures the device to proxy HTTP/HTTPS traffic. If using themeninthemiddle.com, access the site via browser on the device to generate test scenarios.

### Step 2: Test Certificate Validation

**Context**: Interact with the app to trigger HTTPS requests while presenting forged certificates; observe if validation fails.

Navigate to app features involving logins or payments, and check proxy logs or site output for unblocked connections.

No specific command; monitor via tool interface. For example, use the testing site to simulate CA mismatch.

> Expected output: App proceeds with connection, logging shows no validation error (e.g., "Certificate verified: false" ignored).

### Step 3: Verify Hostname Checks

**Context**: Test for hostname verification by using a proxy with mismatched domain certificates.

Repeat app interactions; success if app accepts mismatched hostname.

> This confirms full MITM feasibility.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[T1417]] Improper Certificate Validation (Mobile-specific)

### Sub-Techniques

-

## Commands Used

-

## Tools Used

- [[tools/themeninthemiddle-com]]

## Tags

- [[ssl-validation]]
- [[mitm-testing]]
- [[android]]
- [[ios]]
