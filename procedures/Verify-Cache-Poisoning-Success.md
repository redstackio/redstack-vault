---
tags:
  - web-cache-poisoning
  - verification
type: procedure
tools:
  - '[[tools/wget]]'
  - '[[tools/grep]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/wget-cache-verification-loop]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: e81db4f2-2a10-43b7-a99b-9d0b8a14d5ad
created_at: '2025-12-13T09:00:34.135Z'
updated_at: '2025-12-13T09:00:34.135Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify Cache Poisoning Success

## Summary

This procedure checks if a web cache has been successfully poisoned by querying the target URL and searching for injected malicious content in the responses.

## Description

After attempting to poison the cache, this verification step sends repeated requests and uses pattern matching to detect the presence of the injected domain or payload. It's essential for confirming the attack's success before proceeding to exploitation. The target must be a web application with a cache that reflects the poisoned content.

## Requirements

1. Access to a command-line environment
2. Installed wget and grep tools
3. Knowledge of the injected content (e.g., domain string)

## Defense

Defensive measures and detection strategies:

- Implement cache key normalization to prevent header-based poisoning
- Log and alert on repeated requests to the same URL

## Objectives

1. Confirm presence of malicious content in cached responses
2. Validate the effectiveness of the poisoning attack
3. Provide indicators for successful cache manipulation

## Instructions

### Step 1: Execute Verification Loop

**Context**: Send repeated GET requests and grep the output for the injected string.

**Command** ([[commands/wget-cache-verification-loop]]):
```bash
while true; do wget "https://help.nextcloud.com/?qwKzzSR=649227948379" -qO- | grep "cyberjutsu.io"; echo "ping my payload..." ;done
```

> This command checks responses for 'cyberjutsu.io' to verify if the cache serves the poisoned content.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/wget-cache-verification-loop]]

## Tools Used

- [[tools/wget]]
- [[tools/grep]]

## Tags

- web-cache-poisoning
- verification
