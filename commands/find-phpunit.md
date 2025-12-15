---
id: cmd-find-phpunit
data: find . -name "*phpunit*" -type d
tags:
  - search
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:27.781Z'
verified: false
validated: true
submitted: true
---
# find-phpunit

## Command

```bash
find . -name "*phpunit*" -type d
```

## Description

Searches the current directory recursively for directories containing 'phpunit' in the name, aiding in dependency discovery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| . | Start path | Yes |
| -name "*phpunit*" | Pattern match | Yes |
| -type d | Directories only | Yes |

## Examples

### Basic Usage

```bash
find . -name "*phpunit*" -type d
```

### Advanced Usage

```bash
find /path/to/app -name "*test*" -type f
```

## Expected Output

List of paths: './vendor/phpunit/phpunit'.

## Related

- [[ls]]
