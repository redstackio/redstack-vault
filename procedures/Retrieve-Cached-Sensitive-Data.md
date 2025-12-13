---
tags:
  - data-theft
  - web-cache-deception
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-retrieve-cached-page]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 9122f383-aaf9-429d-9473-02640b4b4c7e
created_at: '2025-12-13T09:00:34.043Z'
updated_at: '2025-12-13T09:00:34.043Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Retrieve Cached Sensitive Data

## Summary

This procedure covers accessing the cached sensitive pages from vulnerable kaspersky.com subdomains after a successful phishing-induced caching, allowing theft of user information without authentication.

## Description

Once the victim has cached the page, the attacker requests the same URL, and due to misconfiguration, the cache serves the sensitive content to anyone. This completes the Web Cache Deception attack.

## Requirements

1. Phishing link successfully visited by victim
2. Vulnerable URL known
3. Basic web access

## Defense

Defensive measures and detection strategies:

- Restrict cache access to authenticated users
- Log and alert on repeated requests to cached sensitive paths

## Objectives

1. Exfiltrate sensitive user data
2. Validate the full exploit chain
3. Demonstrate impact of vulnerability

## Instructions

### Step 1: Request Cached Page

**Context**: Fetch the cached content.

**Command** ([[commands/curl-retrieve-cached-page]]):
```bash
curl https://subdomain.kaspersky.com/sensitive-page.css
```

> The response contains the victim's sensitive data.

### Step 2: Extract Data

**Context**: Parse the retrieved content for sensitive information.

Manually review or script extraction of user details.

> Expected: Stolen information like account data.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-retrieve-cached-page]]

## Tools Used



## Tags

- data-theft
- web-cache-deception
