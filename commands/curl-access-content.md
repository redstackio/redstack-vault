---
id: cmd-curl-access-content
data: 'curl https://campaign.starbucks.com.sg/path/to/uploaded/test.html -v'
tags:
  - web
  - xss
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:49.727Z'
verified: false
validated: true
submitted: true
---
# curl-access-content

## Command

```bash
curl https://campaign.starbucks.com.sg/path/to/uploaded/test.html -v
```

## Description

Fetches uploaded content to verify storage and potential rendering issues like XSS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Path to uploaded resource | Yes |
| `-v` | Verbose output | Yes |

## Examples

### Basic Usage

```bash
curl https://target.com/uploads/test.html -v
```

### Advanced Usage

```bash
curl -H "User-Agent: Mozilla/5.0" https://target.com/uploads/test.html -v
```

## Expected Output

Raw HTML content including script tags; in browser, would execute JS.

## Related

- [[Related Procedure: Trigger Stored XSS via Uploaded Content]]
