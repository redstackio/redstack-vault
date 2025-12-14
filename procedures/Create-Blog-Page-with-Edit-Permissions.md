---
id: proc-uuid-001
tags:
  - setup
  - permissions
  - concrete-cms
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:03.326Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-Blog-Page-with-Edit-Permissions

## Summary

This procedure sets up a blog page in Concrete CMS with edit permissions granted to a non-admin user, enabling subsequent injection of malicious content for CSRF exploitation.

## Description

In Concrete CMS, administrators can create pages and assign permissions. This step abuses legitimate CMS functionality to create a vector for payload injection. The target environment is a Concrete CMS instance where the attacker has admin access initially but aims to escalate via non-admin. Expected outcome: A page editable by the victim user, leading to privilege escalation when admins visit.

## Requirements

1. Admin login credentials to Concrete CMS dashboard
2. Access to Pages and Permissions sections
3. Target non-admin user account identified (e.g., uID 8)

## Defense

Defensive measures and detection strategies:

- Enforce principle of least privilege: Limit non-admin edit access to sensitive pages
- Monitor permission changes via CMS audit logs
- Use role-based access control (RBAC) to restrict page creation

## Objectives

1. Create a modifiable page for payload hosting
2. Grant edit access without alerting admins
3. Prepare for CSRF payload injection

## Instructions

### Step 1: Log In and Navigate to Pages

**Context**: Access the admin dashboard to initiate page creation.

**Command** (Browser Navigation):

No CLI command; use web interface: Log in at `/dashboard` and go to Pages > Add Page > Blog.

> Fills out page details (title, etc.) and saves the new blog page.

### Step 2: Modify Page Permissions

**Context**: Assign edit rights to the non-admin user to allow payload injection.

**Command** (UI Action):

In Page Settings > Permissions, add the non-admin user (uID 8) with 'Edit Page' and 'Approve Changes' permissions.

> Permissions updated; non-admin can now edit without full access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[setup]]
- [[permissions]]
- [[concrete-cms]]
