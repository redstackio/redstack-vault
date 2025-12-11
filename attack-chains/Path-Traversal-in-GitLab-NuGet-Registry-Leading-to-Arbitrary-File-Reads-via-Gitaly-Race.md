---
tags:
  - gitlab
  - path-traversal
  - race-condition
  - arbitrary-file-read
type: attack_chain
tools:
  - '[[tools/Nokogiri]]'
  - '[[tools/Faraday]]'
  - '[[tools/exp.rb]]'
tactics:
  - '[[Execution]]'
  - '[[Discovery]]'
commands: []
platforms:
  - Linux
complexity: medium
procedures:
  - '[[procedures/Craft-Malicious-NuSpec-for-Path-Traversal]]'
  - '[[procedures/Package-NuSpec-into-NuPkg]]'
  - '[[procedures/Upload-Malicious-NuPkg-via-GitLab-API]]'
  - '[[procedures/Exploit-Gitaly-Race-for-Arbitrary-File-Read]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
description: >-
  Exploits a path traversal vulnerability in GitLab's NuGet Package Registry
  combined with a Gitaly race condition to achieve arbitrary file reads on the
  GitLab instance.
skill_level: intermediate
impact_level: high
id: 276a87dc-7699-4d0d-a97d-d135137e0cc5
created_at: '2025-12-11T03:47:39.837Z'
updated_at: '2025-12-11T03:47:39.837Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1083]]'
---
# Path Traversal in GitLab NuGet Registry Leading to Arbitrary File Reads via Gitaly Race

Multi-stage attack chain demonstrating a complete attack workflow exploiting a path traversal vulnerability in GitLab's NuGet Package Registry by injecting traversal sequences into the version field of a .nuspec XML file, allowing arbitrary file creation, and combining it with a known Gitaly race condition to enable arbitrary file reads, such as accessing sensitive files like .gitlab_shell_secret.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via API] --> B[Path Traversal Exploitation]
    B --> C[File Creation]
    C --> D[Arbitrary File Read via Race]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- #zip
- [[tools/Faraday]]
- #rubyzip
- [[tools/exp.rb]]

### Target Environment

- Linux
- GitLab 12.8.7-ee with Gitaly and GitLab Shell 11.0.0
- Required services/ports: GitLab API endpoint accessible

### Initial Access Requirements

- Credential requirements: Valid GitLab project ID and API access token
- Network position: External access to GitLab instance
- Prior access needed: Ability to upload packages to a project

## Detailed Attack Procedures

### Step 1: Craft Malicious NuSpec - [[procedures/Craft-Malicious-NuSpec-for-Path-Traversal]]

**Procedure**: [[procedures/Craft-Malicious-NuSpec-for-Path-Traversal]]

**Objective**: Create a .nuspec XML file with path traversal sequences in the version field to enable arbitrary path file creation.

**Expected Output**: A dummy.nuspec file with traversal like '../../../../../nyangawa' in the version field.

**Success Indicators**:
- XML file is valid and contains the traversal sequence
- No parsing errors when viewed

### Step 2: Package into NuPkg - [[procedures/Package-NuSpec-into-NuPkg]]

**Procedure**: [[procedures/Package-NuSpec-into-NuPkg]]

**Objective**: Compress the malicious .nuspec into a .nupkg file for upload.

Use #zip to create the package:

```bash
zip dummy.nupkg dummy.nuspec
```

**Expected Output**: A valid dummy.nupkg file ready for upload.

**Success Indicators**:
- Zip file created without errors
- File can be extracted to verify contents

### Step 3: Upload via API - [[procedures/Upload-Malicious-NuPkg-via-GitLab-API]]

**Procedure**: [[procedures/Upload-Malicious-NuPkg-via-GitLab-API]]

**Objective**: Upload the malicious .nupkg to trigger the path traversal during metadata extraction.

Use the GitLab API endpoint PUT /api/v4/projects/#{id}/packages/nuget/ to upload the package, which triggers extraction using [[tools/Nokogiri]] and creates files with traversed paths.

**Expected Output**: Successful upload and file creation on the server filesystem as the git user.

**Success Indicators**:
- HTTP 200 response from API
- Evidence of file creation in logs or subsequent steps

### Step 4: Exploit Gitaly Race - [[procedures/Exploit-Gitaly-Race-for-Arbitrary-File-Read]]

**Procedure**: [[procedures/Exploit-Gitaly-Race-for-Arbitrary-File-Read]]

**Objective**: Combine the path traversal with the Gitaly race condition to read arbitrary files.

First, install dependencies using [[commands/gem-install-faraday]]:

```bash
gem install faraday
```

And [[commands/gem-install-rubyzip]]:

```bash
gem install rubyzip
```

Then run the exploit script [[tools/exp.rb]] (edit to update URL and credentials) to read files like .gitlab_shell_secret.

**Expected Output**: Contents of the target file displayed or exfiltrated.

**Success Indicators**:
- Script executes without errors
- Sensitive file contents retrieved

## Attack Chain Summary

### Key Achievements

1. Arbitrary file creation via path traversal in NuGet registry
2. Exploitation of Gitaly race for file reads
3. Access to sensitive files like .gitlab_shell_secret

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Discovery]]

*Last updated: 2023-10-01*
