---
id: proc-stripo-role-bypass-001
tags:
  - improper-authorization
  - role-downgrade
  - bypass-ui
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/PUT-Update-User-Role-to-Admin]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:28.702Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-Frontend-to-Downgrade-Owner-Role

## Summary

This procedure exploits an improper authorization vulnerability in Stripo's web application by bypassing frontend restrictions on the users management UI, allowing an admin to downgrade the organization owner's role to admin via a manipulated PUT request, resulting in the owner's account lockout.

## Description

In Stripo's organization management interface, the frontend disables role changes for the owner to prevent downgrades, but the backend API at PUT /cabinet/stripeapi/v1/organizations/{orgId}/users lacks proper authorization checks. An admin can inspect and modify the disabled input using browser tools, change the role to 'admin', and submit, triggering an unauthorized update. This locks the owner out as they lose elevated privileges and cannot log in. The attack requires admin access and targets web-based SaaS environments like Stripo.email.

## Requirements

1. Valid admin credentials in the target organization
2. Owner account to set up the organization (for testing)
3. Modern browser with developer tools (e.g., Firefox 70.0 or later)
4. Network access to https://my.stripo.email

## Defense

Defensive measures and detection strategies:

- Implement backend authorization checks to prevent role downgrades by non-owners
- Disable or validate all user inputs server-side, rejecting changes to owner roles
- Monitor API logs for unexpected PUT requests to user endpoints from admin accounts
- Use role-based access control (RBAC) with immutable owner roles

## Objectives

1. Gain unauthorized control over organization roles by downgrading the owner
2. Lock out the legitimate owner from accessing the account and organization
3. Demonstrate improper authorization in web UIs relying on client-side controls

## Instructions

### Step 1: Setup and Access Management UI

**Context**: Prepare accounts and navigate to the users page as admin to view the disabled owner role input.

Log in as admin and access https://my.stripo.email/cabinet/#/users/{orgId}.

**Expected Output**: UI loads with owner's role shown as disabled.

### Step 2: Enable Disabled Input with Developer Tools

**Context**: Use [[tools/Browser-Developer-Tools]] to inspect and modify the HTML, removing the 'disabled' attribute on the owner's role input.

Press F12 to open dev tools, inspect the role element (e.g., <input disabled>), and edit to remove 'disabled='disabled''.

**Expected Output**: Input field becomes editable in the browser.

### Step 3: Modify and Submit Role Change

**Context**: Change the role to 'admin' and save, sending the PUT request.

**Command** ([[commands/PUT-Update-User-Role-to-Admin]]):

Use the browser to submit or execute via dev tools/network tab:

```http
PUT /cabinet/stripeapi/v1/organizations/{orgId}/users HTTP/1.1
Host: my.stripo.email
Authorization: Bearer {token}
Content-Type: application/json;charset=UTF-8

{"id":{userId},"role":"admin","organizationId":{orgId},...}
```

> This command updates the user's role via API. Expected output is HTTP 200 with JSON confirming {"role":"admin"}. Verify by attempting owner login, which should fail.

### Step 4: Validate Lockout

**Context**: Confirm the impact by logging in as owner.

Attempt login with owner credentials; access should be denied due to lost privileges.

**Expected Output**: Login failure or restricted access to organization.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/PUT-Update-User-Role-to-Admin]]

## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[improper-authorization]]
- [[role-downgrade]]
- [[account-lockout]]
