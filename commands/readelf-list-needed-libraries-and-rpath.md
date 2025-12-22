---
id: 266b69d1-bcc4-4325-898d-fc142bb17079
name: readelf-list-needed-libraries-and-rpath
type: command
executor: bash
data: readelf -d $_BINARY | egrep "NEEDED|RPATH"
output: null
created_at: '2023-04-06T03:56:19.400857+00:00'
updated_at: '2023-04-10T20:34:31.017246+00:00'
platforms:
  - Linux
tags:
  - recon
  - linux
verified: true
validated: true
---

# readelf-list-needed-libraries-and-rpath

## Command

```bash
readelf -d $_BINARY | egrep "NEEDED|RPATH"
```

## Description

Displays the dynamic section of an ELF binary, filtering for shared library dependencies (NEEDED) and runtime library search paths (RPATH). Use this to identify hijackable libraries and writable paths for RPATH attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_BINARY | Path to the target ELF binary (e.g., ./flag15) | Yes |
| -d | Display dynamic section | Built-in |
| egrep "NEEDED\|RPATH" | Filter for relevant lines | Built-in |

## Examples

### Basic Usage

```bash
readelf -d flag15 | egrep "NEEDED|RPATH"
```

### Advanced Usage

```bash
readelf -d /usr/bin/sudo | egrep "NEEDED|RPATH"
```

## Expected Output

```
0x00000001 (NEEDED)                     Shared library: [libc.so.6]
0x0000000f (RPATH)                      Library rpath: [/var/tmp/flag15]
```

## Related

- [[procedures/Linux-Privilege-Escalation-via-Shared-Library-RPATH-Hijacking]]
- [[commands/ldd-list-dynamic-dependencies]]
