---
id: proc-uuid-add-client
tags:
  - wordpress
  - mainwp
  - client-management
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-13T23:52:50.135Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Add-New-Client-in-MainWP-Dashboard

## Summary

This procedure outlines creating a new client entry in the MainWP WordPress plugin dashboard, serving as the initial setup for accessing vulnerable editing features like the notes field.

## Description

In the context of exploiting the MainWP plugin, adding a new client provides a test subject for editing without affecting production data. The process involves navigating the admin interface and filling basic fields. Prerequisites include authenticated access to the MainWP dashboard. Expected outcomes are a new client profile ready for further manipulation, with no technical exploits in this step itself.

## Requirements

1. Authenticated session in MainWP dashboard
2. Access to client management section
3. Basic knowledge of WordPress admin navigation

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls to limit client creation to authorized admins
- Log all client additions for audit trails
- Monitor for unusual patterns in client management activities

## Objectives

1. Establish a target client for subsequent editing and exploitation
2. Verify dashboard functionality without triggering alerts
3. Prepare environment for payload injection

## Instructions

### Step 1: Access Client Management

**Context**: Log in and reach the section for managing clients to initiate creation.

No specific command; use the web interface to navigate to MainWP > Clients > Add New.

> Fill in required fields like client name and website URL, then save to create the entry.

### Step 2: Confirm Creation

**Context**: Validate the new client is listed and editable.

No specific command; refresh the clients list and check for the new entry.

> Successful creation shows the client in the dashboard list with edit options available.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[wordpress]]
- [[mainwp]]
- [[client-creation]]
