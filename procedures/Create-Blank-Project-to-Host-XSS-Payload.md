---
id: proc-gitlab-create-blank-project-001
tags:
  - xss-trigger
  - project-creation
  - gitlab
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/git-config-user-name]]'
  - '[[commands/git-config-user-email]]'
  - '[[commands/git-clone]]'
  - '[[commands/cd-project-path]]'
  - '[[commands/git-switch-branch]]'
  - '[[commands/touch-readme]]'
  - '[[commands/git-add-readme]]'
  - '[[commands/git-commit-readme]]'
  - '[[commands/git-push-branch]]'
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:06.930Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Blank-Project-to-Host-XSS-Payload

## Summary

This procedure creates a new blank project within the malicious group, causing the injected default branch name to be rendered in the project's setup instructions, thereby triggering the stored XSS payload when the page loads.

## Description

Upon project creation without an initial repository, GitLab displays Git setup commands on the main project page, interpolating the group's default branch name directly into the code blocks using vulnerable HAML rendering (e.g., `#{default_branch_name}` without escaping). This executes the script in the context of any visitor's session, allowing arbitrary JS like token theft. The attack relies on the project's visibility to victims.

## Requirements

1. Group with injected XSS payload in default branch name.
2. Attacker permissions to create projects in the group.
3. Target GitLab version vulnerable to unsanitized display (pre-patch).

## Defense

Defensive measures and detection strategies:

- Escape branch names in all templates (e.g., use `h` helper in HAML).
- Avoid rendering user input in `pre` tags without sanitization.
- Scan for anomalous project creations in groups with suspicious settings.

## Objectives

1. Host the payload in a shareable project page.
2. Trigger automatic execution on page load.
3. Enable broad victim exposure via invites or links.

## Instructions

### Step 1: Initiate Blank Project Creation

**Context**: Select options to create a project that relies on the default branch, ensuring payload interpolation.

No command required; use the UI:

From https://gitlab.domain.com/groups/attack_group, click 'New project', select 'Create blank project', name it 'attacking_project', and create without importing or initializing a repo.

> Project is generated; main page at https://gitlab.domain.com/attack_group/attacking_project loads with setup instructions.

### Step 2: Verify XSS Trigger on Project Page

**Context**: Load the page to confirm the payload executes via displayed Git commands like `git switch -c <injected-script>`.

The vulnerable display includes commands such as:

Execute [[commands/git-config-user-name]] (displayed):

```bash
git config --global user.name "#{h git_user_name}"
```

> Alert(1) pops up; inspect page source to see unescaped `<script>` in branch name interpolation.

Follow with [[commands/git-switch-branch]]:

```bash
git switch -c #{default_branch_name}
```

> Script executes; successful if JS runs in browser context.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/git-config-user-name]]
- [[commands/git-switch-branch]]

## Tools Used


## Tags

- [[xss-trigger]]
- [[project-creation]]
