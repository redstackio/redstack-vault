---
type: command
executor: bash
data: uname -a
tags:
  - reconnaissance
  - system-information
platforms:
  - Linux
verified: true
validated: true
---

# uname-kernel-version

## Command

```bash
uname -a
```

## Description

This command displays detailed system information, including the Linux kernel version, architecture, and build details. It is essential for identifying potential vulnerabilities during privilege escalation planning, as many kernel exploits are version-specific.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -a | Display all information (kernel name, node name, kernel release, kernel version, machine, processor, hardware platform, operating system) | Yes |

## Examples

### Basic Usage

```bash
uname -a
```

### Alternative for Kernel Release Only

```bash
uname -r
```

## Expected Output

```
Linux hostname 5.4.0-42-generic #46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
```

The output reveals the kernel release (e.g., 5.4.0-42-generic), which can be used to search for exploits.

## Related

- [[procedures/Kernel-Exploits-Privilege-Escalation-on-Linux]]
