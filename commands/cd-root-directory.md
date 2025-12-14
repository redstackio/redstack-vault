---
id: cmd-cd-root-001
name: cd-root-directory
type: command
executor: bash
data: cd /root
output: Shell prompt changes to indicate current directory is /root
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:05.992Z'
platforms:
  - Linux
tags:
  - navigation
  - shell
verified: false
validated: true
submitted: true
---

# cd-root-directory

## Command

```bash
cd /root
```

## Description

Changes the current working directory to /root, setting it as the web root for the lactate server in the test setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/root` | Target directory path | Yes |

## Examples

### Basic Usage

```bash
cd /root
```

### Advanced Usage

```bash
cd /root && pwd
```

## Expected Output

Prompt updates to "root@host:/root#" or similar.

## Related

- [[commands/npm-install-lactate]]
- [[procedures/Install-and-Setup-Lactate-Server]]
