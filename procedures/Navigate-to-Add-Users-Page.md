---
tags:
  - navigation
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:56.679Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: c5f335f0-e3fe-403a-8f51-41af7db3d72e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Navigate-to-Add-Users-Page

## Summary

This procedure guides the user from the Shopify Plus dashboard to the 'Add users' invitation page, positioning the attacker to exploit the information disclosure vulnerability.

## Description

Once authenticated, navigation occurs through the admin UI or direct URL access. The 'Add users' page is part of the User management section unique to Shopify Plus, differing from standard plans by allowing premature user detail checks during invitations. This step ensures the vulnerable form is loaded without triggering any session-based restrictions.

## Requirements

1. Active authenticated session in Shopify Plus dashboard
2. User management permissions
3. Knowledge of the shop identifier ([id])
4. Standard web browser

## Defense

Defensive measures and detection strategies:

- Log and alert on access to sensitive admin endpoints like /users/invite
- Role-based access controls (RBAC) to limit navigation to authorized users
- Audit trails for UI interactions in admin panels

## Objectives

1. Load the invitation form interface
2. Confirm availability of email and role fields
3. Avoid any pre-navigation permission errors

## Instructions

### Step 1: Access Invitation Endpoint

**Context**: Use UI or URL to reach the vulnerable form.

No specific command required; perform via browser UI:

- In the dashboard sidebar, click 'Users' > 'Add users'.
- Alternatively, enter the URL `https://shopify.plus/[id]/users/invite` in the address bar, replacing [id] with your shop's identifier.
- Press Enter to load the page.

> The page should display the form with an email input field, role dropdown, and 'Send invite' button. If permissions are insufficient, an error will appear.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- navigation
- shopify
