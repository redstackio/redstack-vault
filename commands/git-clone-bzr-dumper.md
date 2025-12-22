---
id: 152c8705-a5ce-4e9a-9d08-5f54c725eea4
name: git-clone-bzr-dumper
type: command
executor: bash
data: 'git clone https://github.com/SeahunOh/bzr_dumper'
output: null
created_at: '2023-04-06T03:56:00.354612+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - git
  - clone
  - tool-download
verified: true
validated: true
---

# git-clone-bzr-dumper

## Command

```bash
git clone https://github.com/SeahunOh/bzr_dumper
```

## Description

This command clones the bzr_dumper tool repository from GitHub to the local machine, downloading the Python script needed to dump insecure Bazaar repositories.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://github.com/SeahunOh/bzr_dumper | The GitHub URL of the bzr_dumper repository | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/SeahunOh/bzr_dumper
```

### Advanced Usage

To clone into a specific directory:

```bash
git clone https://github.com/SeahunOh/bzr_dumper /path/to/target/dir
```

## Expected Output

Cloning into 'bzr_dumper'...
remote: Enumerating objects: X, done.
remote: Counting objects: 100% (X/X), done.
remote: Compressing objects: 100% (X/X), done.
Receiving objects: 100% (X/X), X KiB | X KiB/s, done.

## Related

- [[procedures/Extract-Source-Code-from-Insecure-Bazaar-Repository]]
