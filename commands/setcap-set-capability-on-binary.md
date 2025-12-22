---
id: 60ca1ac4-1bc4-40c2-b9ad-8467d28ce704
name: setcap-set-capability-on-binary
type: command
executor: bash
data: sudo setcap cap_setuid+ep $_BINARY
output: null
created_at: '2023-04-06T03:56:18.915364+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - privesc
  - setup
verified: true
validated: true
---

# setcap-set-capability-on-binary

## Command

```bash
sudo setcap cap_setuid+ep $_BINARY
```

## Description

Sets the cap_setuid+ep capability on a binary, allowing it to change its effective UID to root when executed. Requires sudo access; useful for lab setups or if partial escalation allows this.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_BINARY | Path to the binary (e.g., /usr/bin/python2.7) | Yes |
| cap_setuid+ep | Specific capability to set (effective and permitted setuid) | Built-in |

## Examples

### Basic Usage

```bash
sudo setcap cap_setuid+ep /usr/bin/python2.7
```

### Remove Capability

```bash
sudo setcap -r /usr/bin/python2.7
```

## Expected Output

No output on success; use getcap to verify:
```
/usr/bin/python2.7 = cap_setuid+ep
```

Error if no sudo: "Operation not permitted".

## Related

- [[procedures/Linux-Privilege-Escalation-via-Capabilities]]
