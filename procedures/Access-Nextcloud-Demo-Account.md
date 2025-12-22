---
id: p-nextcloud-demo-access
tags:
  - initial-access
  - nextcloud
  - demo
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T05:32:13.205Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Nextcloud-Demo-Account

## Summary

This procedure outlines gaining initial access to a Nextcloud instance using the public demo account, providing a testing environment for the Contacts app without needing custom credentials.

## Description

The Nextcloud demo allows anonymous access via a guided wizard, simulating a real user session. This is the entry point for exploiting vulnerabilities in apps like Contacts. Expected outcomes include a logged-in session with full app access, enabling subsequent upload tests. Prerequisites include a web browser and internet access to the Nextcloud site.

## Requirements

1. Web browser with JavaScript enabled
2. Internet connection to access Nextcloud demo
3. No authentication credentials required

## Defense

Defensive measures and detection strategies:

- Disable or restrict demo/public instances in production
- Implement rate limiting on login wizards
- Monitor for unusual demo access patterns

## Objectives

1. Establish authenticated session in Nextcloud
2. Access the Contacts app interface
3. Prepare for file upload exploitation

## Instructions

### Step 1: Navigate to Nextcloud Connection Wizard

**Context**: Use the official Nextcloud site to initiate demo access.

**Instructions**: Open a web browser and go to the Nextcloud download or connection page, then select 'Register with a provider' > 'Demo' > 'Take me there!'.

> This redirects to the demo instance and auto-logs you in.

### Step 2: Verify Session

**Context**: Confirm access to core features like Contacts.

**Instructions**: Once loaded, navigate to the Apps section and ensure the Contacts app is available and opens without errors.

> Successful access shows the demo dashboard with app icons.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[initial-access]]
- [[nextcloud]]
