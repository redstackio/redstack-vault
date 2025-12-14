---
data: ln -s fake_ca.crt ca.crt
tags:
  - symlink
  - ca-swap
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:19.029Z'
id: ab7f1005-b11f-4bf4-8be6-50d1d61d75d2
verified: false
validated: true
submitted: true
---
# ln-symlink-fake-ca

## Command

```bash
ln -s fake_ca.crt ca.crt
```

## Description

Creates a symbolic link from ca.crt to fake_ca.crt to swap the trust anchor during the TOCTOU attack.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Symbolic link | Yes |
| `fake_ca.crt` | Target file | Yes |
| `ca.crt` | Link name | Yes |

## Examples

### Basic Usage

```bash
ln -s fake_ca.crt ca.crt
```

### Advanced Usage

```bash
ln -sf fake_ca.crt ca.crt
```

## Expected Output

Symlink created; ls -l shows ca.crt -> fake_ca.crt.

## Related

- [[commands/curl-http2-requests-with-cacert]]
