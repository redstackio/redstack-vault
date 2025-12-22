---
id: proc-acronis-register-token
tags:
  - registration
  - token
  - initial-access
type: procedure
tools: []
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
updated_at: '2025-12-14T17:32:29.042Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Register Acronis Account to Obtain Token

## Summary

This procedure involves registering a new partner account on the Acronis website to generate a personal token embedded in an API URL, serving as the starting point for IDOR exploitation.

## Description

The Acronis partner registration form at https://www.acronis.com/en-us/partners/registration/ creates a permanent token for form autocompletion, which includes user details and a predictable structure. This token is crucial for subsequent analysis and modification in the IDOR attack, targeting the /api/v1/lead/ endpoint. No authentication is required beyond completing the public form, making it accessible to any attacker.

## Requirements

1. Web browser with access to the internet
2. Basic personal details for registration (e.g., name, email)
3. No prior Acronis account needed

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA on registration forms to deter automated sign-ups
- Monitor for unusual registration patterns or rapid account creation
- Rate-limit registrations and token generations

## Objectives

1. Gain initial access to an Acronis token
2. Establish a baseline for token predictability analysis
3. Prepare for brute-force enumeration of other users' data

## Instructions

### Step 1: Access Registration Form

**Context**: Navigate to the public partner registration page to begin the process.

Visit https://www.acronis.com/en-us/partners/registration/ in your browser.

> This loads the form without any barriers.

### Step 2: Complete Registration

**Context**: Fill out the form to trigger token generation.

Provide minimal details such as name, email, company, and submit the form.

> Upon submission, the system generates a token-embedded URL for autocompletion.

### Step 3: Capture Token URL

**Context**: Inspect the post-registration redirect or response to extract the token.

Use browser developer tools (F12) to view the network tab or URL bar for the API endpoint like https://www.acronis.com/en-us/api/v1/lead/id:929-HVV-335&token:_mch-acronis.com-<timestamp>-<integer>.

> Expected output: Full token URL with timestamp and integer (e.g., -39235).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- registration
- token-acquisition
