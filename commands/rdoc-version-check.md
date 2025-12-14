---
data: rdoc -v
tags:
  - recon
  - version
type: command
executor: bash
platforms:
  - Ruby
id: 450f7363-f07e-4208-97e9-c8850faa25e6
created_at: '2025-12-14T17:23:42.425Z'
updated_at: '2025-12-14T17:23:42.425Z'
verified: false
validated: true
submitted: true
---
# rdoc-version-check

## Command

```bash
rdoc -v
```

## Description

Checks the installed version of RDoc, Ruby's documentation tool, to identify if it's vulnerable to deserialization attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose flag to display version info | Yes |

## Examples

### Basic Usage

```bash
rdoc -v
```

### Advanced Usage

```bash
rdoc --version
```

## Expected Output

rdoc 6.3.1 (or similar version string)

## Related

- [[commands/rdoc-execute]]
