---
id: cmd-002
data: >-
  true | openssl s_client -connect ██████:443 2>/dev/null | openssl x509 -noout
  -text | perl -l -0777 -ne '@names=/\bDNS:([^\s,]+)/g; print join("\n", sort
  @names);'
tags:
  - ssl
  - certificate
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:57.313Z'
verified: false
validated: true
submitted: true
---
# openssl-inspect-ssl-certificate-for-dns-names

## Command

```bash
true | openssl s_client -connect ██████:443 2>/dev/null | openssl x509 -noout -text | perl -l -0777 -ne '@names=/\bDNS:([^\s,]+)/g; print join("\n", sort @names);'
```

## Description

This command establishes a TLS connection to the target IP, retrieves the SSL certificate, extracts its text details, and uses Perl to parse and print sorted DNS names from the Subject Alternative Name field. Ideal for verifying if an IP hosts a specific domain during bypass recon.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -connect | IP:port to connect (e.g., ██████:443) | Yes |
| 2>/dev/null | Suppress stderr output | Yes |
| -noout | Do not output the encoded certificate | Yes |
| -text | Output certificate in readable text | Yes |
| perl options (-l -0777 -ne) | Process input line-by-line, slurp mode, execute code | Yes |
| Regex (@names=/\bDNS:([^\s,]+)/g) | Match DNS names in SAN | Yes |

## Examples

### Basic Usage

```bash
true | openssl s_client -connect ██████:443 2>/dev/null | openssl x509 -noout -text | perl -l -0777 -ne '@names=/\bDNS:([^\s,]+)/g; print join("\n", sort @names);'
```

### Advanced Usage

```bash
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null | openssl x509 -noout -text | perl -l -0777 -ne '@names=/\bDNS:([^\s,]+)/g; print join("\n", sort @names);'
```

> Adds SNI for virtual hosting.

## Expected Output

List of DNS names from certificate, including █████████, confirming domain association.

## Related

- [[Related Procedure]]: [[procedures/Verify-Origin-IP-Using-SSL-Certificate-Inspection]]
