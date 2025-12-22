---
type: command
executor: bash
data: python eternal_checker.py <target_ip>
tags:
  - recon
  - architecture
  - eternalblue
platforms:
  - Linux
verified: true
validated: true
---

# eternalblue-architecture-check

## Command

```bash
python eternal_checker.py <target_ip>
```

## Description

This command runs the eternal_checker.py script from the MS17-010 tools to determine the target's CPU architecture (x86 or x64), essential for selecting the correct EternalBlue exploit variant.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| <target_ip> | IP address of the target host | Yes |

## Examples

### Basic Usage

```bash
python eternal_checker.py 192.168.1.100
```

### Advanced Usage

```bash
python3 eternal_checker.py 192.168.1.100 --timeout 10
```

## Expected Output

```
[*] 192.168.1.100:445 => x64
```

## Related

- [[procedures/EternalBlue-SMB-Exploitation]]
- [[tools/MS17-010-EternalBlue-Tools]]
