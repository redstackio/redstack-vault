---
type: command
executor: bash
data: >-
  rdesktop -u $_USERNAME -p $_PASSWORD -g $_GEOMETRY -r disk:share=$_SHARE_PATH
  $_TARGET_IP
tags:
  - rdp
  - connection
  - local-auth
platforms:
  - Linux
verified: true
validated: true
---

# rdesktop-connect-with-local-credentials-and-share

## Command

```bash
rdesktop -u $_USERNAME -p $_PASSWORD -g $_GEOMETRY -r disk:share=$_SHARE_PATH $_TARGET_IP
```

## Description

Connects to a target via RDP using local (non-domain) credentials and shares a local folder. Suitable for workgroup or standalone Windows targets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u $_USERNAME | Local username | Yes |
| -p $_PASSWORD | Local password | Yes |
| -g $_GEOMETRY | Screen size (e.g., 70%) | No |
| -r disk:share=$_SHARE_PATH | Path to share | No |
| $_TARGET_IP | Target IP/hostname | Yes |

## Examples

### Basic Usage

```bash
rdesktop -u user -p pass 10.10.10.10 -g 70% -r disk:share=/tmp/share
```

## Expected Output

Connected to 10.10.10.10:3389
[Desktop session starts, share mounted]

## Related

- [[procedures/RDP-Remote-Code-Execution]]
- [[tools/rdesktop]]
