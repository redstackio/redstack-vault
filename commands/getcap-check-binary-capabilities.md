---
id: 832a04cd-9389-4b12-9c4d-446c7636f706
name: getcap-check-binary-capabilities
type: command
executor: bash
data: getcap $_BINARY
output: null
created_at: '2023-04-06T03:56:18.915248+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - privesc
  - enumeration
verified: true
validated: true
---

# getcap-check-binary-capabilities

## Command

```bash
getcap $_BINARY
```

## Description

Displays the capabilities assigned to a specific binary file. Use this to identify if a binary has dangerous capabilities like cap_setuid+ep that can be exploited for privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_BINARY | Path to the binary to check (e.g., /usr/bin/python2.7) | Yes |

## Examples

### Basic Usage

```bash
getcap /usr/bin/python2.7
```

### Check Multiple Binaries

```bash
getcap /usr/bin/openssl /usr/bin/ping
```

## Expected Output

If capabilities are present:
```
/usr/bin/python2.7 = cap_setuid+ep
```

If none:
```
/usr/bin/python2.7 =
```

No capabilities mean no immediate exploit via this method.

## Related

- [[procedures/Linux-Privilege-Escalation-via-Capabilities]]
