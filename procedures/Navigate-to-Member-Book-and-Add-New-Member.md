---
id: 123e4567-e89b-12d3-a456-426614174002
name: Navigate-to-Member-Book-and-Add-New-Member
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:26.700Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - navigation
  - web
  - xss
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Navigate-to-Member-Book-and-Add-New-Member

## Summary

This procedure navigates an authenticated user to the Member Book feature in the Veris portal and initiates the addition of a new member, positioning for payload injection in vulnerable fields.

## Description

Following authentication, the attacker must reach the specific endpoint vulnerable to stored XSS: the add member form at https://sandbox.veris.in/portal/members/. This involves clicking through the UI to the members section and selecting 'Add new member'. The form includes unsanitized Name and Description fields where payloads can be stored. Expected outcome is the form loading without errors, allowing input submission to the backend.

## Requirements

1. Active authenticated session in Veris portal
2. Web browser capable of handling session cookies
3. Access to the members management UI

## Defense

Defensive measures and detection strategies:

- Restrict access to admin features with role-based access control (RBAC)
- Log navigation patterns to sensitive areas for anomaly detection
- Employ client-side controls to validate UI interactions

## Objectives

1. Locate and access the vulnerable add member form
2. Prepare input fields for malicious payload entry
3. Store data in the backend without immediate execution

## Instructions

### Step 1: Access Members Section

**Context**: From the dashboard, reach the Member Book area.

Click on the 'Members' or 'Member Book' link in the portal navigation menu, directing to https://sandbox.veris.in/portal/members/.

> The members list page should load, displaying existing members.

### Step 2: Initiate Add Member

**Context**: Open the form for creating a new entry.

Select the 'Add new member' button or option on the members page.

> A form modal or new page opens with fields including Name and Description.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[navigation]]
- [[web]]
- [[xss]]
