---
type: command
executor: cmd
data: reg query "HKCU\Software\SimonTatham\PuTTY\Sessions"
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - credential-access
  - putty
verified: true
validated: true
---

# reg-query-putty-sessions

## Command

```cmd
reg query "HKCU\Software\SimonTatham\PuTTY\Sessions"
```

## Description

Dumps PuTTY session data for proxy credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Key path | PuTTY sessions path | Yes |

## Examples

### Basic Usage

```cmd
reg query "HKCU\Software\SimonTatham\PuTTY\Sessions"
```

## Expected Output

```
HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\Default
    ProxyPassword    REG_SZ    proxy123
```

## Related

- [[procedures/windows-password-and-credential-query-via-registry]]
