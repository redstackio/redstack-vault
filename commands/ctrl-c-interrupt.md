---
data: ^C
tags:
  - interrupt
type: command
executor: bash
platforms:
  - Linux
id: 6f780bb4-0e81-4245-9a32-98f233d59c51
created_at: '2025-12-11T03:47:47.791Z'
updated_at: '2025-12-11T03:47:47.791Z'
verified: false
validated: true
submitted: true
---
# ctrl-c-interrupt

## Command

```bash
^C
```

## Description

Interrupts the running process (CTRL-C), used to terminate the headless_shell after allowing time for exploit to run.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | N/A | N/A |

## Examples

### Basic Usage

Press CTRL-C in the terminal.

## Expected Output

Stops the headless_shell process.

## Related

- [[procedures/Execute-Headless-Chromium-Exploit]]
- [[commands/headless-shell-exploit]]
