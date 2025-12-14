---
id: cmd-git-clone-ysoserial
data: 'git clone https://github.com/frohoff/ysoserial.git'
tags:
  - setup
  - git
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:27.698Z'
verified: false
validated: true
submitted: true
---
# git-clone-ysoserial

## Command

```bash
git clone https://github.com/frohoff/ysoserial.git
```

## Description

Clones the ysoserial repository from GitHub to obtain the source code for building Java deserialization exploit tools.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://github.com/frohoff/ysoserial.git | Repository URL | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/frohoff/ysoserial.git
```

### Advanced Usage

```bash
git clone https://github.com/frohoff/ysoserial.git ysoserial-local
```

## Expected Output

Cloning into 'ysoserial'... 
remote: Enumerating objects: ..., done.
... (progress bars and completion)
Local copy of the ysoserial source code directory created.

## Related

- [[commands/cd-ysoserial]]
- [[procedures/Prepare-Ysoserial-Tool]]
