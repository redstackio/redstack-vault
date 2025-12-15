---
tags:
  - csrf
  - inspection
  - oauth
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
updated_at: '2025-12-14T17:24:35.318Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 633e76f1-8e9d-49b8-a069-e4e9fbe7ac6a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inspect-OAuth-Authorization-URL

## Summary

This procedure involves examining the OAuth authorization URL generated during Slack's Google Drive integration to detect the absence of the state parameter, which acts as an anti-CSRF token.

## Description

During OAuth flows, the state parameter prevents CSRF attacks by tying requests to user sessions. In Slack's implementation, its omission allows attackers to hijack sessions. This procedure targets web-based OAuth endpoints, requiring browser access post-initiation. Outcomes include confirmation of the vulnerability and documentation for reporting.

## Requirements

1. Generated OAuth URL from the initiation step.
2. Browser developer tools (e.g., Chrome DevTools Network tab).
3. Basic understanding of URL parameters and OAuth 2.0.

## Defense

Defensive measures and detection strategies:

- Enforce inclusion of state parameters in all OAuth requests with server-side validation.
- Log and alert on OAuth requests missing state or with mismatched values.
- Conduct regular security audits of integration flows using tools like OWASP ZAP.

## Objectives

1. Parse and analyze URL components for security tokens.
2. Identify CSRF risks due to missing parameters.
3. Document findings for vulnerability validation.

## Instructions

### Step 1: Copy the Authorization URL

**Context**: Extract the full URL from the browser after OAuth redirection.

Right-click the address bar and copy the link, or use DevTools to capture the request.

> Example URL: https://accounts.google.com/o/oauth2/auth?response_type=code&redirect_uri=https%3A%2F%2Fslack.com%2Fservices%2Fauth%2Fgdrive&client_id=19570130570-tfuuvh6hutjd09bq64is5sao643q67jg.apps.googleusercontent.com&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive&access_type=offline&approval_prompt=force

### Step 2: Analyze Parameters

**Context**: Check for the presence of the 'state' query parameter.

Decode the URL and search for 'state='; note its absence, which prevents session binding.

> This confirms the root cause: no anti-CSRF protection, enabling session hijacking.

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
- [[oauth]]
- [[inspection]]
