---
id: cmd-run-npm
data: npm
tags:
  - execution
  - hijacking
type: command
output: Node.js REPL prompt or malicious payload execution.
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.947Z'
verified: false
validated: true
submitted: true
---
# run-npm-command

## Command

```cmd
npm
```

## Description

Executes the 'npm' command, which in an exploited environment hijacks to run a malicious npm.exe from the writable PATH directory, demonstrating privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Runs default npm invocation | N/A |

## Examples

### Basic Usage

```cmd
npm
```

### Advanced Usage

```cmd
npm --version
```

## Expected Output

In hijacked setup: Executes malicious code (e.g., Node shell). Legitimate: npm help or version.

## Related

- [[procedures/Hijack-NPM-Command-via-PATH-Precedence]]
