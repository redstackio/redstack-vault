---
tags:
  - csrf
  - token-extraction
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:33:06.096Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: f1f7259a-c867-4e91-94d3-08bbbef1c010
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Extract-CSRF-fkey-Token

## Summary

This procedure uses browser inspection to capture the fixed 'fkey' CSRF token from an active Khan Academy session for reuse in forged requests.

## Description

The fkey token in Khan Academy is a static value per browser that protects against CSRF but fails to update with session changes. This procedure involves inspecting authenticated pages or network traffic to extract it, setting up for scenarios like shared browsers or XSS theft. It assumes an active attacker session from prior login.

## Requirements

1. Active authenticated session on Khan Academy
2. Browser with developer console (e.g., Chrome DevTools)
3. Basic knowledge of HTML inspection

## Defense

Defensive measures and detection strategies:

- Bind CSRF tokens to unique sessions and regenerate them periodically
- Log and alert on unusual token access patterns
- Employ client-side token validation with short expiration

## Objectives

1. Obtain the exact fkey value
2. Confirm its static nature by checking multiple pages
3. Store for use in exploitation

## Instructions

### Step 1: Inspect Form Elements

**Context**: Load a page with forms containing the fkey and extract it.

Navigate to a settings or profile page (e.g., https://www.khanacademy.org/settings) and right-click a form > Inspect Element.

> Locate the hidden input field named 'fkey' and copy its value attribute (e.g., value="fixedtoken123").

### Step 2: Verify via Network Requests

**Context**: Confirm the token in outgoing requests to ensure consistency.

Submit a benign form action and monitor the Network tab in DevTools.

> Observe the fkey parameter in POST data; it should match the extracted value, proving fixation.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Credentials In Files]] Credentials In-Files

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[token-theft]]
