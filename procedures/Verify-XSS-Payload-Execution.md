---
id: proc-verify-xss-execution
tags:
  - xss-verification
  - execution-test
  - stored-xss
  - oberlo
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:18.234Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify-XSS-Payload-Execution

## Summary

This procedure tests the stored XSS by viewing the profile to confirm JavaScript execution, validating the vulnerability's impact on other users.

## Description

After injection, the payload is reflected without escaping when the profile is loaded, executing in the viewer's browser context. Use a separate session or incognito mode to simulate a victim. This demonstrates potential for session hijacking or data theft. Prerequisites: payload injection; outcomes: visible script execution like an alert.

## Requirements

1. Injected payload in profile
2. Ability to view profiles (e.g., another account or public view)
3. Web browser

## Defense

Defensive measures and detection strategies:

- Output encode all dynamic content on rendering
- Monitor for anomalous JavaScript errors in client logs
- Implement browser-based XSS auditors or extensions

## Objectives

1. Trigger payload execution on profile load
2. Confirm lack of sanitization
3. Assess impact on victim browsers

## Instructions

### Step 1: Prepare Victim Session

**Context**: Simulate a non-attacker view to test execution.

Log out or open an incognito window; optionally create/use another account.

> This ensures clean session without attacker cookies.

### Step 2: View Affected Profile

**Context**: Load the page where the payload is reflected.

Navigate to a page displaying the profile name, such as the user's own profile view or a shared link.

> The name field content is rendered, triggering the payload.

### Step 3: Observe Execution

**Context**: Check for JavaScript alert or other effects.

Upon page load, an alert should pop up displaying the document domain (e.g., app.oberlo.com).

> Successful execution confirms the stored XSS; no alert indicates failure or mitigation.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-verification]]
- [[execution-test]]
- [[stored-xss]]
- [[oberlo]]
