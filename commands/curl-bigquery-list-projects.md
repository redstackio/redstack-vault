---
id: uuid-c9
data: >-
  TOKEN="[redacted]" curl https://www.googleapis.com/bigquery/v2/projects -H
  "Authorization: Bearer $TOKEN" -H "Content-Type: application/json"
tags:
  - gcp
  - api
type: command
output: >-
  JSON list of projects including 'en-development', 'en-testing',
  'sf6fb9ce958be8d9d-tp'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.594Z'
verified: false
validated: true
submitted: true
---
# curl-bigquery-list-projects

## Command

```bash
TOKEN="[redacted]" curl https://www.googleapis.com/bigquery/v2/projects -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json"
```

## Description

Queries the BigQuery API using a stolen bearer token to list accessible projects.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| TOKEN | Bearer token variable | Yes |
| Authorization: Bearer $TOKEN | Auth header | Yes |
| Content-Type: application/json | Request type | Yes |

## Examples

### Basic Usage

```bash
TOKEN="ya29..." curl https://www.googleapis.com/bigquery/v2/projects -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json"
```

## Expected Output

JSON array of projects with ids like 'en-development'.

## Related

- [[Related Procedure: Query-GCP-APIs-with-Obtained-Token]]
