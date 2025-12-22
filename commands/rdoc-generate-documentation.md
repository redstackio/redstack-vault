---
id: cmd-uuid-001
data: rdoc
tags:
  - rce
  - documentation
type: command
output: null
executor: bash
platforms:
  - Ruby
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:07.893Z'
verified: false
validated: true
submitted: true
---
# rdoc-generate-documentation

## Command

```bash
rdoc
```

## Description

Generates documentation for Ruby code by parsing source files and configuration, including the .rdoc_options file as YAML. In vulnerable versions, this triggers unsafe deserialization leading to RCE when processing untrusted inputs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None (default) | Generates docs for current directory | No |
| --all | Include all files | No |
| -o DIR | Output directory | No |

## Examples

### Basic Usage

```bash
rdoc
```

### Advanced Usage

```bash
rdoc --all -o ./docs
```

## Expected Output

Documentation files in the current or specified directory, with logs like 'Generating RDoc...' Potential RCE indicators include unexpected system commands or errors during parsing.

## Related

- [[commands/gem-update-rdoc]]
- [[procedures/Exploit-RDoc-YAML-Deserialization-for-RCE]]
