---
id: p2b3c4d5-e6f7-8901-bcde-f2345678901
tags:
  - ssti
  - email-trigger
  - jinja2
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:08.805Z'
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
# Trigger-Uber-Email-Notification-to-Confirm-SSTI

## Summary

This procedure triggers an email notification after profile injection to observe and confirm the SSTI by checking if the Jinja2 expression is evaluated in the rendered email body.

## Description

Once the profile name contains the injected payload, updating the profile or performing related actions sends an email via support@uber.com. The template processes the name field, evaluating Jinja2 if vulnerable, revealing the injection point in the email generation server.

## Requirements

1. Injected payload already set in profile name
2. Access to email inbox for Uber notifications
3. Ability to trigger profile-related emails

## Defense

Defensive measures and detection strategies:

- Escape user data in email templates using Jinja2's |e filter
- Log template rendering events for injection attempts
- Rate-limit profile updates to prevent abuse

## Objectives

1. Provoke rendering of the injected template
2. Validate SSTI through output observation
3. Identify email as the exploitation vector

## Instructions

### Step 1: Perform Triggering Action

**Context**: Initiate a profile update or account change to queue an email.

Make a minor profile change, such as updating another field, to send the 'Your Uber account information has been updated' email.

### Step 2: Inspect Received Email

**Context**: Check the email for evaluated payload to confirm vulnerability.

Open the email from support@uber.com and examine the name in the body.

> Look for '7777777' instead of the raw `{{ '7'*7 }}` payload.

**Expected Output**: Email arrives with rendered expression in the name field.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssti]]
- [[email]]
- [[web]]
