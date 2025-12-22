---
type: command
executor: bash
data: original_cmd_by_server || ls
tags:
  - command-injection
  - chaining
platforms:
  - Linux
verified: true
validated: true
---

# bash-chain-commands-with-or

## Command

```bash
original_cmd_by_server || $_INJECTED_COMMAND
```

## Description

Chains Bash commands with `||`, running the second only if the first fails. Useful in injections for fallback reconnaissance or error handling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_INJECTED_COMMAND | Fallback command (e.g., ls) | Yes |

## Examples

### Basic Usage

```bash
false || ls
```

### Advanced Usage

```bash
ping invalid || whoami
```

## Expected Output

If first fails: Output of injected command only (e.g., directory listing).

## Related

- [[procedures/Command-Injection-Chaining-Commands]]
