---
id: proc-uuid-002
tags:
  - session-hijack
  - cookies
  - govslack
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:30:35.459Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[Credentials In Files]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Obtain-GovSlack-Session-Cookies

## Summary

This procedure generates session cookies from an attempted sign-in on slack-gov.com, where direct workspace creation is restricted, providing tokens for subsequent request replays.

## Description

GovSlack (slack-gov.com) enforces invitation-only access, disabling self-service workspace creation. By attempting a login—which may fail due to restrictions—this step establishes a partial session, extracting cookies like session IDs or auth tokens via browser tools. These cookies can impersonate a legitimate session when combined with payloads from slack.com. The target environment is the GovSlack web interface, requiring only public access. Outcomes include cookies ready for injection into modified requests, enabling bypass of auth controls.

## Requirements

1. Access to slack-gov.com
2. Firefox browser for cookie management
3. No valid GovSlack credentials needed (failed login suffices)

## Defense

Defensive measures and detection strategies:

- Enforce short-lived cookies and validate against IP/user-agent mismatches
- Log failed login attempts and correlate with anomalous API calls
- Implement CSRF tokens on login endpoints to prevent cookie-only replays

## Objectives

1. Establish a GovSlack session without full authentication
2. Extract cookies for use in unauthorized requests
3. Confirm session viability for payload replay

## Instructions

### Step 1: Navigate to GovSlack Login

**Context**: Initiate a sign-in attempt to trigger cookie generation.

Open Firefox and go to slack-gov.com. Click on the sign-in option and enter arbitrary credentials (e.g., a test email and password).

**Expected Output**: Login attempt processed, even if failed.

### Step 2: Extract Cookies

**Context**: Retrieve session cookies from the browser after the attempt.

In Firefox DevTools (Storage tab or Application tab), locate and copy cookies set during the session, such as those under slack-gov.com domain.

**Expected Output**: List of cookies including session-related ones.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques

- [[Credentials In Files]]

## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- session-hijack
- cookies
