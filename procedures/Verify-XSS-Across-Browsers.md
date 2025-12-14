---
tags:
  - xss
  - verification
  - browser
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/test-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:38.998Z'
sub_techniques: []
id: f99a8218-5ec2-478b-9458-189cbe64b10b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify XSS Across Browsers

## Summary

This procedure reproduces the reflected XSS payload in multiple browsers to confirm broad exploitability and lack of browser-specific mitigations.

## Description

After initial XSS confirmation, testing in Firefox, IE, and Edge ensures the vulnerability isn't limited by rendering engines or security features. The same GET payload is used, highlighting improper handling in the CGI response.

## Requirements

1. Multiple browsers installed (Firefox, IE, Edge)
2. Valid XSS payload from prior test
3. Target endpoint access

## Defense

Defensive measures and detection strategies:

- Test applications across browsers during security audits
- Implement consistent escaping regardless of client
- Log user-agent anomalies with payloads

## Objectives

1. Validate XSS consistency
2. Identify any browser mitigations
3. Ensure reliable exploitation

## Instructions

### Step 1: Replay Payload in Firefox

**Context**: Load the crafted URL to check execution.

**Command** ([[commands/test-xss-payload]]):
```bash
# Load in Firefox: http://target/cgi-bin/PasswordCreate.pl?email=%26nslookup... (full URL)
```

> Expected output: Alert(1) executes.

### Step 2: Test in IE and Edge

**Context**: Repeat in legacy and modern browsers.

**Command** (Browser Load):
```bash
# Load same URL in IE and Edge
```

> Expected output: Alert appears in both, confirming cross-browser vuln.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/test-xss-payload]]

## Tools Used


## Tags

- [[xss]]
- [[verification]]
- [[browser]]
