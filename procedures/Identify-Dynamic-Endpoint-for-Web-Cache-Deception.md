---
tags:
  - web-cache-deception
  - recon
type: procedure
tools:
  - '[[tools/Web-Cache-Deception-Concept]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-manipulate-url-for-caching]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: ba21af9e-670c-40a2-a91a-996b144874af
created_at: '2025-12-13T09:00:34.606Z'
updated_at: '2025-12-13T09:00:34.606Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Dynamic Endpoint for Web Cache Deception

## Summary

This procedure identifies a dynamic endpoint in a web application that reflects sensitive data like CSRF tokens and can be manipulated to cache responses by appending static file extensions, enabling web cache deception attacks.

## Description

Web cache deception exploits path confusion where dynamic content is treated as static and cached. In Glassdoor, this allows caching of user-specific responses containing gdToken. The procedure involves testing endpoints for cacheability and token reflection.

## Requirements

1. Access to the target web application (e.g., Glassdoor)
2. Tools for URL manipulation and response analysis
3. Knowledge of the application's endpoints

## Defense

Defensive measures and detection strategies:

- Implement proper cache controls to prevent caching of dynamic content
- Monitor for unusual URL patterns with static extensions on dynamic paths

## Objectives

1. Locate vulnerable endpoint for caching
2. Confirm token reflection in responses
3. Verify path confusion exploitability

## Instructions

### Step 1: Enumerate Dynamic Endpoints

**Context**: Scan and identify endpoints that return user-specific data like gdToken.

**Command** ([[commands/curl-manipulate-url-for-caching]]):
```bash
curl "https://www.glassdoor.com/dynamic-endpoint"
```

> This fetches the response to check for gdToken presence.

### Step 2: Test for Cache Deception

**Context**: Append static extension and check if the response is cacheable.

**Command** ([[commands/curl-manipulate-url-for-caching]]):
```bash
curl "https://www.glassdoor.com/dynamic-endpoint.css"
```

> Analyze headers for caching indicators.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-manipulate-url-for-caching]]

## Tools Used

- [[tools/Web-Cache-Deception-Concept]]

## Tags

- web-cache-deception
- recon
