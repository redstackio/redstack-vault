---
id: new-uuid-5
name: run-linpeas-with-password
type: command
executor: bash
data: ./linpeas.sh -P $_PASSWORD
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - enumeration
  - bruteforce
verified: true
validated: true
---

# run-linpeas-with-password

## Command

```bash
./linpeas.sh -P $_PASSWORD
```

## Description

Runs LinPEAS with a provided password for enhanced sudo checks and user bruteforcing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -P | Password for sudo and bruteforce | Yes |
| $_PASSWORD | The password string | Yes |

## Examples

### Basic Usage

```bash
./linpeas.sh -P "password123"
```

## Expected Output

[*] Sudo -l with password
User user1 may run the following commands on this host:
    (ALL : ALL) ALL

## Related

- [[procedures/Linux-Privilege-Escalation-Enumeration]]
- [[tools/linPEAS]]
