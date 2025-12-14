---
id: proc-create-malicious-branch-ui
tags:
  - xss
  - branch-injection
  - gitlab
type: procedure
tools:
  - '[[tools/GDK-GitLab-Development-Kit]]'
  - '[[tools/Git-Client]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:20.777Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Branch-via-UI

## Summary

This procedure creates a Git branch with an XSS payload as its name using GitLab's web UI, bypassing client-side validations to store the malicious string for later use in merge requests.

## Description

Branch names in GitLab are not fully sanitized in the UI for creation, allowing HTML/JS like `<script>alert(1)</script>` to be set. This is done by creating a new file and specifying the branch name during commit. Targets local or remote GitLab instances; uses GDK for safe testing. Outcome: Malicious branch created, payload persists in repo metadata.

## Requirements

1. Forked GitLab repository under your control.
2. Access to the repo's web interface.
3. No special tools beyond browser; Git client as alternative.

## Defense

Defensive measures and detection strategies:

- Sanitize branch names server-side during creation.
- Flag branches with HTML tags in names via repo scans.
- Audit merge requests from forks for suspicious branch names.

## Objectives

1. Inject persistent XSS payload into branch metadata.
2. Store payload for rendering in unsanitized email templates.
3. Enable execution when branch name is displayed in notifications.

## Instructions

### Step 1: Initiate New File

**Context**: Start branch creation via file addition to leverage the branch name field.

Use GitLab UI:

- Click '+' > 'New File' on repo page, redirecting to `/new/master`.

> This opens the form where branch name can be set.

**Expected Output**: New file form with branch input.

### Step 2: Set Payload and Commit

**Context**: Enter the XSS payload as the branch name and commit.

- Add placeholder file content.
- Set target branch to `<script>alert(1)</script>`.
- Click 'Commit changes', ignore MR prompt if shown.

> UI accepts the payload; branch is created with JS in name.

**Expected Output**: Commit success, new branch listed.

### Step 3: Alternative via Git Client

**Context**: If UI blocks, use Git client to push malicious branch.

Execute [[git-push-malicious-branch]] (inferred command):

```bash
git checkout -b '<script>alert(1)</script>'
git commit --allow-empty -m "Malicious branch"
git push origin '<script>alert(1)</script>'
```

> Bypasses UI; pushes directly to remote.

**Expected Output**: Branch pushed successfully.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/git-push-malicious-branch]]

## Tools Used

- [[tools/Git-Client]]

## Tags

- xss
- git-branch
- injection
