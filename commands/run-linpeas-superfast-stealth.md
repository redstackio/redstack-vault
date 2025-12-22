---
id: new-uuid-4
name: run-linpeas-superfast-stealth
type: command
executor: bash
data: ./linpeas.sh -s
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - enumeration
  - stealth
verified: true
validated: true
---

# run-linpeas-superfast-stealth

## Command

```bash
./linpeas.sh -s
```

## Description

Executes LinPEAS in superfast stealth mode, skipping slow checks and avoiding disk writes for low-detection enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s | Superfast and stealth mode | Yes |

## Examples

### Basic Usage

```bash
./linpeas.sh -s
```

## Expected Output

[*] Quick System Scan
User: user1
Groups: user1 sudo

[!] Sudo privileges found

## Related

- [[procedures/Linux-Privilege-Escalation-Enumeration]]
- [[tools/linPEAS]]
