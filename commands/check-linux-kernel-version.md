---
id: d3f828c7-6f45-4490-9096-63c7a13d9b49
name: check-linux-kernel-version
type: command
executor: bash
data: uname -r
output: null
created_at: '2023-04-06T03:56:19.629776+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - recon
  - linux
verified: true
validated: true
---

# check-linux-kernel-version

## Command

```bash
uname -r
```

## Description

This command retrieves the version of the running Linux kernel, useful for determining if the system is vulnerable to kernel-specific exploits like DirtyPipe (CVE-2022-0847), which affects versions 5.8 to 5.16.11.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -r | Output the kernel release (version) | Yes (built-in flag) |

## Examples

### Basic Usage

```bash
uname -r
```

### Advanced Usage

Combine with grep for version filtering:

```bash
grep -E '5\.[8-16](?![^.]*(17|18|19|20|21|22|23|24|25|26|27|28|29|30|31|32))' <(uname -r)
```

## Expected Output

A string like '5.15.0-25-generic', indicating the kernel release version.

## Related

- [[procedures/DirtyPipe-Kernel-Exploit-for-Privilege-Escalation]]
