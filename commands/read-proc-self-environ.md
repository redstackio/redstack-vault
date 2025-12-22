---
id: abc12345-6789-0123-4567-890abcdef123
name: read-proc-self-environ
type: command
executor: bash
data: cat /proc/self/environ
output: null
created_at: '2023-04-06T03:56:38.241183+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - discovery
  - environment
  - procfs
verified: true
validated: true
---

# read-proc-self-environ

## Command

```bash
cat /proc/self/environ
```

## Description

This command reads the environment variables of the current process from the /proc/self/environ pseudo-file in Linux. It is useful in SSRF or post-exploitation scenarios to dump process-specific variables, such as AWS metadata paths or secrets, without invoking external tools.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; reads current process environ directly | No |

## Examples

### Basic Usage

```bash
cat /proc/self/environ
```

### Piping to Filter

```bash
cat /proc/self/environ | tr '\0' '\n' | grep AWS
```

## Expected Output

Null-separated key=value pairs, e.g.:

HOME=/root\0PATH=/usr/bin:/bin\0AWS_CONTAINER_CREDENTIALS_RELATIVE_URI=/v2/credentials/task-uuid\0...

Parse with tr '\0' '\n' to make readable lines. Success is indicated by listing variables without permission errors.
