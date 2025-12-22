---
id: 113a2d60-b083-4790-bec3-666033ca2d81
name: git-clone-dotdotpwn-repository
type: command
executor: bash
data: 'git clone https://github.com/wireghoul/dotdotpwn'
output: null
created_at: '2023-04-06T03:55:57.747865+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - installation
  - git
verified: true
validated: true
---

# git-clone-dotdotpwn-repository

## Command

```bash
git clone https://github.com/wireghoul/dotdotpwn
```

## Description

This command clones the Dotdotpwn repository from GitHub, downloading the Perl script and supporting files needed for directory traversal fuzzing. Use this as the first step to install the tool on a Linux-based attack machine.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://github.com/wireghoul/dotdotpwn | Repository URL for Dotdotpwn | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/wireghoul/dotdotpwn
```

### Advanced Usage

Run in a specific directory:

```bash
git clone https://github.com/wireghoul/dotdotpwn /path/to/install
```

## Expected Output

Cloning into 'dotdotpwn'...
remote: Enumerating objects: 50, done.
remote: Total 50 (delta 0), reused 0 (delta 0), pack-reused 50
Receiving objects: 100% (50/50), done.

## Related

- [[procedures/Directory-Traversal-using-Dotdotpwn]]
- [[tools/dotdotpwn]]
