---
id: ddf41931-9f6b-4e38-9310-3283215f7ba9
name: linenum-run-thorough-scan
type: command
executor: bash
data: ./LinEnum.sh -t 1
output: |-
  root@host:~$ ./LinEnum.sh -t 1
  ...
  [+] Thorough tests = Enabled
  ...
  ### SCAN COMPLETE ####################################
created_at: '2019-10-25T23:13:00.217988+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - enum
  - thorough
verified: true
validated: true
---

# linenum-run-thorough-scan

## Command

```bash
./LinEnum.sh -t 1
```

## Description

Executes LinEnum in thorough mode, enabling additional file timing tests to detect potential vulnerabilities related to file system access times, permissions, and modifications. This is useful for in-depth enumeration during privilege escalation assessments on Linux systems.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-t 1` | Enables thorough mode with file timing checks (0 for standard, 2 for extended with web) | Yes |

## Examples

### Basic Usage

```bash
./LinEnum.sh -t 1
```

### Advanced Usage

```bash
./LinEnum.sh -t 1 -e
```

Adds extended checks alongside thorough mode.

## Expected Output

The command outputs a comprehensive report starting with system details, followed by categorized findings:

```
root@host:~$ ./LinEnum.sh -t 1
[...]
[+] Thorough tests = Enabled
[...]
Kernel Information:
[...]
System Information:
[...]
### SCAN COMPLETE ####################################
```

Look for highlighted sections like "Interesting files found" or "Potential SUID binaries" indicating misconfigurations.

## Related

- [[procedures/enumerate-linux-privilege-escalation-paths-with-linenum]]
- [[tools/LinEnum]]
