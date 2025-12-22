---
id: 843624d5-4646-49a6-a596-6f943fb2747f
name: ldd-list-dynamic-dependencies
type: command
executor: bash
data: ldd $_BINARY
output: null
created_at: '2023-04-06T03:56:19.400908+00:00'
updated_at: '2023-04-10T20:34:31.017246+00:00'
platforms:
  - Linux
tags:
  - recon
  - linux
verified: true
validated: true
---

# ldd-list-dynamic-dependencies

## Command

```bash
ldd $_BINARY
```

## Description

Lists the shared libraries required by an executable or shared library, showing resolved paths. Useful for verifying if a library loads from an attacker-controlled RPATH directory after placement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_BINARY | Path to the target executable or library | Yes |

## Examples

### Basic Usage

```bash
ldd ./flag15
```

### Advanced Usage

```bash
ldd /bin/su
```

## Expected Output

```
linux-gate.so.1 =>  (0x0068c000)
libc.so.6 => /lib/i386-linux-gnu/libc.so.6 (0x00110000)
/lib/ld-linux.so.2 (0x005bb000)
```

## Related

- [[procedures/Linux-Privilege-Escalation-via-Shared-Library-RPATH-Hijacking]]
- [[commands/readelf-list-needed-libraries-and-rpath]]
