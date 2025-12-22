---
id: proc-header-injection-cookie
tags:
  - header-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:13.396Z'
skill_level: advanced
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# HTTP-Header-Injection-via-Language-Cookie

## Summary

This procedure attempts header injection by injecting newline characters into the MONERO_LANG cookie, but it's mitigated by PHP and CloudFlare protections.

## Description

In language.php, the cookie value is directly inserted into an HTTP header without escaping, potentially allowing manipulation. However, PHP since 5.1.2 prevents CRLF injection, and CloudFlare adds safeguards, limiting impact.

## Requirements

1. Access to set cookies on getmonero.org
2. Tools to manipulate HTTP requests (e.g., Burp)
3. Understanding of header injection payloads

## Defense

Defensive measures and detection strategies:

- Escape user input in headers (e.g., str_replace for CRLF)
- Use secure cookie handling and validation
- Employ WAF to block injection attempts

## Objectives

1. Inject malicious headers via cookie
2. Potential for response splitting (mitigated)
3. Test for legacy vulnerabilities

## Instructions

### Step 1: Set Malicious Cookie

**Context**: Inject payload into MONERO_LANG.

**Instructions**: Set cookie to value like "en\r\nX-Injected: malicious" via browser dev tools or proxy.

**Expected Output**: N/A.

### Step 2: Trigger Endpoint

**Context**: Visit language.php to process cookie.

**Instructions**: Request https://getmonero.org/language.php with the cookie.

**Expected Output**: No injection due to mitigations; normal response.

**Success Indicators**:
- No header manipulation observed
- Confirms mitigations in place

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- cookie-injection
- mitigated
