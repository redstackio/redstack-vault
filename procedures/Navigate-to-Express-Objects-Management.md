---
tags:
  - discovery
  - navigation
  - concrete-cms
  - express-objects
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T03:16:25.126Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: 8d18e84a-6fcd-4abc-933d-ef035e59e184
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Navigate-to-Express-Objects-Management

## Summary

This procedure involves accessing the Express entries management interface in Concrete CMS v8.1.0 after authentication, identifying the location for creating new objects where the XSS vulnerability exists.

## Description

Once authenticated, navigating to the Express module allows discovery of the vulnerable add object form. This step targets the /index.php/dashboard/express/entries endpoint, which lists entries and provides the 'Add Object' option. In the attack scenario, this positions the attacker to inject payloads. Prerequisites include an active session; outcomes include visibility of the management interface.

## Requirements

1. Active authenticated session in Concrete CMS
2. Permissions to access Express Objects (e.g., editor role)
3. Web browser for navigation

## Defense

Defensive measures and detection strategies:

- Role-based access control (RBAC) to limit Express module access
- Audit logs for dashboard navigation patterns
- Session timeout and monitoring for prolonged activity

## Objectives

1. Locate the Express entries page
2. Identify the add object functionality
3. Prepare for payload injection

## Instructions

### Step 1: Access Dashboard

**Context**: From the authenticated session, proceed to the main dashboard.

The browser is already at /index.php/dashboard post-login.

> Expected output: Dashboard menu visible.

### Step 2: Navigate to Express Entries

**Context**: Select the Express section to reach the vulnerable interface.

Click on 'Express' in the menu, then 'Entries' to visit /index.php/dashboard/express/entries.

> Expected output: Page loads showing entries list and 'Add Object' button.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- discovery
- navigation
