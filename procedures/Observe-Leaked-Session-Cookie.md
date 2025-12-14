---
tags:
  - credential-leak
  - observation
  - bug-bounty
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-extract-cookie]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:33:34.559Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 289ba336-f9e7-49f8-85ed-54e5417bb144
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Observe-Leaked-Session-Cookie

## Summary

This procedure involves monitoring public bug bounty reports for accidentally disclosed session cookies in comments, typically from unredacted cURL commands pasted by analysts during vulnerability reproduction.

## Description

In security platforms like HackerOne, analysts may copy cURL commands directly from browser developer consoles to demonstrate exploits, inadvertently including active session cookies. Attackers can review these public comments to extract the cookie, which is often domain-bound but lacks IP or device restrictions, enabling reuse for account takeover. This targets web-based platforms with session authentication and relies on human error rather than technical flaws.

## Requirements

1. Access to public bug bounty reports on hackerone.com
2. Basic knowledge of HTTP headers and cookies
3. Web browser or text editor for reviewing comments

## Defense

Defensive measures and detection strategies:

- Implement automated redaction tools for sensitive data in comments (e.g., scan for cookie patterns)
- Enforce session binding to IP addresses or user agents
- Train analysts on redacting credentials in reproductions
- Monitor for anomalous logins from leaked cookies

## Objectives

1. Identify exposed session cookies in report comments
2. Extract cookie value for potential reuse
3. Validate cookie's domain and scope

## Instructions

### Step 1: Review Bug Bounty Reports

**Context**: Search for reports with reproduction comments containing cURL snippets.

**Command** ([[commands/curl-extract-cookie]]):
```bash
# No direct command; manually inspect via browser: Open report page and search for 'Cookie:' in comments
```

> Manually scan the comment text for lines like 'Cookie: __session=abc123...' and copy the value. Expected output: Isolated cookie string.

### Step 2: Validate Cookie Format

**Context**: Confirm the cookie is a valid session token for the platform.

**Command** ([[commands/curl-extract-cookie]]):
```bash
curl -v https://hackerone.com/reports/example 2>&1 | grep -i cookie
```

> Use grep or browser dev tools to pattern-match. Expected output: Confirmation of cookie presence in headers.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used

- [[commands/curl-extract-cookie]]

## Tools Used


## Tags

- [[credential-leak]]
- [[observation]]
