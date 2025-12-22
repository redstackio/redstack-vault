---
type: command
executor: bash
data: lxc image import ./alpine-i686.tar.gz --alias alpine-priv-esc
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - lxc
  - image-import
verified: true
validated: true
---

# Import-Alpine-Image

## Command

```bash
lxc image import ./alpine-i686.tar.gz --alias alpine-priv-esc
```

## Description

Imports a built Alpine image tarball into the LXD image store, assigning an alias for easy reference in container creation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ./alpine-i686.tar.gz | Path to the image tarball | Yes |
| --alias alpine-priv-esc | Alias name for the image | Yes |

## Examples

### Basic Usage

```bash
lxc image import ./alpine.tar.gz --alias my-alpine
```

## Expected Output

Image imported.
Fingerprint: abc123...
Alias: alpine-priv-esc

## Related

- [[procedures/Linux-Privilege-Escalation-via-LXC-LXD-Alpine-Image]]
