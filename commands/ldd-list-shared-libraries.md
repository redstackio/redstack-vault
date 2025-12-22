---
type: command
executor: bash
data: ldd $_EXECUTABLE
output: null
created_at: '2023-04-06T03:56:19.370291+00:00'
updated_at: '2023-04-10T20:34:33.738831+00:00'
platforms:
  - Linux
tags:
  - enumeration
  - dependencies
verified: true
validated: true
---

# ldd-list-shared-libraries

## Command

```bash
ldd $_EXECUTABLE
```

## Description

This command displays the shared library dependencies of a given executable or shared object, including the paths from which each library is loaded. It is essential for identifying potential hijack points in privilege escalation attacks by revealing if a binary loads libraries from user-controllable paths.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_EXECUTABLE | Path to the binary or library to analyze (e.g., /usr/bin/sudo or /opt/binary) | Yes |

## Examples

### Basic Usage

```bash
ldd /opt/binary
```

### Advanced Usage

```bash
ldd /usr/bin/sudo | grep lib
```

> Filters output to show only library names for quicker review.

## Expected Output

```	linux-vdso.so.1 (0x00007ffe961cd000)
	vulnlib.so.8 => /usr/lib/vulnlib.so.8 (0x00007fa55e55a000)
	/lib64/ld-linux-x86-64.so.2 => /usr/lib64/ld-linux-x86-64.so.2 (0x00007fa55e6c8000)
```

This sample shows dependencies for /opt/binary, with paths indicating where libraries are resolved. Look for => not found or paths like /tmp that can be manipulated.

## Related

- [[procedures/Linux-Privilege-Escalation-via-Shared-Library-Dependencies]]
