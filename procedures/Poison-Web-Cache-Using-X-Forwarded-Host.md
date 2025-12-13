---
tags:
  - web-cache-poisoning
  - header-manipulation
type: procedure
tools:
  - '[[tools/wget]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/wget-cache-poisoning-loop]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 68fd55d2-9953-4208-8897-71a3eb497a51
created_at: '2025-12-13T09:00:34.139Z'
updated_at: '2025-12-13T09:00:34.139Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Poison Web Cache Using X-Forwarded-Host

## Summary

This procedure exploits improper validation of the X-Forwarded-Host header in web caching mechanisms, such as those in Discourse forums, by repeatedly sending manipulated requests to inject malicious content into the cache for later retrieval.

## Description

The attack targets caching systems that trust the X-Forwarded-Host header without proper sanitization, allowing attackers to poison cached responses with arbitrary hosts or payloads. This can lead to stored XSS, defacement, or phishing when victims access the poisoned pages. The procedure involves looping HTTP requests to ensure the cache is overwritten. Prerequisites include network access to the target and a vulnerable caching setup.

## Requirements

1. Access to a command-line environment (e.g., Linux terminal)
2. Installed wget tool
3. Target URL with vulnerable caching (e.g., Discourse forum)

## Defense

Defensive measures and detection strategies:

- Validate and sanitize X-Forwarded-Host headers in caching logic
- Monitor for anomalous header values in web server logs

## Objectives

1. Inject malicious content into the web cache
2. Enable downstream attacks like XSS or phishing
3. Confirm cache manipulation through repeated requests

## Instructions

### Step 1: Execute Poisoning Loop

**Context**: Send repeated GET requests with the manipulated header to overwrite the cache.

**Command** ([[commands/wget-cache-poisoning-loop]]):
```bash
while true; do wget "https://help.nextcloud.com/?qwKzzSR=649227948379" --header 'X-Forwarded-Host: cyberjutsu.io/#' -qO- >/dev/null; echo "poisoning...";done
```

> This command loops indefinitely, injecting the malicious host into each request to poison the cache.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/wget-cache-poisoning-loop]]

## Tools Used

- [[tools/wget]]

## Tags

- web-cache-poisoning
- header-manipulation
