---
id: proc-1043804-form-submit-xss
tags:
  - xss
  - form-submission
  - account-takeover
  - javascript
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/execute-form-submission-js]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:06.583Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute-Unauthorized-Form-Submission-via-XSS

## Summary

This procedure leverages an active XSS payload to automatically submit forms on behalf of the user, such as closing accounts or exporting data from IntenseDebate's your-information page.

## Description

Once XSS is triggered, inject JavaScript to target form elements by ID (e.g., 'frm2') and submit them without user consent. This executes in the authenticated context, performing destructive actions like account deletion. Requires the victim to load the malicious URL while logged in.

## Requirements

1. Established XSS execution from prior injection
2. Logged-in session to the target site
3. Knowledge of form IDs from site inspection

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on forms
- Monitor for unexpected submissions in audit logs
- Use event listeners to detect automated interactions

## Objectives

1. Automate form submission for unauthorized actions
2. Achieve account manipulation or data exfiltration
3. Demonstrate high-impact exploitation

## Instructions

### Step 1: Modify Payload for Form Submission

**Context**: Replace alert with submission code in the XSS payload.

Payload example:

```javascript
"><script>document.getElementById('frm2').submit();</script>
```

Embed in URL as before.

> This selects the form and triggers submit() on load.

### Step 2: Load in Authenticated Browser

**Context**: Ensure session is active, then trigger.

Use [[tools/Firefox]] with login.

**Expected Output**: Form submits silently, e.g., account closure confirmation or data export initiation.

> Check account status post-execution for changes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/execute-form-submission-js]]

## Tools Used

- [[tools/Firefox]]

## Tags

- xss
- form-hijacking
- escalation
