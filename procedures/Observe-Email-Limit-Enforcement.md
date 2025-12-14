---
id: proc-uuid-001
tags:
  - recon
  - web
  - limit-testing
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:24:22.816Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Observe-Email-Limit-Enforcement

## Summary

This procedure manually tests the Mozilla Monitor web interface to observe and confirm the enforced limit of 5 monitored email addresses, establishing the baseline for exploitation.

## Description

In the Mozilla Monitor staging environment, users are restricted to monitoring up to 5 email addresses for data breaches. This step involves navigating to the user settings and adding emails sequentially to trigger and verify the limit enforcement, which relies on server-side counters that can be bypassed via concurrency issues.

## Requirements

1. Authenticated access to https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net/user/settings
2. Valid Mozilla Monitor user account
3. Web browser (e.g., Firefox)

## Defense

Defensive measures and detection strategies:

- Implement client-side validation alongside server-side checks
- Log and monitor rapid email addition attempts
- Rate limit API calls per user session

## Objectives

1. Verify the 5-email limit is active
2. Document the failure behavior for the 6th addition
3. Prepare for API-level testing

## Instructions

### Step 1: Access User Settings

**Context**: Log in and navigate to the settings page to begin manual additions.

No command required; use the web UI to visit https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net/user/settings.

> Expected: Page loads with current email list (initially empty).

### Step 2: Add Emails Manually

**Context**: Add up to 5 unique emails one at a time via the form.

Use the UI input field and submit button for each.

> Expected: Each of the first 5 additions succeeds with a confirmation message.

### Step 3: Test Limit Exceedance

**Context**: Attempt a 6th addition to observe enforcement.

Submit another email via the form.

> Expected: Error message like "You have reached the maximum of 5 emails."

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- recon
- web
- limit-testing
