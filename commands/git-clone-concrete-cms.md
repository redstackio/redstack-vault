---
id: cmd-git-clone-concrete-cms
data: 'git clone https://github.com/concrete5/concrete5.git'
tags:
  - recon
  - code-review
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:35.948Z'
verified: false
validated: true
submitted: true
---
# git-clone-concrete-cms

## Command

```bash
git clone https://github.com/concrete5/concrete5.git
```

## Description

This command clones the Concrete CMS repository from GitHub to locally review source code for vulnerabilities like XSS in the theme preview tool.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://github.com/concrete5/concrete5.git` | Repository URL | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/concrete5/concrete5.git
```

### Advanced Usage

```bash
git clone https://github.com/concrete5/concrete5.git concrete5-review
```

## Expected Output

Cloning into 'concrete5'... remote: Enumerating objects... Receiving objects... Resolving deltas... A new directory with source files is created.

## Related

- [[Related Procedure|procedures/Review-Concrete-CMS-Source-Code-for-XSS]]
