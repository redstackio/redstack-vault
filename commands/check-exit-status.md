---
id: cmd-check-exit
data: echo $?
tags:
  - verification
  - dos
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:37.265Z'
verified: false
validated: true
submitted: true
---
# check-exit-status

## Command

```bash
echo $?
```

## Description

This shell command prints the exit status of the previous command (e.g., curl), used to verify if the process was terminated due to out-of-memory conditions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$?` | Shell variable for last command's exit code | Yes |

## Examples

### Basic Usage

```bash
echo $?
```

### Advanced Usage

Not applicable; run immediately after the target command.

## Expected Output

137 (indicating SIGKILL from OOM killer).

## Related

- [[commands/curl-fetch-malicious-response]]
- [[procedures/Trigger-curl-Memory-Exhaustion-with-Malicious-Response]]
