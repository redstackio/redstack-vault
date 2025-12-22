---
type: command
executor: bash
data: >-
  rdesktop -d $_DOMAIN -u $_USERNAME -p $_PASSWORD $_TARGET_IP -g $_GEOMETRY -r
  disk:share=$_SHARE_PATH
tags:
  - rdp
  - connection
  - share
platforms:
  - Linux
verified: true
validated: true
---

# rdesktop-connect-with-domain-credentials-and-share

## Command

```bash
rdesktop -d $_DOMAIN -u $_USERNAME -p $_PASSWORD $_TARGET_IP -g $_GEOMETRY -r disk:share=$_SHARE_PATH
```

## Description

Establishes an RDP connection to a target Windows machine using domain credentials and shares a local folder for file transfer during the session. Useful for initial remote access in domain environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -d $_DOMAIN | Domain for authentication | Yes |
| -u $_USERNAME | Username for login | Yes |
| -p $_PASSWORD | Password for login | Yes |
| $_TARGET_IP | IP or hostname of target | Yes |
| -g $_GEOMETRY | Screen geometry (e.g., 70% or 1024x768) | No |
| -r disk:share=$_SHARE_PATH | Local path to share as drive | No |

## Examples

### Basic Usage

```bash
rdesktop -d corp -u admin -p pass123 10.10.10.10 -g 70% -r disk:share=/home/user/share
```

### Advanced Usage

Omit geometry for default sizing:

```bash
rdesktop -d corp -u admin -p pass123 10.10.10.10 -r disk:share=/tmp/payloads
```

## Expected Output

Autodetecting from keyboard layout...
Autodetecting from language/region...
Connected to 10.10.10.10:3389
[RDP window opens with shared drive accessible]

## Related

- [[procedures/RDP-Remote-Code-Execution]]
- [[tools/rdesktop]]
