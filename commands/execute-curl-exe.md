---
id: cmd-execute-curl-001
data: curl.exe --version
tags:
  - execution
  - trigger
type: command
output: 'curl version info, plus payload execution (e.g., calc launch).'
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.936Z'
verified: false
validated: true
submitted: true
---
# execute-curl-exe

## Command

```cmd
curl.exe --version
```

## Description

Executes curl.exe to trigger OpenSSL config load from insecure path, injecting and running the malicious DLL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--version` | Displays version (any flag works to init OpenSSL) | No |

## Examples

### Basic Usage

```cmd
curl.exe --version
```

### Advanced Usage

```cmd
curl.exe https://example.com
```

## Expected Output

curl version output; malicious code executes (e.g., calculator).

## Related

- [[procedures/Trigger-curl-Vulnerability]]
