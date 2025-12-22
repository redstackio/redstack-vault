---
id: 87ebabd6-6a22-4764-9dd5-b774d26edb28
type: command
executor: bash
data: 'git clone https://github.com/cyberark/SkyArk'
output: null
created_at: '2023-04-06T03:56:08.936635+00:00'
updated_at: '2023-04-10T20:20:58.747935+00:00'
platforms:
  - Linux
  - macOS
tags:
  - cloud
  - aws
  - recon
verified: true
validated: true
---

# Clone SkyArk Repository

## Command

```bash
git clone https://github.com/cyberark/SkyArk
```

## Description

Clones the SkyArk repository from GitHub, which contains tools for discovering AWS shadow administrators.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | GitHub repository URL | Yes (built-in) |

## Examples

### Basic Usage

```bash
git clone https://github.com/cyberark/SkyArk
```

## Expected Output

Cloning into 'SkyArk'...
remote: Enumerating objects: X, done.
remote: Counting objects: 100% (X/X), done.
...
