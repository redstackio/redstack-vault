---
id: 834e9fc5-2228-4220-97a8-71a01f9a7969-install
name: go-install-tko-subs
type: command
executor: bash
data: go install github.com/anshumanbh/tko-subs@latest
output: null
created_at: '2023-04-06T03:56:25.771557+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - installation
  - go-tool
verified: true
validated: true
---

# go-install-tko-subs

## Command

```bash
go install github.com/anshumanbh/tko-subs@latest
```

## Description

This command installs the tko-subs tool, a Go-based utility for detecting subdomain takeover vulnerabilities, by downloading and compiling it from the official GitHub repository. Use this before running scans to ensure the binary is available.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `github.com/anshumanbh/tko-subs@latest` | Repository URL and version tag to install from | Yes |

## Examples

### Basic Usage

```bash
go install github.com/anshumanbh/tko-subs@latest
```

### Advanced Usage

If specifying a version:
```bash
go install github.com/anshumanbh/tko-subs@v1.0.0
```

## Expected Output

Build progress messages like "go: downloading github.com/anshumanbh/tko-subs v1.x.x" followed by "go: built github.com/anshumanbh/tko-subs." No errors indicate successful installation. The binary is placed in $GOPATH/bin.

## Related

- [[procedures/Subdomain-Enumeration-and-Takeover-with-tko-subs]]
- [[commands/tko-subs-scan-domains-for-takeover]]
