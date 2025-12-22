---
id: cmd-run-parserbatch
data: ./parserbatch
tags:
  - test
  - parsing
type: command
output: 'Hostname: [fe80::1]'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.056Z'
verified: false
validated: true
submitted: true
---
# run-parserbatch-test

## Command

```bash
./parserbatch
```

## Description

Runs the compiled parserbatch program to test libcurl's parsing of IPv6 URLs from an input file, showing omission of zone identifiers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `seed_tmp.txt` | Input file with test URLs (implied) | Yes |

## Examples

### Basic Usage

```bash
./parserbatch
```

### Advanced Usage

```bash
./parserbatch seed_tmp.txt
```

> Explicitly specify input file.

## Expected Output

Outputs parsed hostnames and ports, e.g., 'Hostname: [fe80::1]' without zone ID for each URL.

## Related

- [[commands/compile-parserbatch-test]]
