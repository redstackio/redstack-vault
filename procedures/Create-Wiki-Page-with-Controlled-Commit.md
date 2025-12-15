---
id: proc-uuid-1
tags:
  - gitlab
  - wiki
  - commit
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:15.349Z'
skill_level: basic
impact_level: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Wiki-Page-with-Controlled-Commit

## Summary

This procedure creates a new wiki page in a GitLab project with a specifically crafted commit message, which serves as the controlled payload for subsequent command injection exploits in the Search API.

## Description

In the context of exploiting GitLab's Search API vulnerability, a wiki page is created to log a commit with attacker-controlled content. This content will be output by git log during the injection, allowing overwrites with predictable data. The target environment is a GitLab instance with wiki enabled on the project. Prerequisites include a valid API token and project access.

## Requirements

1. Valid GitLab personal access token ($TOKEN)
2. Project ID with wiki feature enabled
3. Network access to GitLab API endpoint

## Defense

Defensive measures and detection strategies:

- Restrict wiki edit permissions to trusted users
- Monitor API calls for unusual commit patterns
- Enable logging of git operations in Gitaly

## Objectives

1. Establish a predictable payload source via commit message
2. Prepare for file overwrite exploitation
3. Verify commit logging works as expected

## Instructions

### Step 1: Create the Wiki Page

**Context**: Use GitLab's wiki creation endpoint or UI to add a page, ensuring the commit message contains the desired payload.

**Command** (via API with [[tools/curl]]):
```bash
curl --request POST --header "PRIVATE-TOKEN: $TOKEN" --header "Content-Type: text/markdown" --data "# Test Page" 'http://gitlab-vm.local/api/v4/projects/5/wikis/pages?page=page.md'
```

> This creates 'page.md' with a simple markdown body. The commit message is set to 'controlled content' via UI or extended API params if needed. Expected output: 201 Created response with page details.

### Step 2: Verify Commit

**Context**: Confirm the commit message is logged correctly for later exploitation.

**Command** (local git clone and log):
```bash
git clone http://gitlab-vm.local/administrator/testing.wiki.git
cd testing.wiki
git log --max-count=1
```

> Outputs the latest commit with the controlled message. Success confirms payload availability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]
- [[tools/git]]

## Tags

- gitlab
- wiki
- commit
