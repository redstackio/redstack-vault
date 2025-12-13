---
tags:
  - web-cache-poisoning
  - x-forwarded-host
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/get-with-x-forwarded-host]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 97623269-d685-4c11-a14e-7756a5e8cf0d
created_at: '2025-12-13T09:00:34.301Z'
updated_at: '2025-12-13T09:00:34.301Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject X-Forwarded-Host to Poison Web Cache

## Summary

This procedure involves intercepting an HTTP request to a vulnerable page on Smule and injecting the X-Forwarded-Host header to poison the web cache, causing subsequent responses to redirect links to an attacker-controlled host.

## Description

The attack targets the Smule user groups page, where improper validation of the X-Forwarded-Host header allows cache poisoning. This modifies cached responses to point action links (e.g., login checks) to a malicious server, enabling data disclosure. Prerequisites include access to the target URL and a tool like Burp Suite for request interception. Expected outcome is a poisoned cache serving altered content.

## Requirements

1. Access to the vulnerable URL: https://www.smule.com/s/smule_groups/user_groups/user_name
2. Burp Suite or similar proxy tool
3. Ability to send modified HTTP requests

## Defense

Defensive measures and detection strategies:

- Validate and restrict X-Forwarded-Host headers in web applications and caches
- Monitor for anomalous header injections in logs

## Objectives

1. Poison the web cache to redirect requests
2. Alter response links to attacker host
3. Enable subsequent data disclosure

## Instructions

### Step 1: Intercept and Modify Request

**Context**: Use a proxy to capture the GET request and add the poisoning header.

**Command** ([[commands/get-with-x-forwarded-host]]):
```bash
GET /s/smule_groups/user_groups/fossnow27 HTTP/1.1
Host: www.smule.com
X-Forwarded-Host: localhost
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Cookie: [redacted]
Connection: close
Upgrade-Insecure-Requests: 1
If-None-Match: W/"74107fb6dcc410390f339e5ddabc3022"
Cache-Control: max-age=0
```

> This command injects X-Forwarded-Host: localhost, poisoning the cache and modifying links in the response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/get-with-x-forwarded-host]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- web-cache-poisoning
- x-forwarded-host
