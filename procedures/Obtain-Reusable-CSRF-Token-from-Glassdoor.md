---
id: proc-glassdoor-csrf-token-001
tags:
  - csrf
  - token-theft
  - web
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:57.830Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Obtain Reusable CSRF Token from Glassdoor

## Summary

This procedure retrieves a CSRF token from glassdoor.com servers, exploiting the lack of proper validation to obtain a reusable token for forging requests on victim accounts.

## Description

In the context of the site-wide CSRF vulnerability on glassdoor.com, attackers can inspect legitimate requests to endpoints like profile or dashboard pages to extract CSRF tokens. These tokens are not uniquely bound to sessions or origins, allowing reuse in cross-site requests. This step is foundational for crafting forged POST actions affecting job seeker and employer accounts. Prerequisites include access to a logged-in session (via social engineering) or observation of victim traffic.

## Requirements

1. Victim logged into www.glassdoor.com
2. Attacker's ability to observe or simulate a request to Glassdoor (e.g., via phishing page or proxy)
3. Basic web development knowledge for inspecting HTTP responses

## Defense

Defensive measures and detection strategies:

- Implement unique, session-bound CSRF tokens with origin checking
- Monitor for anomalous POST requests from unexpected referers
- Use Content Security Policy (CSP) to restrict form submissions

## Objectives

1. Extract a valid CSRF token for reuse
2. Enable subsequent forged requests without authentication
3. Prepare for unauthorized account actions

## Instructions

### Step 1: Inspect Legitimate Request

**Context**: Log in to glassdoor.com as a victim (or simulate via proxy) and navigate to an action page like employer dashboard or job seeker profile to trigger a token-inclusive response.

Use browser developer tools (Network tab) to capture the request:

Open DevTools (F12), go to a page that loads forms, and look for tokens in headers like X-CSRF-Token or form hidden fields.

> Expected output: Token visible in response body or headers, e.g., <input type="hidden" name="_csrf" value="abc123">

### Step 2: Extract and Store Token

**Context**: Copy the token value for use in malicious forms.

Manually extract the token string from the inspected response.

> Expected output: Reusable token string ready for inclusion in forged requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web-exploitation]]
