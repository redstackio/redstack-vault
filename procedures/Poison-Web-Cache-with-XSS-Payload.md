---
tags:
  - cache-poisoning
  - xss
  - discourse
type: procedure
tools:
  - '[[tools/webcachedeception-php]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/inject-xss-via-cache-poisoning-script]]'
platforms:
  - Web
  - AWS
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 077cc40f-0978-4b44-8e0b-897bb443c7b5
created_at: '2025-12-13T09:00:34.562Z'
updated_at: '2025-12-13T09:00:34.562Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Poison Web Cache with XSS Payload

## Summary

This procedure automates the injection of an XSS payload into a Discourse instance's web cache using a PHP script, poisoning the cache for a specified duration to enable stored XSS attacks.

## Description

The procedure exploits improper handling of the X-Forwarded-Host header in Discourse's font loading code, allowing malicious scripts to be injected into cached HTML responses. It targets the caching mechanism that stores responses for 1 minute based on specific headers, amplifying the XSS impact by serving poisoned content to multiple users.

## Requirements

1. Access to the webcachedeception.php script
2. Network access to the target Discourse URL
3. Web browser or HTTP client for sending requests

## Defense

Defensive measures and detection strategies:

- Implement strict header validation and sanitization in font loading code
- Configure cache to ignore or validate user-controlled parameters and headers

## Objectives

1. Poison the web cache with XSS payload
2. Set up for stored XSS execution
3. Demonstrate cache deception vulnerability

## Instructions

### Step 1: Execute Cache Poisoning Script

**Context**: Access the PHP script with parameters to inject the XSS payload into the target cache.

**Command** ([[commands/inject-xss-via-cache-poisoning-script]]):
```bash
https://blackfan.ru/bugbounty/webcachedeception.php?url=https://meta.discourse.org/?cacheattack&payload=%22%3E%3Cscript%3Ealert(document.domain)%3C/script%3E&cache=60
```

> This command sets the target URL with a cacheattack parameter, injects an encoded XSS script, and poisons the cache for 60 seconds. Expected output: Displays the poisoned cache URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/inject-xss-via-cache-poisoning-script]]

## Tools Used

- [[tools/webcachedeception-php]]

## Tags

- [[cache-poisoning]]
- [[xss]]
