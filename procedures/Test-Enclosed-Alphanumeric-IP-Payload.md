---
tags:
  - ssrf
  - bypass
  - unicode
type: procedure
tools:
  - '[[tools/PHP]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/throw-if-local-ip-validation]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:53:38.268Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 12bdf736-59a4-430d-9f29-510e942f68e9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Enclosed-Alphanumeric-IP-Payload

## Summary

This procedure exploits Unicode enclosed alphanumerics to bypass IP validation for SSRF to AWS metadata.

## Description

Use the payload `⑯⑨。②⑤④。⑯⑨｡②⑤④` which visually and functionally resolves to 169.254.169.254 but evades `filter_var` by appearing as a non-private IP. Test via ?ip=; it passes `ThrowIfLocalIp` but may be caught by `ThrowIfLocalAddress` hostname checks. Enables access to cloud metadata for information disclosure.

## Requirements

1. Local test script with validation functions
2. Unicode support in PHP (default)
3. Target internal endpoint like AWS metadata

## Defense

Defensive measures and detection strategies:

- Normalize inputs with punycode or ASCII conversion before validation
- Block non-ASCII characters in URL parameters

## Objectives

1. Bypass `filter_var` private range checks
2. Access reserved IPs like AWS metadata
3. Highlight encoding evasion risks

## Instructions

### Step 1: Craft Payload

**Context**: Encode IP with fullwidth and enclosed characters.

No command; prepare `⑯⑨。②⑤④。⑯⑨｡②⑤④`.

> Expected: Payload ready for testing.

### Step 2: Test Bypass

**Context**: Validate against IP function.

Execute [[commands/throw-if-local-ip-validation]] with ?ip=⑯⑨。②⑤④。⑯⑨｡②⑤④:

```bash
php test.php?ip=⑯⑨。②⑤④。⑯⑨｡②⑤④
```

> Expected: 'Pass' output; filter_var sees it as public IP.

### Step 3: Check Host Validation

**Context**: Test full URI in address function.

Use updated script; expected partial bypass until hostname dot count fix.

> Expected: Potential exception from substr_count($host, '.') === 0.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/throw-if-local-ip-validation]]

## Tools Used

- [[tools/PHP]]

## Tags

- ssrf
- bypass
- unicode
