---
id: proc-slack-team-intercept
name: Create-Slack-Team-and-Intercept-Survey
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:22.312Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - race-condition
  - web
  - slack
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Create-Slack-Team-and-Intercept-Survey

## Summary

This procedure covers the initial setup of a new Slack team, password configuration, access to the account creation survey, and interception of the survey completion request using Burp Suite, setting the stage for exploiting a race condition.

## Description

In the context of Slack's account creation flow, this procedure involves standard registration to create a new team, followed by navigating to the survey page post-password setup. The survey is an optional step offering promotional credits upon completion. By intercepting the POST request with Burp Suite, attackers can capture the exact payload needed for replay. This targets the web-based endpoint on slack.com and requires no prior access, making it accessible for initial exploitation attempts. Expected outcomes include a captured request ready for duplication, enabling the race condition exploit.

## Requirements

1. Internet access to slack.com
2. Web browser with proxy support (e.g., Firefox or Chrome)
3. Burp Suite installed and configured as a proxy (port 8080)
4. Basic knowledge of HTTP requests and form submissions

## Defense

Defensive measures and detection strategies:

- Implement client-side rate limiting on survey submissions
- Use server-side idempotency keys or tokens to prevent duplicate processing
- Monitor for unusual patterns of concurrent requests from the same IP/session
- Log and alert on multiple successful survey completions in quick succession

## Objectives

1. Gain access to the survey completion endpoint
2. Capture the authentic POST request payload
3. Prepare for concurrent replay to exploit race condition

## Instructions

### Step 1: Create New Slack Team

**Context**: Start the registration process to establish a new workspace.

No specific command; use browser to visit https://slack.com/create and fill in team name, email, etc.

> Navigate through the signup flow until team creation confirmation.

### Step 2: Set Password and Access Survey

**Context**: Complete password setup to unlock the survey option.

No command; after email verification, set password and proceed to https://yourteam.slack.com/account/reset/complete.

> The page should present the survey as an optional step for new users.

### Step 3: Fill Survey and Intercept with Burp Suite

**Context**: Submit the survey while proxying through Burp to capture the request.

Configure browser proxy to 127.0.0.1:8080. Fill form fields (e.g., company size, industry) and submit.

> In Burp, the POST to /survey/6-23387113491-bed6344a95 will be intercepted, showing parameters like done2=1, crumb, etc.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[race-condition]]
- [[web]]
- [[slack]]
