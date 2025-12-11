---
tags:
  - gitlab
  - commit-injection
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/git]]'
  - '[[tools/ssh]]'
  - '[[tools/cat]]'
  - '[[tools/GitLab-Wiki]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-gitlab-search-wiki-blobs]]'
  - '[[commands/cat-file-contents]]'
  - '[[commands/ssh-gitlab-access]]'
  - '[[commands/id-user-check]]'
  - '[[commands/cat-authorized-keys]]'
  - '[[commands/curl-gitlab-search-blobs]]'
platforms:
  - GitLab
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 031ed8ed-63ac-46c0-bd5c-684fa230787d
created_at: '2025-12-11T06:10:29.992Z'
updated_at: '2025-12-11T06:10:29.992Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Create Wiki Page with Controlled Commit

## Summary

This procedure involves creating a new GitLab wiki page with a specific commit message to embed controlled content that can be used in subsequent file overwrite attacks via Git flag injection.

## Description

In GitLab, wiki pages are stored as Git repositories, and commit messages can be controlled by the user. This allows embedding arbitrary content (e.g., SSH keys) into the Git log, which can then be written to files through vulnerable API calls that execute unsanitized Git commands.

## Requirements

1. Access to a GitLab project with wiki enabled
2. Valid user credentials for wiki editing
3. GitLab instance vulnerable to flag injection

## Defense

Defensive measures and detection strategies:

- Sanitize API parameters to prevent flag injection
- Monitor API logs for suspicious ref parameters like --output

## Objectives

1. Embed controlled content in Git commit
2. Prepare for file overwrite exploitation
3. Enable content control in injected Git commands

## Instructions

### Step 1: Access GitLab Wiki

**Context**: Navigate to the project's wiki section.

Use the GitLab web interface to create a new page.

### Step 2: Create Page with Commit Message

**Context**: Set the page content and commit message.

Create a page named 'page' with any content, and set the commit message to 'controlled content' or the SSH public key.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/GitLab-Wiki]]

## Tags

- [[tools/GitLab-Wiki]]
- [[commit-injection]]
