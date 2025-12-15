---
id: proc-clone-wiki-repo
tags:
  - git
  - clone
type: procedure
tools:
  - '[[tools/git]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/git-clone-wiki]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:23:50.171Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Clone-Project-Wiki-Repository

## Summary

This procedure clones the GitLab project wiki repository locally, allowing editing and pushing of malicious content to trigger RCE during rendering.

## Description

GitLab wikis are git repositories ending in .wiki.git, separate from the main project repo. Cloning requires authentication via HTTPS with personal access token or SSH key. This enables local modification of wiki pages in MediaWiki format, which will be rendered server-side using the vulnerable WikiCloth Lua extension. Prerequisites: Wiki-enabled project; outcomes: Local repo ready for payload addition.

## Requirements

1. Git installed locally
2. GitLab credentials (token or SSH) for authenticated clone
3. Wiki URL from project page (e.g., https://gitlab.com/group/project.wiki.git)

## Defense

Defensive measures and detection strategies:

- Monitor git clone/push events in GitLab logs for wiki repos
- Enforce 2FA and limit clone access
- Use webhooks to alert on wiki changes

## Objectives

1. Obtain local copy of wiki for payload editing
2. Maintain authenticated access for pushes
3. Avoid direct server edits

## Instructions

### Step 1: Clone Wiki Repo

**Context**: Use git to fetch the remote wiki repository.

**Command** ([[commands/git-clone-wiki]]):
```bash
git clone <wiki-url>.wiki.git
```

> Replaces <wiki-url> with actual project wiki URL. Expected output: Progress bars and 'Cloning into 'wiki'' directory created.

### Step 2: Verify Clone

**Context**: Confirm the repo is cloned and authenticated.

**Command** (Git UI):
```bash
git log
```

> Shows commit history. Expected output: Initial commits or empty log for new wiki.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/git-clone-wiki]]

## Tools Used

- [[tools/git]]

## Tags

- git
- clone
