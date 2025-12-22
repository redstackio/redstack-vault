---
id: cmd-gdb-php
data: gdb --args sapi/cli/php -f ../crash/bz_poc.php
tags:
  - debugging
  - php
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.179Z'
verified: false
validated: true
submitted: true
---
# gdb-debug-php-script

## Command

```bash
gdb --args sapi/cli/php -f ../crash/bz_poc.php
```

## Description

Starts GDB to debug a PHP CLI execution of a POC script, allowing analysis of crashes from vulnerabilities like heap overflows in bzdecompress(). Use after 'run' in GDB to trigger and inspect the exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--args` | Passes subsequent arguments to the debugged program (PHP CLI) | Yes |
| `sapi/cli/php` | Path to PHP CLI executable | Yes |
| `-f` | Specifies the PHP file to execute | Yes |
| `../crash/bz_poc.php` | Path to the POC script | Yes |

## Examples

### Basic Usage

```bash
gdb --args sapi/cli/php -f ../crash/bz_poc.php
```
Then in GDB: `run`

### Advanced Usage

```bash
gdb --args sapi/cli/php -d memory_limit=-1 -f bz_poc.php
```

## Expected Output

GDB session initializes, loads PHP symbols. After 'run', shows SIGSEGV at vulnerable instruction, with backtrace to bzdecompress().

## Related

- [[commands/info-registers-eip]]
- [[procedures/Debug-and-Demonstrate-EIP-Control-with-GDB]]
