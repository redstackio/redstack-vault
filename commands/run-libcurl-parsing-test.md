---
id: cmd-parserbatch-run-001
data: ./parserbatch
tags:
  - test
  - parse
type: command
output: 'Parsed hostnames and ports for each URL, showing stripping of zone IDs.'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.524Z'
verified: false
validated: true
submitted: true
---
# run-libcurl-parsing-test

## Command

```bash
./parserbatch
```

## Description

Executes the compiled C program to test libcurl's parsing of IPv6 URLs with zone identifiers, reading from an input file like seed_tmp.txt and outputting extracted hostnames.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```bash
./parserbatch
```

### Advanced Usage

```bash
./parserbatch input.txt  # Custom input file
```

## Expected Output

Outputs parsed hostnames and ports for each URL in the file, showing stripping of zone IDs (e.g., [fe80::1] without %eth0).

## Related

- [[commands/compile-libcurl-test]]
