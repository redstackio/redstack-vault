---
id: 1e11b496-a2e0-4031-b4cb-f36e7e2d0066
name: whereis-lib-mysqludf-sys-so
type: command
executor: bash
data: whereis lib_mysqludf_sys.so
output: null
created_at: '2023-04-06T03:56:34.963960+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - recon
  - mysql-udf
verified: true
validated: true
---

# whereis-lib-mysqludf-sys-so

## Command

```bash
whereis lib_mysqludf_sys.so
```

## Description

Locates the lib_mysqludf_sys.so library file on the Linux file system, which is required for MySQL UDF-based command execution. Use this to verify if the UDF is pre-installed before attempting to load it.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| lib_mysqludf_sys.so | The name of the library to search for | Yes |

## Examples

### Basic Usage

```bash
whereis lib_mysqludf_sys.so
```

### Expected Output

If installed:
```
lib_mysqludf_sys: /usr/lib/lib_mysqludf_sys.so
```

If not found:
```
lib_mysqludf_sys:
```

## Related

- [[procedures/MySQL-UDF-Command-Execution-via-lib_mysqludf_sys.so]]
