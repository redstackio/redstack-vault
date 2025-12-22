---
tags:
  - information-disclosure
  - cache-retrieval
type: procedure
tools: []
tactics:
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:13.488Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: e78eb0e7-8e4a-40db-a392-163f1976267c
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Retrieve-Poisoned-Cache-Content-as-Unauthenticated-User

## Summary

This procedure retrieves sensitive user data from a poisoned web cache by accessing the crafted URL in an unauthenticated session, exploiting the lack of auth-state cache keying.

## Description

Following cache poisoning, unauthenticated requests to the same .css URL serve the cached authenticated content, disclosing details like email and member ID. This targets web apps like Lyst.com where static URL patterns bypass auth checks in caching. Expected outcome: Direct access to victim data without credentials.

## Requirements

1. Knowledge of the poisoned URL from prior step
2. Incognito or private browser mode to simulate unauthenticated access
3. Network connectivity to the target

## Defense

Defensive measures and detection strategies:

- Enforce authentication for all dynamic content, even under static extensions
- Log and invalidate cache entries with suspicious user data patterns
- Use content security policies to prevent rendering of cached dynamic content

## Objectives

1. Extract cached sensitive information without authentication
2. Validate the poisoning success and gather user details
3. Highlight risks to user privacy

## Instructions

### Step 1: Initiate Unauthenticated Session

**Context**: Ensure no credentials are present to simulate an external attacker.

Open a new incognito/private browsing window and navigate to the target site's homepage without logging in.

> Expected output: Public, non-personalized view of the site.

### Step 2: Access Poisoned URL

**Context**: Fetch the cached response containing user data.

Visit the exact poisoned URL (e.g., `https://www.lyst.com/shop/trends/mens-dress-shoes/blahblah.css`). View the page source or use browser dev tools to inspect the response.

> Expected output: HTML/JS with leaked data, e.g., `email: "victim@lyst.com"`, `member_id: 12345`, `username: victim_user`.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[information-disclosure]]
- [[web-cache-poisoning]]
