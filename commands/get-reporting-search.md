---
data: 'GET /.reporting-2021-*/_search?sort=created_at:desc&size=1'
tags:
  - kibana
  - api
type: command
output: Latest job details including headers
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.122Z'
id: 62d80142-da6b-40b0-8993-f20e678f833b
verified: false
validated: true
submitted: true
---
# get-reporting-search

## Command

```bash
GET /.reporting-2021-*/_search?sort=created_at:desc&size=1
```

## Description

Queries Elasticsearch for the most recent reporting job to extract a valid authorization header for creating new jobs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sort | created_at:desc for newest | Yes |
| size | 1 to get latest | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "localhost:9200/.reporting-2021-*/_search?sort=created_at:desc&size=1"
```

## Expected Output

JSON with job details, including auth headers from prior requests.

## Related

- [[commands/post-reporting-job-pdf]]
- [[procedures/Create-Reporting-Job-to-Trigger-Exploit-via-Redirect]]
