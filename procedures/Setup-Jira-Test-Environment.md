---
id: proc-uuid-001
tags:
  - jira-setup
  - environment-prep
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/jira-check-project-permissions]]'
  - '[[commands/jira-check-site-permissions]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:58.170Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-Jira-Test-Environment

## Summary

This procedure sets up a Jira Cloud instance with basic and admin users, restricted private projects, and installs the HackerOne integration app to prepare for exploiting access control flaws.

## Description

In a real attack, the target Jira instance already exists, but for testing, create a new one via Atlassian. Add a basic user, create 8 projects with 5 restricted to admins, and install the app. This simulates the environment where basic users can access sensitive config without checks, leading to JWT leakage and escalation.

## Requirements

1. Atlassian account with ability to create Jira Cloud instances
2. Access to HackerOne account for later claiming
3. Basic knowledge of Jira permissions and Atlassian Marketplace

## Defense

Defensive measures and detection strategies:

- Enforce strict role-based access control (RBAC) in Jira
- Monitor app installations and user permission changes via Atlassian audit logs
- Use JWT validation with user-specific claims on the HackerOne side

## Objectives

1. Establish a testable Jira environment with privilege disparities
2. Install vulnerable integration without triggering alerts
3. Verify basic user's limited access via API checks

## Instructions

### Step 1: Create Jira Cloud Instance

**Context**: Set up a new instance to control the environment.

**Command** ([[commands/jira-create-instance]]):
No direct command; use Atlassian web interface to sign up at https://www.atlassian.com/software/jira.

> Navigate to Atlassian Cloud signup, create a new Jira site, and log in as admin.

### Step 2: Add Basic User and Configure Projects

**Context**: Invite a low-privilege user and restrict projects to isolate the attack surface.

**Command** (Manual via UI):
Use Jira admin panel to invite user@domain.com with Basic license, then create 8 projects, setting permissions for 5 to admin-only.

> Expected: Basic user can view public projects but not administer or access privates.

### Step 3: Install HackerOne App

**Context**: Deploy the vulnerable plugin from Marketplace.

**Command** (Manual):
Go to https://marketplace.atlassian.com/apps/1214355/hackerone-for-jira-cloud, install, and enable.

> Expected: App installed without errors.

### Step 4: Verify Permissions

**Context**: Confirm basic user's limitations using API.

**Command** ([[commands/jira-check-project-permissions]]):
```bash
curl -u basic-user:password -X GET "https://your-jira.atlassian.net/rest/api/3/mypermissions?permissions=ADMINISTER_PROJECTS"
```

> JSON response: {"permissions": [{"id": "ADMINISTER_PROJECTS", "havePermission": false}]}. Repeat with [[commands/jira-check-site-permissions]] for site-wide checks.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

- [[commands/jira-check-project-permissions]]
- [[commands/jira-check-site-permissions]]

## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- jira-setup
- environment-prep
