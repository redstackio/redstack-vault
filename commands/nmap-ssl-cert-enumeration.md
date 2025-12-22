---
type: command
executor: bash
data: nmap --script ssl-cert $_TARGET -p$_PORT
output: null
platforms:
  - Linux
  - Web
tags:
  - reconnaissance
  - ssl
  - enumeration
verified: true
validated: true
---

# nmap-ssl-cert-enumeration

## Command

```bash
nmap --script ssl-cert $_TARGET -p$_PORT
```

## Description

This command uses Nmap's ssl-cert NSE script to enumerate SSL/TLS certificate details from a target host's specified port. It performs a lightweight TLS handshake to extract metadata like the certificate subject, issuer, public key type and size, signature algorithm, validity dates, and fingerprint hashes (MD5/SHA-1). Ideal for quick reconnaissance during web application testing to spot configuration issues without exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET | Target hostname or IP address (e.g., example.com or 192.168.1.1) | Yes |
| $_PORT | Target port for the SSL/TLS service (e.g., 443 for HTTPS) | Yes |
| --script ssl-cert | Enables the ssl-cert NSE script for certificate enumeration | Yes (built-in flag) |

## Examples

### Basic Usage

```bash
nmap --script ssl-cert example.com -p443
```

### Advanced Usage

Scan multiple ports or add verbosity:
```bash
nmap -v --script ssl-cert example.com -p443,8443
```

## Expected Output

```
Starting Nmap 7.80 ( https://nmap.org ) at 2023-10-01 10:00 UTC
Nmap scan report for example.com (93.184.216.34)
Host is up (0.10s latency).

PORT    STATE SERVICE
443/tcp open  https
| ssl-cert: Subject: commonName=example.com
| Issuer: commonName=Let's Encrypt Authority X3/organizationName=Let's Encrypt/countryName=US
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2023-09-01T00:00:00
| Not valid after:  2023-12-01T23:59:59
| MD5:   abcd ef12 3456 7890 1234 5678 9abc def0
|_SHA-1: 1234 5678 9abc def0 1234 5678 9abc def0 1234 5678

Nmap done: 1 IP address (1 host up) scanned in 1.50 seconds
```

The output includes certificate chain details; success is indicated by populated fields under 'ssl-cert' without errors like 'handshake failure'.

## Related

- [[procedures/Enumerate-SSL-Certificate-Details-with-Nmap]]
- [[tools/Nmap]]
