---
id: uuid-5
tags:
  - gitlab
  - project-limit
  - alternative
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-gitlab-list-projects-private-token]]'
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:30:27.312Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Enable-Project-Creation-for-External-User

## Summary

Modifies external user settings to allow project creation, enabling independent token generation as an alternative to invitation-based escalation.

## Description

By setting project limit >0, the external user can create a personal project and generate a token there, which still escalates to internal access. This bypasses the need for project invitation. Expected outcome: External user creates project and exploits token similarly.

## Requirements

1. Admin access to user settings
2. External user account
3. GitLab with personal project creation enabled for limits

## Defense

Defensive measures and detection strategies:

- Default external users to 0 project limit
- Audit admin changes to user limits
- Prevent token creation on personal projects for external users

## Objectives

1. Grant project creation to external user
2. Allow self-contained token generation
3. Validate escalation without team involvement

## Instructions

### Step 1: Update User Limits

**Context**: As admin, increase project allowance.

Navigate to `/admin/users/<username>/edit` and set Projects Limit to 1 or more, then save.

> Limit updated; external user now has creation quota.

### Step 2: Create Personal Project

**Context**: As external user, create a blank project.

Go to `/projects/new#blank_project`, enter details, and create.

> Project dashboard accessible.

### Step 3: Generate Token and Test

**Context**: Create token on new project and test internal access.

Follow token generation, then use [[commands/curl-gitlab-list-projects-private-token]] with PRIVATE-TOKEN header:

```bash
curl --header "PRIVATE-TOKEN: <TOKEN>" "https://gitlab.domain.com/api/v4/projects?visibility=internal"
```

> JSON of internal projects, confirming escalation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[External Remote Services]] External Remote Services

### Sub-Techniques


## Commands Used

- [[commands/curl-gitlab-list-projects-private-token]]

## Tools Used

- [[tools/curl]]

## Tags

- gitlab
- project-creation
- external-limit
