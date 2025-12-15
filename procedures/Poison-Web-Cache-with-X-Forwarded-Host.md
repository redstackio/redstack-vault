---
id: proc-smule-poison-cache-001
name: Poison-Web-Cache-with-X-Forwarded-Host
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:50.360Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - web-cache-poisoning
  - x-forwarded-host
commands:
  - '[[commands/modify-get-with-x-forwarded-host]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Poison-Web-Cache-with-X-Forwarded-Host

## Summary

This procedure exploits a web cache poisoning vulnerability by injecting an unvalidated X-Forwarded-Host header into a GET request to Smule's user group page, causing the server to rewrite HTML links to an attacker-controlled host like localhost, which gets cached and served to victims.

## Description

In the Smule application, the server processes the X-Forwarded-Host header without proper validation, using it to generate absolute URLs in the HTML response. By setting this header to 'localhost', an attacker poisons the shared cache. When a victim loads the cached page, any interactions (e.g., login forms) submit to the attacker's server instead of Smule's, enabling data interception. This targets Ruby on Rails-based endpoints like /s/smule_groups/user_groups/<username> and requires no authentication.

## Requirements

1. Proxy tool like Burp Suite for request interception and modification
2. Network access to www.smule.com over HTTPS
3. Attacker-controlled server running on localhost or equivalent (port 80)

## Defense

Defensive measures and detection strategies:

- Validate and sanitize forwarded headers like X-Forwarded-Host, rejecting non-origin domains
- Implement cache key inclusion of sensitive headers or use per-user caching
- Monitor for anomalous headers in access logs and unusual redirects in responses

## Objectives

1. Poison the web cache with rewritten URLs pointing to attacker host
2. Ensure the poisoned response is cached and served to victims
3. Set up for subsequent data disclosure during victim interactions

## Instructions

### Step 1: Intercept GET Request

**Context**: Use Burp Suite to capture the initial request to the target user group page.

**Command** ([[commands/modify-get-with-x-forwarded-host]]):

No direct command; configure Burp Suite proxy to intercept https://www.smule.com/s/smule_groups/user_groups/fossnow27.

> This step captures the raw GET request for modification. Expected output: Intercepted HTTP request in Burp Repeater.

### Step 2: Add X-Forwarded-Host and Forward

**Context**: Modify the request to include the poisoning header and send it to the server.

**Command** ([[commands/modify-get-with-x-forwarded-host]]):
```http
GET /s/smule_groups/user_groups/fossnow27 HTTP/1.1
Host: www.smule.com
X-Forwarded-Host: localhost
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Cookie: [redacted cookies]
Connection: close
Upgrade-Insecure-Requests: 1
If-None-Match: W/"74107fb6dcc410390f339e5ddabc3022"
Cache-Control: max-age=0
```

> Forward the modified request via Burp. Expected output: 200 OK response with HTML links rewritten to http://localhost/.

### Step 3: Verify Poisoning

**Context**: Inspect the response to confirm URL rewriting occurred.

No command; view response in Burp.

> Look for action links and footer URLs pointing to localhost. Success confirms cache poisoning.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/modify-get-with-x-forwarded-host]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[web-cache-poisoning]]
- [[x-forwarded-host]]
