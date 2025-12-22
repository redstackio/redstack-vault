---
id: 12345678-1234-5678-9abc-123456789abc
name: go-build-revsocks-windows-gui
type: command
executor: bash
data: GOOS=windows GOARCH=amd64 go build -ldflags="-H=windowsgui"
output: null
created_at: '2023-04-06T03:56:22.907951Z'
updated_at: '2023-04-10T20:25:18.397562Z'
platforms:
  - Windows
tags:
  - build
  - go
  - gui
verified: true
validated: true
---

# go-build-revsocks-windows-gui

## Command

```bash
GOOS=windows GOARCH=amd64 go build -ldflags="-H=windowsgui"
```

## Description

Builds a Windows GUI version of revsocks to avoid console popup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| GOOS=windows | Target OS | Yes |
| GOARCH=amd64 | Target architecture | Yes |
| -ldflags="-H=windowsgui" | GUI mode | Yes |

## Examples

### Basic Usage

```bash
GOOS=windows GOARCH=amd64 go build -ldflags="-H=windowsgui"
```

## Expected Output

No output; generates `revsocks.exe` in GUI mode.

## Related

- [[procedures/Reverse-SOCKS-Proxy-Pivoting]]
