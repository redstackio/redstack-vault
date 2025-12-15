---
tags:
  - csrf
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-logout]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:23.658Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: d50cf36f-ef42-423d-a781-55938eb35451
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Identify-Logout-Endpoint

## Summary

This procedure involves manually testing a web application's authentication features to identify if the logout endpoint is vulnerable to CSRF by using a GET method without token protection, as seen in the Weblate demo site.

## Description

In Django-based applications like Weblate, the logout functionality at /accounts/logout/ may be implemented insecurely, allowing direct access via GET requests from cross-origin sites. This procedure simulates manual discovery through browser inspection or simple HTTP requests, confirming the endpoint's exposure. Prerequisites include access to the target site and basic knowledge of web requests; no special privileges are needed. Expected outcome is verification of the vulnerability for further exploitation.

## Requirements

1. Access to the target web application (e.g., https://demo.weblate.org)
2. Browser or command-line tool like curl for testing
3. Understanding of HTTP methods and CSRF concepts

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints, including logout
- Use POST method for logout to prevent accidental or forged requests
- Monitor for unusual logout patterns in access logs

## Objectives

1. Confirm the logout endpoint's method and protection status
2. Document the vulnerability for reporting or exploitation
3. Assess potential for session disruption attacks

## Instructions

### Step 1: Inspect Authentication Flow

**Context**: Navigate the site's login and logout features to locate the endpoint URL.

**Command** ([[commands/curl-test-logout]]):
```bash
curl -X GET https://demo.weblate.org/accounts/logout/ -v
```

> This command sends a GET request to the logout endpoint and displays verbose output, revealing if any CSRF checks fail or are absent. Expected output includes a 302 redirect to login without token errors.

### Step 2: Verify Cross-Origin Access

**Context**: Test if the endpoint can be triggered from a different origin without authentication barriers.

**Command** ([[commands/curl-test-logout]]):
```bash
curl -X GET https://demo.weblate.org/accounts/logout/ --referer https://attacker.com -v
```

> By spoofing a referer from an attacker-controlled site, confirm the request succeeds, indicating CSRF vulnerability. Success shows no rejection based on origin.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-logout]]

## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[recon]]
