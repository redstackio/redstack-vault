---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - privilege-escalation
  - lark
  - cloud
  - authorization-bypass
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:07.408Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Self-Approve-App-for-Privilege-Escalation-in-Lark

## Summary

This procedure exploits a vulnerability in Lark Technologies' app approval process, allowing a non-privileged user to approve their own app without admin intervention, resulting in privilege escalation and potential unauthorized access to tenant-wide resources.

## Description

In Lark tenants, apps typically require admin approval for installation to prevent unauthorized access. However, due to a lack of enforcement in the approval workflow, non-privileged users can self-approve apps, bypassing security controls. This leads to mass privilege escalations, as the approved app can access sensitive data or other apps within the same tenant. The vulnerability was reported on HackerOne (Report #1168475) and affects cloud-based Lark deployments. Prerequisites include a valid non-privileged account; no special tools are needed beyond a web browser. Expected outcomes include immediate app approval and elevated permissions, potentially compromising the entire tenant.

## Requirements

1. Valid non-privileged user account in a Lark tenant
2. Web browser access to the Lark platform (e.g., https://your-tenant.larksuite.com)
3. Basic understanding of Lark's app management interface

## Defense

Defensive measures and detection strategies:

- Enforce strict admin-only approval workflows with audit logging
- Implement role-based access controls (RBAC) to prevent self-approval
- Monitor for anomalous app approvals by non-admin users via SIEM tools
- Regularly audit app permissions and tenant access logs

## Objectives

1. Bypass admin approval to install a custom app
2. Escalate privileges to access restricted tenant resources
3. Enable mass unauthorized actions across multiple apps

## Instructions

### Step 1: Access Lark App Management

**Context**: Log in to the Lark tenant and navigate to the app creation or management section to prepare for self-approval.

Log in using non-privileged credentials at the Lark web interface. Go to the "Apps" or "Integrations" section in the tenant admin or user dashboard.

> Upon successful login, the dashboard loads without errors, displaying app-related options.

### Step 2: Create or Select an App

**Context**: Develop or select a pending app that requires approval, setting the stage for the bypass.

Create a new app via the Lark developer console or select an existing unapproved app. Configure basic app details, such as scopes requesting elevated permissions (e.g., access to tenant data).

> The app is created and enters a "Pending Approval" state, but no admin notification is enforced.

### Step 3: Self-Approve the App

**Context**: Exploit the lack of admin enforcement to approve the app directly, triggering privilege escalation.

In the app details page, locate the approval button or workflow. Click to submit and approve the app as the non-privileged user. The system fails to validate admin privileges, completing the approval.

> The app status updates to "Approved" and installs, granting the requested permissions without alerts.

### Step 4: Validate Escalation

**Context**: Test the escalated privileges by accessing restricted resources.

Use the approved app to query tenant data or interact with other apps. Attempt actions previously denied, such as reading user lists or approving other apps.

> Successful access to elevated resources confirms the escalation; monitor for any delayed admin notifications.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- privilege-escalation
- lark
- cloud
- authorization-bypass
