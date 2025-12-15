---
id: proc-uuid-002
name: Extract-Credentials-from-Exposed-File
tags:
  - credential-access
  - github
  - aws
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:32:29.060Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques:
  - '[[Credentials In Files]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Extract-Credentials-from-Exposed-File

## Summary

This procedure details viewing and extracting plain-text AWS Access Key and Secret Key from a specific file in a public GitHub repository, enabling subsequent unauthorized access.

## Description

Attackers open the exposed file (e.g., a config or script) in the repository and locate the credentials embedded in the content without protection. The target is GitHub's file viewer, with outcomes including copied keys ready for use in AWS authentication. This exploits poor secret management in version control.

## Requirements

1. Access to the public repository from Step 1
2. Ability to view file contents in browser
3. Text editor or screenshot tool for documentation

## Defense

Defensive measures and detection strategies:

- Encrypt or use environment variables for credentials in code
- Employ tools like git-secrets to prevent commits of sensitive data
- Monitor for exposure via services like GitHub Advanced Security

## Objectives

1. View the file containing credentials
2. Identify and copy the Access Key and Secret Key
3. Validate keys appear unredacted

## Instructions

### Step 1: Open the Exposed File

**Context**: Navigate to the specific file path within the repository to view its contents.

Use browser to click on the file link (e.g., /repo/blob/main/config.py).

> Displays raw file content. Expected output: File loads with plain text visible.

### Step 2: Locate and Copy Credentials

**Context**: Scan the file, typically mid-content, for AWS keys (Access Key: AKIA..., Secret Key: ...).

Select and copy the key strings; take a screenshot for evidence.

> Extracts usable credentials. Expected output: Keys copied to clipboard or notes.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Unsecured Credentials]] Unprotected Storage of Credentials

### Sub-Techniques

- [[Credentials In Files]] Credentials In Files

## Commands Used


## Tools Used


## Tags

- [[credential-access]]
- [[github]]
- [[aws]]
