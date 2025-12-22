---
type: command
executor: bash
data: 'git clone https://github.com/its-a-feature/KeytabParser'
output: null
tags:
  - kerberos
  - keytab
platforms:
  - Linux
  - macOS
verified: true
validated: true
---

# git-clone-keytabparser

## Command

```bash
git clone https://github.com/its-a-feature/KeytabParser
```

## Description

This command clones the KeytabParser repository from GitHub, providing a Python script to parse and analyze Kerberos keytab files for credential extraction in Active Directory attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL (fixed) | Repository URL for KeytabParser | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/its-a-feature/KeytabParser
```

> Clones the repo into a local 'KeytabParser' directory.

## Expected Output

Cloning into 'KeytabParser'...
remote: Enumerating objects: 50, done.
remote: Counting objects: 100% (50/50), done.
remote: Compressing objects: 100% (30/30), done.
Receiving objects: 100% (50/50), 20.00 KiB | 20.00 MiB/s, done.

## Related

- [[procedures/Extract-and-Reuse-Kerberos-Tickets-from-Keytab]]
