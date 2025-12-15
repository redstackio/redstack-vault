---
id: proc-uuid-001
tags:
  - access-control-bypass
  - improper-authorization
  - web-vulnerability
  - data-manipulation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:17.927Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass Access Control to Create Tables in Restricted Spaces

## Summary

This procedure exploits improper access control in the Dust web application, allowing member users to create tables in restricted company data spaces designated for workspace builders (admins) only. By interacting with a visually disabled UI element that lacks server-side enforcement, attackers can perform unauthorized data creation, leading to potential tampering, clutter, or leakage.

## Description

In the Dust application, restricted data spaces rely on client-side UI restrictions, such as disabling the 'Add Data' button for non-admin users. However, these controls are not backed by server-side permission checks, enabling members to trigger table creation via UI interactions. This vulnerability was identified by authenticating as a member and navigating to a restricted space, where clicking the disabled button reveals functional options. Successful exploitation results in new tables being added without authorization, compromising data integrity and potentially exposing sensitive information if tables are populated with unauthorized content.

## Requirements

1. Valid member-level credentials for the Dust web application.
2. Web browser with JavaScript enabled for UI interactions.
3. Access to a restricted company data space within the workspace.

## Defense

Defensive measures and detection strategies:

- Implement server-side role-based access control (RBAC) validation for all data creation endpoints.
- Monitor audit logs for unauthorized table creations in restricted spaces, flagging member-initiated writes.
- Use UI frameworks that enforce non-interactive states for disabled elements (e.g., remove click handlers).
- Conduct regular permission audits and penetration testing on SaaS applications.

## Objectives

1. Gain unauthorized write access to admin-only data spaces using a member account.
2. Create persistent tables to enable further data manipulation.
3. Demonstrate the absence of backend authorization, highlighting escalation risks.

## Instructions

### Step 1: Authenticate as Member

**Context**: Establish a session with limited privileges to test access controls.

No specific command; use the web UI to log in with member credentials.

> Enter username and password on the login page. Expected: Dashboard access with member views.

### Step 2: Access Restricted Space

**Context**: Navigate to an admin-restricted area to probe UI elements.

Use the sidebar or menu to select a company data space.

> The space loads; verify read-only indicators for members. Expected: No immediate block.

### Step 3: Trigger Add Data Functionality

**Context**: Bypass visual disablement to access hidden features.

Locate and click the grayed-out 'Add Data' button.

> Button responds despite appearance. Expected: Menu with options like 'Create Table'.

### Step 4: Initiate Table Creation

**Context**: Select the creation method to load the form.

Choose 'Create Table' from the menu.

> Form appears for inputs. Expected: No permission prompt.

### Step 5: Submit Table Details

**Context**: Provide and save data to exploit the lack of checks.

Fill fields (e.g., table name: 'TestTable', columns: 'id:int, name:string') and click 'Save'.

> Submission processes. Expected: Success confirmation without errors.

### Step 6: Validate Creation

**Context**: Confirm the bypass by checking persistence.

Refresh the space listing.

> New table visible. Expected: Table listed and queryable by member.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- access-control-bypass
- improper-authorization
- web-vulnerability
