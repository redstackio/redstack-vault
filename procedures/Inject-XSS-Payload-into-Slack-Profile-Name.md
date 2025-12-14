---
id: proc-uuid-1
tags:
  - xss
  - injection
  - slack
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:14.606Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload into Slack Profile Name

## Summary

This procedure involves updating the user's Slack profile name with a malicious XSS payload, such as "><img src=x onerror=prompt(12);>, which is stored but sanitized on the profile page itself, preventing immediate execution.

## Description

In the context of Slack's stored XSS vulnerability, the profile name field accepts input that is validated and escaped when displayed on the user's profile page. However, this same input is later included in help ticket data without proper encoding. This step sets up the payload for later triggering. The attack requires an authenticated Slack session and targets the web interface. Expected outcome: Payload stored without execution, ready for use in subsequent steps.

## Requirements

1. Authenticated access to a Slack workspace.
2. Web browser with developer tools for inspection (optional).
3. No additional tools needed; performed manually via UI.

## Defense

Defensive measures and detection strategies:

- Implement consistent output encoding across all display contexts (e.g., profile vs. integrated apps like Zendesk).
- Use Content Security Policy (CSP) to restrict inline script execution.
- Monitor for unusual profile name changes via audit logs.

## Objectives

1. Store malicious JavaScript in the profile name field.
2. Verify sanitization on profile view to confirm no immediate impact.
3. Prepare for payload execution in downstream views.

## Instructions

### Step 1: Access Profile Settings

**Context**: Log in and navigate to the profile editing interface to input the payload.

No command required; use the Slack UI:

- Click on your profile picture in the top-right.
- Select "View profile" then "Edit profile".
- In the name field, enter: `"><img src=x onerror=prompt(12);>` or alternative like `}'); ">ppp>`.
- Save changes.

> The save succeeds, but viewing the profile shows sanitized output (no execution).

### Step 2: Verify Profile Update

**Context**: Confirm the payload is stored without triggering XSS.

- Refresh the profile page.
- Inspect the name display; it should appear altered but no prompt fires due to validation.

> Expected: No JavaScript execution; name visible but escaped.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- slack
- profile-injection
