---
id: cmd-curl-db-endpoint
data: 'curl -X GET "https://█████████/schema/columns.byTable.html" -o schema.html'
tags:
  - web-access
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:11.300Z'
verified: false
validated: true
submitted: true
---
# curl-access-endpoint

## Command

```bash
curl -X GET "https://█████████/schema/columns.byTable.html" -o schema.html
```

## Description

This command uses curl to perform a GET request on an unauthenticated web endpoint to retrieve and save the backend database schema as an HTML file. It is used in scenarios involving improper access control testing to expose sensitive database structures without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| URL | The target endpoint URL (e.g., schema page) | Yes |
| `-o schema.html` | Outputs the response to a file named schema.html | No (but recommended for review) |

## Examples

### Basic Usage

```bash
curl -X GET "https://█████████/schema/columns.byTable.html"
```

### Advanced Usage

```bash
curl -X GET "https://█████████/schema/columns.byTable.html" -o schema.html -v
```

> The -v flag adds verbose output for debugging headers and responses.

## Expected Output

Successful execution returns an HTML response body containing the database schema, such as a table listing database tables (e.g., 'users' with columns 'id', 'name', 'email') and their details. No authentication errors; status code 200 OK.

## Related

- [[Related Procedure|procedures/Access-Database-Schema-Without-Authentication]]
