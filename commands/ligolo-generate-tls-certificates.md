---
id: a1cbce6a-9e8c-4374-a497-b85031d181e6
name: ligolo-generate-tls-certificates
type: command
executor: bash
data: |
  make certs TLS_HOST=example.com
output: null
created_at: '2023-04-06T03:56:22.792135+00:00'
updated_at: '2023-04-10T20:25:12.831311+00:00'
platforms:
  - Linux
tags:
  - tls
  - certificates
verified: true
validated: true
---

# Ligolo Generate TLS Certificates

## Command

```bash
make certs TLS_HOST=example.com
```

## Description

This command uses Make to generate self-signed TLS certificates for securing Ligolo tunnels. It creates a private key and certificate based on the provided host, which the agent will use to connect securely to the proxy.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| TLS_HOST | Hostname or IP for the certificate (e.g., attacker domain) | Yes |

## Examples

### Basic Usage

```bash
make certs TLS_HOST=attacker.example.com
```

### Advanced Usage

For IP-based: `make certs TLS_HOST=192.168.1.100`.

## Expected Output

Generating a RSA private key
writing new private key to 'server.key'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
... (OpenSSL prompts)
Signature ok
certificate request "server.csr" is valid

The 'certs' directory will contain server.crt and server.key upon success.

## Related

- [[procedures/setup-ligolo-for-reverse-tunneling]]
- [[tools/ligolo]]
