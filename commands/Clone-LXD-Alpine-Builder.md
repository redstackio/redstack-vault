---
type: command
executor: bash
data: 'git clone https://github.com/saghul/lxd-alpine-builder'
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - setup
  - image-building
verified: true
validated: true
---

# Clone-LXD-Alpine-Builder

## Command

```bash
git clone https://github.com/saghul/lxd-alpine-builder
```

## Description

Clones the GitHub repository containing the LXD Alpine image builder script, which is used to create custom Alpine images for LXD containers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://github.com/saghul/lxd-alpine-builder | Repository URL | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/saghul/lxd-alpine-builder
```

## Expected Output

Cloning into 'lxd-alpine-builder'...
remote: Enumerating objects: ..., done.
...

Directory 'lxd-alpine-builder' created with build-alpine script.

## Related

- [[procedures/Linux-Privilege-Escalation-via-LXC-LXD-Alpine-Image]]
