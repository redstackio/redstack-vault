---
id: cmd-uuid-1
data: 'curl "https://www.zomato.com/php/instagram_tag_relay?callback=test"'
tags:
  - recon
  - web-test
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:47.292Z'
verified: false
validated: true
submitted: true
---
# curl-basic-endpoint-test

## Command

```bash
curl "https://www.zomato.com/php/instagram_tag_relay?callback=test"
```

## Description

This command sends a basic GET request to the Zomato endpoint with a test value in the callback parameter to check for direct reflection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target endpoint with callback param | Yes |

## Examples

### Basic Usage

```bash
curl "https://www.zomato.com/php/instagram_tag_relay?callback=test"
```

### Advanced Usage

```bash
curl -X POST -d "callback=test" https://www.zomato.com/php/instagram_tag_relay
```

## Expected Output

Response body containing the raw 'test' string, e.g., JSON or HTML with unsanitized input.

## Related

- [[Related Procedure]]
