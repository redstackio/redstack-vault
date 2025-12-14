---
tags:
  - csrf
  - web
  - discovery
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 091addb9-283b-4089-b780-dd0e505489a3
created_at: '2025-12-14T17:27:36.179Z'
updated_at: '2025-12-14T17:27:36.179Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Identify-Missing-CSRF-Protection-in-Profile-Settings

## Summary

This procedure involves inspecting the profile privacy toggle endpoint on ok.ru to detect the absence of CSRF token validation, confirming the vulnerability that allows forged requests from external sites.

## Description

In the context of security testing on ok.ru, this procedure targets the 'Closed Profile' or 'Friends only' mode feature. By analyzing network requests during legitimate toggles, testers can verify that the state-changing POST endpoint lacks CSRF protection, making it susceptible to cross-site forgery. This is critical as it enables attackers to manipulate user privacy without consent, potentially exposing profiles to unintended viewers.

## Requirements

1. Access to a logged-in ok.ru account for testing
2. Browser with developer tools (e.g., Chrome DevTools)
3. Knowledge of web request inspection

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Monitor for anomalous POST requests to privacy settings
- Educate users on phishing links and same-site restrictions

## Objectives

1. Confirm lack of CSRF validation on privacy toggle
2. Document endpoint details for exploitation planning
3. Assess potential privacy impact

## Instructions

### Step 1: Inspect Legitimate Request

**Context**: Log in to ok.ru and navigate to profile settings to toggle 'Closed Profile' mode, capturing the request.

Open browser developer tools (Network tab) and perform the toggle action. Observe the POST request to the privacy endpoint (e.g., /settings/privacy/toggle).

> Look for absence of CSRF token in headers or form data. Expected: No token field like _csrf or similar.

### Step 2: Test Tokenless Request

**Context**: Attempt a direct POST without token to validate vulnerability.

Use browser console or a simple script to send a tokenless POST mimicking the toggle. If successful, vulnerability confirmed.

> Success: Endpoint processes request and toggles setting without error.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[Discovery]]
