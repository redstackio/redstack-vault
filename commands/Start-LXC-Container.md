---
type: command
executor: bash
data: lxc start priv-esc-container
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - lxc
verified: true
validated: true
---

# Start-LXC-Container

## Command

```bash
lxc start priv-esc-container
```

## Description

Starts a previously initialized LXC/LXD container, making it operational for interaction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| priv-esc-container | Container name | Yes |

## Examples

### Basic Usage

```bash
lxc start mycontainer
```

## Expected Output

Starting priv-esc-container

Container started.

## Related

- [[procedures/Linux-Privilege-Escalation-via-LXC-LXD-Alpine-Image]]
