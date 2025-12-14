---
tags:
  - nextcloud
  - email-config
  - abuse-functionality
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:01.517Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 35b55deb-c676-4255-b01e-be8f89cbba95
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set-Personal-Email-to-Target-in-Nextcloud

## Summary

This procedure configures the personal email address in Nextcloud settings to a victim's email, enabling redirection of test emails for subsequent bombing attacks. It exploits the lack of validation on email fields in the admin-personal settings.

## Description

In Nextcloud, administrators can update their personal email via the web interface without restrictions, allowing any arbitrary address to be set. This step is the foundation for email bombing, as the test email function uses this configured address as the recipient. The target environment is a Nextcloud instance with admin access; no additional tools are needed beyond a browser. Expected outcome: All test emails route to the victim, setting up for unlimited sends.

## Requirements

1. Administrator login credentials for Nextcloud
2. Access to the personal settings page (e.g., https://target.nextcloud.com/settings/personal)
3. Victim's email address

## Defense

Defensive measures and detection strategies:

- Implement email field validation to restrict to domain-approved addresses
- Log changes to personal settings and alert on suspicious updates
- Rate-limit admin configuration changes

## Objectives

1. Redirect test email recipient to victim address
2. Verify configuration persistence
3. Prepare for API abuse in follow-on steps

## Instructions

### Step 1: Access Personal Settings

**Context**: Log in and navigate to the personal settings to locate the email field.

Navigate to https://target.nextcloud.com/settings/personal in your browser.

> This loads the form with current user details, including the email input.

### Step 2: Update Email Field

**Context**: Enter the victim's email and save to apply the change.

Update the email field to the target's address (e.g., victim@example.com) and click save.

> The UI updates without validation errors, confirming the new recipient for tests.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[nextcloud]]
- [[email-bomb]]
- [[web]]
