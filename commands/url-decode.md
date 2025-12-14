---
id: cmd-url-decode-2380084
data: >-
  echo 'ENCODED_JSON_HERE' | python3 -c "import urllib.parse;
  print(urllib.parse.unquote(input()))"
tags:
  - decoding
  - utility
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:29.077Z'
verified: false
validated: true
submitted: true
---
# url-decode

## Command

```bash
echo 'ENCODED_JSON_HERE' | python3 -c "import urllib.parse; print(urllib.parse.unquote(input()))"
```

## Description

This command decodes URL-encoded strings using Python's urllib, useful for extracting plain JSON from archived web paths.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `ENCODED_JSON_HERE` | The percent-encoded string to decode | Yes |
| `python3 -c ...` | Inline Python script for unquoting | Yes |

## Examples

### Basic Usage

```bash
echo '%7B%22clientId%22%3A%22value%22%7D' | python3 -c "import urllib.parse; print(urllib.parse.unquote(input()))"
```

### Advanced Usage

```bash
echo '$(cat encoded.txt)' | python3 -c "import urllib.parse, json; data = urllib.parse.unquote(input()); print(json.dumps(json.loads(data), indent=2))"
```

## Expected Output

Decoded string, e.g., '{"clientId":"value"}'.

## Related

- [[tools/beautifier-io]]
- [[procedures/Decode-and-Extract-API-Keys-from-JSON]]
