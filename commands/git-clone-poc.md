---
id: cmd-uuid-1
data: 'git clone https://github.com/l00ph0le/CVE-2019-0604.git'
tags:
  - poc
  - clone
type: command
output: null
executor: bash
platforms:
  - Windows
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.042Z'
verified: false
validated: true
submitted: true
---
# git-clone-poc

## Command

```bash
git clone https://github.com/l00ph0le/CVE-2019-0604.git
```

## Description

Clones the GitHub repository containing the PoC for CVE-2019-0604, including the XAML template and encoder source, to prepare for SharePoint RCE exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Repository URL | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/l00ph0le/CVE-2019-0604.git
```

### Advanced Usage

```bash
git clone https://github.com/l00ph0le/CVE-2019-0604.git CVE-2019-0604-PoC
```

## Expected Output

Cloning into 'CVE-2019-0604'... remote: Enumerating objects... Receiving objects: 100% (X/X), done. Directory populated with PoC files.

## Related

- [[procedures/Prepare-SharePoint-CVE-2019-0604-PoC]]
