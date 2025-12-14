---
data: echo -n "$1" | md5sum
tags:
  - hashing
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.938Z'
id: 457c239b-cd60-4088-895c-a3d4d43814c1
verified: false
validated: true
submitted: true
---
# Compute MD5 Hash

## Command

```bash
echo -n "$1" | md5sum
```

## Description

This command computes the MD5 hash of a provided string input, useful for generating predictable endpoints in vulnerabilities like CVE-2021-38314 where site URLs are hashed with salts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$1` | Input string (e.g., site URL + salt) | Yes |

## Examples

### Basic Usage

```bash
echo -n "https://example.com-redux" | md5sum
```

### Advanced Usage

```bash
echo -n "https://example.com-support" | md5sum
```

## Expected Output

Hexadecimal MD5 hash followed by the input string, e.g., 'd41d8cd98f00b204e9800998ecf8427e  -' (use only the hash part).

## Related

- [[Related Procedure]]
