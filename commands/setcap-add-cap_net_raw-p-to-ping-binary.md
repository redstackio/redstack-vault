---
id: 8b63bb63-640e-452f-a908-cb4e5cedfb33
name: setcap-add-cap_net_raw-p-to-ping-binary
type: command
executor: bash
data: /usr/bin/setcap cap_net_raw+p /bin/ping
output: null
created_at: '2023-04-06T03:56:18.886416+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - capabilities
  - privilege-escalation
verified: true
validated: true
---

# setcap-add-cap_net_raw-p-to-ping-binary

## Command

```bash
/usr/bin/setcap cap_net_raw+p /bin/ping
```

## Description

This command adds the cap_net_raw capability with the +p (permitted and inheritable) flag to the /bin/ping binary, allowing non-root users to perform raw network operations like ICMP pings, which is a form of privilege escalation by delegating root-level permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| cap_net_raw+p | The capability to add (raw network access, inheritable) | Yes |
| /bin/ping | Path to the target binary | Yes |

## Examples

### Basic Usage

```bash
/usr/bin/setcap cap_net_raw+p /bin/ping
```

### Advanced Usage

To add to a different binary:

```bash
/usr/bin/setcap cap_net_raw+p /usr/bin/mytool
```

## Expected Output

On success, no output is produced. On failure (e.g., insufficient permissions), it outputs something like "Failed to set capabilities on file '/bin/ping' (Operation not permitted)". Verify with `getcap /bin/ping` showing `/bin/ping = cap_net_raw+p`.

## Related

- [[procedures/Linux-Privilege-Escalation-via-Capabilities-Edit]]
- [[commands/setcap-remove-capabilities-from-ping-binary]]
