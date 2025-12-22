---
type: command
executor: bash
data: original_cmd_by_server | ls
tags:
  - command-injection
  - chaining
platforms:
  - Linux
verified: true
validated: true
---

# bash-chain-commands-with-pipe

## Command

```bash
original_cmd_by_server | $_INJECTED_COMMAND
```

## Description

Pipes output from the original command to the injected one in Bash. Can be used to process or filter results in injections, though often for obfuscation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_INJECTED_COMMAND | Command to receive piped input (e.g., ls, though ls ignores stdin) | Yes |

## Examples

### Basic Usage

```bash
echo "test" | ls
```

### Advanced Usage

```bash
ls / | grep .txt
```

## Expected Output

Injected command processes original's stdout (e.g., filtered list if using grep).

## Related

- [[procedures/Command-Injection-Chaining-Commands]]
