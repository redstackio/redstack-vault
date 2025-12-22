---
id: 3d5b5e03-7ec4-47d8-b29f-62cbf5506a22
name: install-gitleaks-via-go-get
type: command
executor: bash
data: go install github.com/gitleaks/gitleaks/v8@latest
output: null
created_at: '2023-04-06T03:56:00.200417+00:00'
updated_at: '2023-04-10T20:33:56.272566+00:00'
platforms:
  - Linux
tags:
  - gitleaks
  - install
verified: true
validated: true
---

# install-gitleaks-via-go-get

## Command

```bash
go install github.com/gitleaks/gitleaks/v8@latest
```

## Description

This command installs the latest version of Gitleaks using Go's module system, making the binary available for native execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| go install | Go command to download and install | Built-in |
| github.com/gitleaks/gitleaks/v8@latest | Module path and version | Yes |

## Examples

### Basic Usage

```bash
go install github.com/gitleaks/gitleaks/v8@latest
```

### Advanced Usage

```bash
GOPATH=/custom/path go install github.com/gitleaks/gitleaks/v8@v8.15.0
```

## Expected Output

Successful install:

```
github.com/gitleaks/gitleaks/v8 (download)
```

Verify with `gitleaks version`.

## Related

- [[procedures/Detect-Secrets-in-Git-Repositories-with-Gitleaks]]
- [[tools/Gitleaks]]
