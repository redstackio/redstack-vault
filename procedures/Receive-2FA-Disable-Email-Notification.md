---
tags:
  - email
  - notification
type: procedure
tools: []
tactics: []
commands: []
platforms:
  - Web
  - Email
techniques: []
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
id: a60456c3-bd9b-4dcf-b946-fdeb05aec992
created_at: '2025-12-14T17:24:45.448Z'
updated_at: '2025-12-14T17:24:45.448Z'
verified: false
validated: true
submitted: true
---
# Receive-2FA-Disable-Email-Notification

## Summary

This procedure involves monitoring and capturing the email notification sent after disabling 2FA on Legal Robot.

## Description

The platform's email system automatically notifies users of 2FA changes. Due to the logic error (checking services.u2f existence without enabled flag), it falsely references a security key. Check inbox promptly. Outcome: Receipt of misleading email.

## Requirements

1. Email account linked to Legal Robot
2. Access to email client or webmail

## Defense

Defensive measures and detection strategies:

- Use templating engines with proper conditionals (e.g., if services.u2f && services.u2f.enabled)
- Test notifications for all 2FA configs
- Monitor email send logs for errors

## Objectives

1. Capture post-disable notification
2. Document exact email content
3. Identify false security key reference

## Instructions

### Step 1: Monitor Inbox

**Context**: Wait for automated email.

After disable, refresh email inbox.

### Step 2: Open and Read

**Context**: Review notification details.

Open the email from Legal Robot and note the body text.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[email]]
- [[notification]]
