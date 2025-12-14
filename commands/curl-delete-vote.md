---
id: cmd-uuid-2
data: 'curl -X DELETE https://hackerone.com/reports/[Report_ID]/votes/[VOTE_ID]'
tags:
  - http-delete
  - vote-removal
type: command
output: HTTP/1.1 204 No Content
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:20.008Z'
verified: false
validated: true
submitted: true
---
# curl-delete-vote

## Command

```bash
curl -X DELETE https://hackerone.com/reports/[Report_ID]/votes/[VOTE_ID]
```

## Description

This command sends a DELETE request to remove a vote from a HackerOne Hacktivity report using the vote ID. It demonstrates unauthorized access to delete resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X DELETE` | Specifies the HTTP method | Yes |
| `https://hackerone.com/reports/[Report_ID]/votes/[VOTE_ID]` | Target endpoint with report and vote IDs | Yes |

## Examples

### Basic Usage

```bash
curl -X DELETE https://hackerone.com/reports/12345/votes/abc123
```

### Advanced Usage

```bash
curl -X DELETE https://hackerone.com/reports/12345/votes/abc123 -H "User-Agent: Mozilla/5.0"
```

## Expected Output

Successful response: HTTP 204 No Content, indicating the vote was deleted without body.

## Related

- [[commands/curl-create-vote]]
