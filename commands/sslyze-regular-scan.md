---
type: command
executor: bash
data: sslyze --regular $_TARGET_HOST
output: null
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - reconnaissance
  - ssl-tls
  - cryptography
verified: true
validated: true
---

# Sslyze Regular Scan

## Command

```bash
sslyze --regular $_TARGET_HOST
```

## Description

This command performs a standard enumeration of the target's SSL/TLS configuration using SSLyze. It retrieves details such as the certificate chain, subject alternative names, validity periods, supported cipher suites, protocol versions, and checks for common vulnerabilities like Heartbleed, ROBOT, and more. Ideal for reconnaissance of HTTPS-enabled services to identify misconfigurations or weak security postures.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_HOST | Target hostname, IP address, or IP:port (e.g., example.com:443 or 192.168.1.100) | Yes |
| --regular | Runs the regular scan plugin, which includes certificate information, cipher suites, TLS versions, and vulnerability checks | No (this is the default scan mode for basic enumeration) |

## Examples

### Basic Usage

```bash
sslyze --regular example.com
```

### Advanced Usage

```bash
sslyze --regular=client_certificates example.com:443
```

## Expected Output

```
example.com:443                       | TLS 1.3   | ecdhe_secp256r1_rsa_pss_rsa_aes_256_gcm_sha384 - accepted
                                     |           |  Internet Explorer 11
                                     |           |  Firefox 63 / Windows 10
                                     |           |  Android 11.0
* Certificate Information *
  Subject: CN=example.com
  Alternative Names: DNS:www.example.com, DNS:mail.example.com
  Not valid before: 2023-01-01 00:00:00 [UTC]
  Not valid after: 2024-01-01 00:00:00 [UTC]
  Signature Algorithm: sha256WithRSAEncryption
* Vulnerabilities *
  Heartbleed: Not vulnerable (Good)
  ROBOT: Not vulnerable (Good)
  CCS Injection: Not vulnerable (Good)
```

## Related

- [[procedures/enumerate-and-analyze-ssl-tls-configuration]]
- [[tools/sslyze]]
