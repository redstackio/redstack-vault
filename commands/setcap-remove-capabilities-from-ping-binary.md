---
id: 06b83c07-8e50-41cf-8bd7-4980d4866bb5
name: setcap-remove-capabilities-from-ping-binary
type: command
executor: bash
data: /usr/bin/setcap -r /bin/ping
output: null
created_at: '2023-04-06T03:56:18.886484+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - capabilities
  - privilege-escalation
verified: true
validated: true
---

# setcap-remove-capabilities-from-ping-binary

## Command

```bash
/usr/bin/setcap -r /bin/ping
```

## Description

This command removes all extended attributes, including capabilities, from the /bin/ping binary using the -r flag, resetting it to a non-privileged state. Useful for cleaning up after testing or reverting escalations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -r | Flag to remove all capabilities | Yes |
| /bin/ping | Path to the target binary | Yes |

## Examples

### Basic Usage

```bash
/usr/bin/setcap -r /bin/ping
```

### Advanced Usage

For a different binary:

```bash
/usr/bin/setcap -r /usr/bin/mytool
```

## Expected Output

On success, no output. On failure, error like "Failed to set capabilities on file '/bin/ping' (Operation not permitted)". Verify with `getcap /bin/ping` showing no capabilities.

## Related

- [[procedures/Linux-Privilege-Escalation-via-Capabilities-Edit]]
- [[commands/setcap-add-cap_net_raw-p-to-ping-binary]]
