---
id: 2f3bcfa4-4c2e-48d6-b501-1f48f8e899e3
name: git-clone-svn-extractor
type: command
executor: bash
data: 'git clone https://github.com/anantshri/svn-extractor.git'
output: null
created_at: '2023-04-06T03:56:00.290018+00:00'
updated_at: '2023-04-10T20:33:57.619782+00:00'
platforms:
  - Linux
tags:
  - git
  - clone
  - tool-acquisition
verified: true
validated: true
---

# git-clone-svn-extractor

## Command

```bash
git clone https://github.com/anantshri/svn-extractor.git
```

## Description

This command clones the svn-extractor tool repository from GitHub to your local machine, downloading the Python script used for extracting contents from insecure SVN repositories.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://github.com/anantshri/svn-extractor.git | The GitHub repository URL for svn-extractor | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/anantshri/svn-extractor.git
```

### Advanced Usage

To clone into a specific directory:

```bash
git clone https://github.com/anantshri/svn-extractor.git /path/to/target/dir
```

## Expected Output

Cloning into 'svn-extractor'...
remote: Enumerating objects: 50, done.
remote: Counting objects: 100% (50/50), done.
remote: Compressing objects: 100% (30/30), done.
Receiving objects: 100% (50/50), 20.00 KiB | 20.00 MiB/s, done.

A new directory 'svn-extractor' is created with the tool files.

## Related

- [[procedures/Extract-Source-Code-from-Insecure-Subversion-Repository]]
- [[tools/svn-extractor]]
