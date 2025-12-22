---
data: make > /dev/null
tags:
  - build
  - compile
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:19.108Z'
id: a20dd1e3-68c5-4604-ad8b-e668bc37b211
verified: false
validated: true
submitted: true
---
# make-build-curl

## Command

```bash
make > /dev/null
```

## Description

Compiles curl from the configured source code, building the binary in src/.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `> /dev/null` | Suppress build output | Yes |

## Examples

### Basic Usage

```bash
make > /dev/null
```

### Advanced Usage

```bash
make -j4 > /dev/null
```

## Expected Output

curl binary compiled in src/curl; no errors.

## Related

- [[commands/curl-version-check]]
