---
tags:
  - csrf
  - web
  - scanning
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-csrf-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:49.852Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 718d7f8b-5011-4f35-bf7c-4e49e801656e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Scan-for-Site-wide-CSRF-Vulnerabilities

## Summary

This procedure systematically tests multiple endpoints across a domain like eats.uber.com for CSRF protections by omitting tokens in requests to various actions, revealing if the flaw is isolated or site-wide.

## Description

Attackers expand from a single vulnerable endpoint to map the scope, testing forms for profile updates, orders, or payments. Using a proxy, requests are modified and replayed without tokens. Success across endpoints indicates poor implementation, increasing impact for attacks like mass account manipulation. Requires authenticated access and endpoint enumeration.

## Requirements

1. List of target endpoints (e.g., via site crawl or documentation)
2. Authenticated session for the domain
3. Web proxy for request manipulation

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens universally on all mutable endpoints
- Implement Content Security Policy (CSP) to restrict form submissions
- Log and alert on requests missing tokens or from suspicious origins

## Objectives

1. Identify all vulnerable endpoints
2. Quantify the scope of the CSRF issue
3. Prioritize high-impact actions for exploitation

## Instructions

### Step 1: Enumerate Endpoints

**Context**: Identify key state-changing endpoints using browser inspection or automated crawling.

Manually list or use Burp's site map to find POST endpoints like /api/update-address, /api/place-order.

### Step 2: Test Each Endpoint Without Token

**Context**: Replay requests omitting CSRF tokens to check validation.

For each endpoint, use curl to submit without token.

**Command** ([[commands/curl-csrf-test]]):
```bash
curl -X POST 'https://eats.uber.com/api/update-profile' \
  -H 'Cookie: session=valid_session_cookie' \
  -d 'email=new@example.com&name=Test User' \
  --insecure
```

> Repeat for other endpoints; success without token confirms vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-csrf-test]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[scanning]]
