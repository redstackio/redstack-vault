---
id: proc-gitlab-invite-victim-xss-001
tags:
  - victim-invite
  - token-theft
  - xss-execution
  - gitlab
type: procedure
tools:
  - '[[tools/Python]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/python-invite-api]]'
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Credentials In Files]]'
updated_at: '2025-12-13T23:55:06.928Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Credentials In Files]]'
---
# Invite-Victim-and-Trigger-XSS-Execution

## Summary

This procedure invites a target user to the malicious project, prompting them to visit the page where the stored XSS payload executes in their browser session, allowing theft of sensitive data like personal access tokens.

## Description

By granting the victim Developer access, the attacker ensures they can view the project page, which loads the vulnerable setup instructions. The XSS executes in the victim's context, enabling actions such as accessing localStorage for GitLab tokens or sending them to an attacker server. For scalability, use Python scripting via the GitLab API to batch-invite multiple victims.

## Requirements

1. Malicious project created with active XSS payload.
2. Victim account details (username/email).
3. Optional: Personal access token for API invites (Maintainer role).

## Defense

Defensive measures and detection strategies:

- Educate users on suspicious project invites and verify senders.
- Monitor for unusual member additions via API or UI logs.
- Deploy browser extensions or policies to block XSS (e.g., strict CSP enforcement).

## Objectives

1. Expose victim to the payload via legitimate access.
2. Collect session data or tokens upon execution.
3. Achieve account takeover using stolen credentials.

## Instructions

### Step 1: Manual Invite via UI

**Context**: Add the victim as a member to gain access to the project page.

No command required; use the UI:

On the project page https://gitlab.domain.com/attack_group/attacking_project, click 'Invite members', enter 'victim01', select Developer role, and send invite.

> Invite sent; victim receives notification and can accept.

### Step 2: Scripted Batch Invites (Optional)

**Context**: Automate invites for multiple targets using GitLab API with Python.

Execute [[commands/python-invite-api]]:

```bash
python invite.py --project-id 123 --user victim01 --token glpat-xxx --role developer
```

> Script adds members via /api/v4/projects/:ID/members; check API response for success (201 Created).

### Step 3: Victim Visit and Execution

**Context**: Direct victim to load the page, triggering XSS in displayed commands.

Have victim log in and visit https://gitlab.domain.com/attack_group/attacking_project.

> Payload executes (e.g., alert or exfil); attacker monitors for stolen data.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript
- [[Credentials In Files]] Credentials from Web Browsers

### Sub-Techniques


## Commands Used

- [[commands/python-invite-api]]

## Tools Used

- [[tools/Python]]

## Tags

- [[victim-invite]]
- [[token-theft]]
