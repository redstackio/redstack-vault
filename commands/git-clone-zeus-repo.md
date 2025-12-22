---
id: da3429a1-edb8-4a8b-a470-d76eb1c2a93a-clone
name: git-clone-zeus-repo
type: command
executor: bash
data: 'git clone https://github.com/DenizParlak/Zeus.git'
output: null
created_at: '2023-04-06T03:56:09.860235+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - cloud
  - aws
  - setup
verified: true
validated: true
---

# git-clone-zeus-repo

## Command

```bash
git clone https://github.com/DenizParlak/Zeus.git
```

## Description

This command clones the Zeus AWS Auditing & Hardening Tool repository from GitHub, downloading all necessary scripts for S3 bucket scanning and other AWS audits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://github.com/DenizParlak/Zeus.git | Repository URL | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/DenizParlak/Zeus.git
```

### With Specific Directory

```bash
git clone https://github.com/DenizParlak/Zeus.git aws-auditor
```

## Expected Output

Cloning into 'Zeus'...
remote: Enumerating objects: 50, done.
remote: Counting objects: 100% (50/50), done.
remote: Compressing objects: 100% (30/30), done.
Receiving objects: 100% (100/100), 20.00 KiB | 1.00 MiB/s, done.
Resolving deltas: 100% (50/50), done.

## Related

- [[procedures/Scan-AWS-S3-Buckets-for-Misconfigurations]]
- [[tools/Zeus-AWS-Auditor]]
