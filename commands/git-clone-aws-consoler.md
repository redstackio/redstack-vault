---
id: c521b387-cf94-407d-a8e5-4c920b74ba52
name: git-clone-aws-consoler
type: command
executor: bash
data: 'git clone https://github.com/NetSPI/aws_consoler'
output: null
created_at: '2023-04-06T03:56:09.462520+00:00'
updated_at: '2023-04-10T20:20:55.849911+00:00'
platforms:
  - Linux
  - macOS
  - Windows (with Git Bash)
tags:
  - git
  - clone
  - aws
verified: true
validated: true
---

# git-clone-aws-consoler

## Command

```bash
git clone https://github.com/NetSPI/aws_consoler
```

## Description

This command clones the aws_consoler repository from GitHub, downloading the tool used to convert AWS API keys into console access URLs. Use this as the first step in setting up the aws_consoler utility for AWS credential exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://github.com/NetSPI/aws_consoler | The repository URL to clone | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/NetSPI/aws_consoler
```

### With Specific Directory

```bash
git clone https://github.com/NetSPI/aws_consoler ./tools/aws-consoler
```

## Expected Output

Cloning into 'aws_consoler'...
remote: Enumerating objects: 50, done.
remote: Counting objects: 100% (50/50), done.
remote: Compressing objects: 100% (30/30), done.
remote: Total 100 (delta 20), reused 50 (delta 10)
Receiving objects: 100% (100/100), 25.00 KiB | 1.00 MiB/s, done.
Resolving deltas: 100% (20/20), done.

The repository is now available locally in the 'aws_consoler' directory.

## Related

- [[procedures/AWS-Console-Access-via-API-Keys]]
- [[commands/run-aws-consoler-with-api-keys]]
