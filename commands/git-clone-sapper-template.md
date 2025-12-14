---
id: cmd-001
data: 'git clone https://github.com/sveltejs/sapper-template'
tags:
  - setup
  - clone
type: command
output: |-
  Cloning into 'sapper-template'...
  remote: Enumerating objects: X, done.
  ... (success messages)
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.549Z'
verified: false
validated: true
submitted: true
---
---

# git-clone-sapper-template

## Command

```bash
git clone https://github.com/sveltejs/sapper-template
```

## Description

Clones the Sapper template repository from GitHub to set up the base project for vulnerability reproduction. Use this to download the framework template without full history.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://github.com/sveltejs/sapper-template` | Repository URL | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/sveltejs/sapper-template
```

### Advanced Usage

```bash
git clone --depth 1 https://github.com/sveltejs/sapper-template sapper-dir
```

## Expected Output

Progress indicators and confirmation of directory creation with project files.

## Related

- [[Related Procedure: Clone-Sapper-Template-Project]]

---
