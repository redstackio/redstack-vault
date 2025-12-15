---
id: p-extract-token-export
name: Extract-Token-from-Export-Archive
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.236Z'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Credentials In Files]]'
  - '[[File and Directory Discovery]]'
tags:
  - gitlab
  - token-extraction
  - tar
commands:
  - '[[commands/list-recent-downloads]]'
  - '[[commands/tar-extract-export]]'
  - '[[commands/tar-list-contents]]'
platforms:
  - Linux
  - Web
tools:
  - '[[tools/tar]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
  - '[[File and Directory Discovery]]'
---

# Extract-Token-from-Export-Archive

## Summary

This procedure unpacks the downloaded GitLab project export .tar.gz archive and inspects the project.json file to retrieve the target's authentication_token from the unredacted project_members array.

## Description

After downloading the export, the attacker extracts the archive using tar and examines the serialized JSON, where user objects include sensitive fields like authentication_token due to lack of redaction. This directly exploits the information disclosure vulnerability. Prerequisites: downloaded .tar.gz file. Expected outcomes: token extracted for use in privilege escalation.

## Requirements

1. Downloaded export .tar.gz in local Downloads folder
2. Bash shell access on Linux/macOS
3. tar utility installed

## Defense

Defensive measures and detection strategies:

- Filter sensitive data (tokens, hashes) before JSON serialization in exports
- Encrypt or obfuscate export archives
- Audit downloaded exports for anomalous access patterns

## Objectives

1. Unpack archive to access project.json
2. Locate and copy authentication_token
3. Prepare for credential use

## Instructions

### Step 1: Locate Recent Download

**Context**: Identify the newest export file in Downloads.

**Command** ([[commands/list-recent-downloads]]):
```bash
ls -t ~/Downloads/ | head -1
```

> Lists the most recent file, e.g., 2016-08-12_09-34-826_gitlab-org_gitlab-test_export.tar.gz.

### Step 2: Extract Archive

**Context**: Unpack to a temporary directory for inspection.

**Command** ([[commands/tar-extract-export]]):
```bash
tar -xzf ~/Downloads/2016-08-12_09-34-826_gitlab-org_gitlab-test_export.tar.gz -C /tmp/export
```

> Extracts files like project.json to /tmp/export; verify with ls /tmp/export.

### Step 3: Inspect JSON for Token

**Context**: Examine project_members in project.json.

**Command** ([[commands/tar-list-contents]]):
```bash
tar -ztvf export.tar.gz
```
(Or directly cat /tmp/export/project.json | grep authentication_token)

> Reveals user objects; copy the token value from the array.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Credentials In Files]] Credentials In Files
- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/list-recent-downloads]]
- [[commands/tar-extract-export]]
- [[commands/tar-list-contents]]

## Tools Used

- [[tools/tar]]

## Tags

- [[gitlab]]
- [[token-extraction]]
- [[tools/tar]]
