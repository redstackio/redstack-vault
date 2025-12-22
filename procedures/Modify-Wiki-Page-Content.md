---
tags:
  - wiki
  - markdown
  - modification
type: procedure
tools:
  - '[[tools/Git]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/echo-append-to-wiki-file]]'
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
sub_techniques: []
id: 2174cde7-c755-4a27-b2cf-0f5e6cc47c57
created_at: '2025-12-13T23:52:55.061Z'
updated_at: '2025-12-13T23:52:55.061Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Modify Wiki Page Content

## Summary

This procedure alters a wiki page's Markdown file to create a commit opportunity, ensuring the malicious Git config email is associated with the change for XSS exploitation.

## Description

Wiki pages in GitLab are Markdown files in the repo. Any modification triggers a commit, pulling in the author email from Git config. This step uses minimal content changes to avoid suspicion while enabling payload persistence.

## Requirements

1. Local wiki repo cloned and navigated to
2. Malicious Git config already set
3. Target file like home.md existing or creatable

## Defense

Defensive measures and detection strategies:

- Review wiki commit history for trivial changes from suspicious authors
- Implement content scanning for wiki pushes
- Rate-limit wiki edits from untrusted sources

## Objectives

1. Trigger a commit with tainted metadata
2. Store the payload indirectly via Git history
3. Prepare for push to production wiki

## Instructions

### Step 1: Append Content to Wiki File

**Context**: Add simple text to a Markdown file to stage a change.

**Command** ([[commands/echo-append-to-wiki-file]]):
```bash
echo "Hi" >> home.md
```

> Appends 'Hi' to home.md. Expected output: File size increases; no errors if file exists.

### Step 2: Confirm Modification

**Context**: Verify the file has been updated.

**Command** (cat):
```bash
cat home.md
```

> Displays content including the new 'Hi' line, confirming readiness for commit.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/echo-append-to-wiki-file]]

## Tools Used

- [[tools/Git]]

## Tags

- [[wiki]]
- [[markdown]]
- [[modification]]
