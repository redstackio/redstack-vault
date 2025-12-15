---
tags:
  - ip-disclosure
  - email-exfiltration
  - information-leak
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
  - '[[Hardware]]'
updated_at: '2025-12-14T17:25:13.417Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 8bfba983-2369-4d7d-8e71-04ee28f53e7e
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Trigger-IP-Disclosure-via-Cancellation

## Summary

This procedure describes monitoring for the server-triggered email after the victim submits the CSRF, which discloses their IP address to the attacker.

## Description

Upon POST to /token.cgi, Bugzilla processes the cancellation and emails the account owner (attacker) a notification including the requesting IP for 'security' purposes. This leaks the victim's IP without consent. Prerequisites: Prior steps completed and email monitoring. Expected outcome: Receipt of IP in email for reconnaissance.

## Requirements

1. Access to attacker's email inbox
2. Valid token in payload
3. Victim submission

## Defense

Defensive measures and detection strategies:

- Remove IP logging from non-essential emails like cancellations
- Anonymize or omit client IP in notifications
- Audit email templates for sensitive data exposure

## Objectives

1. Confirm CSRF execution via server response
2. Collect victim's IP for further targeting
3. Validate information disclosure

## Instructions

### Step 1: Monitor Email Inbox

**Context**: Wait for server notification.

Check the email associated with the Bugzilla account for the cancellation alert.

**Expected Output**: Email body containing "Cancellation request from IP: [Victim's IP]".

### Step 2: Verify Token Cancellation

**Context**: Confirm action on Bugzilla.

Log into Bugzilla and check account settings or attempt another reset to see if token is invalidated.

**Expected Output**: Token no longer valid; IP extracted from email.

> Use the IP for geolocation via tools like ipinfo.io.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Hardware]] Gather Victim Network Information: IP Addresses

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ip-disclosure
- email-exfiltration
- information-leak
