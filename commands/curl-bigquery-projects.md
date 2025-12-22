---
data: >-
  TOKEN="████████"

  curl https://www.googleapis.com/bigquery/v2/projects -H "Authorization: Bearer
  $TOKEN" -H "Content-Type: application/json"
tags:
  - curl
  - api
type: command
executor: bash
platforms:
  - Linux
id: 2a013194-da1c-402a-92e9-94fb4926f399
created_at: '2025-12-13T09:00:27.753Z'
updated_at: '2025-12-13T09:00:27.753Z'
verified: false
validated: true
submitted: true
---
# curl-bigquery-projects

## Command

```bash
TOKEN="████████"
curl https://www.googleapis.com/bigquery/v2/projects -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json"
```

## Description

Queries BigQuery projects using a fetched GCP token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Authorization: Bearer $TOKEN"` | Authenticates with bearer token | Yes |
| `-H "Content-Type: application/json"` | Sets request content type | Yes |

## Examples

### Basic Usage

```bash
TOKEN="████████"
curl https://www.googleapis.com/bigquery/v2/projects -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json"
```

## Expected Output

JSON list of projects including en-development, en-testing, etc.

## Related

- [[procedures/Access-GCP-Services-with-Fetched-Token]]
