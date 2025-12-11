---
id: 242032c2-1e0a-49de-a5c4-93fb1e10f6e9
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:48:05.918Z'
updated_at: '2025-12-11T03:48:05.918Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - gitlab
  - setup
commands: []
platforms:
  - Web
tools:
  - '[[tools/Flask]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---

# Setup Initial GitLab Group and Extract Upload Secret

## Summary

This procedure sets up an initial GitLab group and extracts the upload secret hash by uploading a dummy file to a milestone, which is necessary for crafting the malicious symlink path in subsequent steps.

## Description

In this procedure, a new group is created on gitlab.com using the web interface. A milestone is then added with a dummy file upload to generate a unique upload path containing a 32-byte secret hash. This hash is noted for use in creating the directory structure for symlinks. The target environment is a GitLab instance, and the expected outcome is obtaining the hash without alerting the system.

## Requirements

1. Access to GitLab account with group creation permissions
2. Web browser for GitLab interface
3. No special tools required

## Defense

Defensive measures and detection strategies:

- Monitor for unusual group creations and imports
- Implement rate limiting on bulk imports

## Objectives

1. Create source group for import
2. Generate and extract upload secret hash
3. Prepare for malicious payload creation

## Instructions

### Step 1: Create New Group

**Context**: Use GitLab web interface to create a group for initial setup.

Navigate to GitLab and create a new group.

> Group created successfully.

### Step 2: Create Milestone and Upload File

**Context**: Upload a dummy file to generate an upload path with a secret hash.

Create a new milestone in the group and upload a file named 'passwd' with any content into the description.

> File uploaded and path generated.

### Step 3: Note Upload Secret

**Context**: Extract the hash from the upload URL for use in symlink creation.

Inspect the upload URL and note the 32-byte hash.

> Hash extracted.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #gitlab
- #setup
