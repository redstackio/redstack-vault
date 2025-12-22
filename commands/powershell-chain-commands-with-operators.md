---
type: command
executor: powershell
data: >-
  original_cmd_by_server; ls; original_cmd_by_server && ls;
  original_cmd_by_server | ls; original_cmd_by_server || ls
tags:
  - command-injection
  - chaining
platforms:
  - Windows
verified: true
validated: true
---

# powershell-chain-commands-with-operators

## Command

```powershell
original_cmd_by_server $_OPERATOR $_INJECTED_COMMAND
```

## Description

Demonstrates PowerShell chaining with operators: `;` (unconditional), `&&` (on success), `|` (pipe), `||` (on failure). Inject into PowerShell-executing vulnerabilities for multi-command execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_OPERATOR | Chaining operator (;, &&, |, ||) | Yes |
| $_INJECTED_COMMAND | Command to chain (e.g., ls, Get-ChildItem) | Yes |

## Examples

### Basic Usage

```powershell
Get-Date; ls
```

### Advanced Usage

```powershell
Test-Path file.txt && whoami
```

## Expected Output

Varies by operator: Sequential outputs for `;`, conditional for `&&`/ `||`, piped for `|`.

## Related

- [[procedures/Command-Injection-Chaining-Commands]]
