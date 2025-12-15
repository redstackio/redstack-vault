---
tags:
  - web
  - parameter
  - manipulation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:30.039Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 97d2808c-d47d-4da1-b14e-9faa3e714c84
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-URL-for-Unsubscribe-Access

## Summary

This procedure manipulates the URL parameter in the Nextcloud newsletter page to access the unsubscribe form, bypassing normal navigation and exposing the IDOR vulnerability.

## Description

By altering the 'p' parameter from 'subscribe' to 'unsubscribe' while keeping 'id=1', the endpoint reveals a form that accepts any email for unsubscription without verification. This direct object reference allows attackers to target specific users by email, highlighting the lack of access controls in the unsubscribe workflow compared to subscription.

## Requirements

1. Access to the subscription page URL
2. Web browser or proxy tool for URL modification
3. Basic understanding of URL parameters

## Defense

Defensive measures and detection strategies:

- Validate URL parameters server-side to prevent unauthorized endpoint access
- Log and monitor unusual parameter changes in access logs

## Objectives

1. Expose the unsubscribe form
2. Confirm minimal input requirements
3. Set up for IDOR exploitation

## Instructions

### Step 1: Alter the Parameter

**Context**: Change the page action from subscribe to unsubscribe.

Modify https://newsletter.nextcloud.com/?p=subscribe&id=1 to https://newsletter.nextcloud.com/?p=unsubscribe&id=1.

> Expected output: Page loads with an email input form only.

### Step 2: Inspect the Form

**Context**: Verify no additional protections.

Examine the form for fields; it should require only email input without CAPTCHA or confirmation.

> Expected output: Simple form ready for submission.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web
- parameter
