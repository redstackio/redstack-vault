---
tags:
  - nextcloud
  - email-test
  - api-abuse
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:32:01.513Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: aa5f54ba-d320-43c8-b52c-872db5dd836b
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Send-Test-Email-from-Admin-Settings-in-Nextcloud

## Summary

This procedure triggers Nextcloud's email test function from the admin interface to send a single email to the configured personal address, verifying the setup for bombing and demonstrating the unrestricted API.

## Description

Nextcloud's admin additional settings include a 'Send test mail' button that calls the /settings/admin/mailtest API, sending an email via the configured server to the personal email address. Without rate limits, this can be repeated. The procedure assumes admin access and prior email configuration; outcome is a delivered test email to the victim.

## Requirements

1. Administrator access to Nextcloud admin settings
2. Email server configured and functional in Nextcloud
3. Personal email set to victim address from prior step

## Defense

Defensive measures and detection strategies:

- Add rate limiting to the mailtest API endpoint
- Require confirmation or CAPTCHA for test sends
- Monitor email server logs for burst sends from admin IPs

## Objectives

1. Send initial test email to confirm targeting
2. Validate API endpoint accessibility
3. Observe delivery to victim's inbox

## Instructions

### Step 1: Access Admin Settings

**Context**: Navigate to the additional admin settings page.

Go to https://target.nextcloud.com/settings/admin/additional in the browser.

> This displays server configuration options, including email testing.

### Step 2: Trigger Test Email

**Context**: Click the send button to invoke the API.

Locate and click 'Send test mail'.

> A success notification appears, and the API POST to /settings/admin/mailtest executes, sending the email.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[nextcloud]]
- [[dos]]
- [[api]]
