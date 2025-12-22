---
type: command
executor: bash
data: BadAssMacros.exe -h
output: null
platforms:
  - Windows
tags:
  - office
  - macro
  - help
verified: true
validated: true
---

# badassmacros-help

## Command

```bash
BadAssMacros.exe -h
```

## Description

Displays the help menu for BadAssMacros, showing all available options, parameters, and usage examples for creating VBA macros from shellcode.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-h` | Show help information | Yes |

## Examples

### Basic Usage

```bash
BadAssMacros.exe -h
```

## Expected Output

A text output listing flags such as:
- `-i <file>`: Input shellcode file
- `-w <type>`: Word or Excel output
- `-s <method>`: Classic or indirect injection
Example:
Usage: BadAssMacros.exe [options]
Options:
  -h, --help            Show this help
  -i, --input <FILE>    Path to raw shellcode
  ...

## Related

- [[procedures/Create-Office-Macro-Malware-with-BadAssMacros]]
- [[tools/BadAssMacros]]
