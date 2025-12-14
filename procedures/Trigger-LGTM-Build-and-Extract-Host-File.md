---
id: proc-lgtm-trigger-build-extract
tags:
  - build-trigger
  - extraction
  - lgtm
  - file-read
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Linux
  - Docker
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:29.955Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Trigger-LGTM-Build-and-Extract-Host-File

## Summary

This procedure initiates a build on the LGTM platform, allowing the symlink to resolve during file retention and exposing host file contents in the build output viewer.

## Description

Once the repository has both lgtm.yml and the .lgtm.yml symlink, triggering a build causes LGTM's worker container to preserve files without symlink restrictions, resolving to host paths like /etc/passwd. Viewable in the LGTM file list post-build. Target is the LGTM dashboard; prerequisites are the prepared repo. Expected outcome: Arbitrary host file read via web interface.

## Requirements

1. GitHub repo with LGTM integration enabled
2. Access to LGTM dashboard
3. Patience for build completion (minutes)

## Defense

Defensive measures and detection strategies:

- Restrict symlink following in container builds to container fs only
- Log and alert on resolved paths outside expected directories
- Post-build artifact scanning for sensitive data leaks

## Objectives

1. Complete the escape by resolving symlink
2. Disclose host sensitive information
3. Enable further exploration

## Instructions

### Step 1: Enable LGTM Analysis

**Context**: Integrate the repository with LGTM to queue a build.

In GitHub repo settings, add LGTM app or visit LGTM.com, search for the repo, and enable analysis.

> Triggers initial scan and build.

### Step 2: Monitor Build

**Context**: Wait for successful completion.

Check LGTM dashboard for build status; ensure it succeeds without errors from the config.

> Build time varies; success indicated by green status.

### Step 3: View File List

**Context**: Access retained files to see resolved symlink content.

In the LGTM project view, navigate to the build artifacts or file list, locate .lgtm.yml, and open it to reveal host file contents like /etc/passwd entries.

> Confirms escape if external data appears.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery
- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[build-trigger]]
- [[extraction]]
- [[lgtm]]
- [[file-read]]
