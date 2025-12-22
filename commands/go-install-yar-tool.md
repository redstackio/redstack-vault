---
id: 6513d12c-527e-425e-bce9-9f9f253c220c
name: go-install-yar-tool
type: command
executor: bash
data: go install github.com/nielsing/yar@latest
output: null
created_at: '2023-04-06T03:56:00.144326+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - installation
  - go
  - yar
verified: true
validated: true
---

# go-install-yar-tool

## Command

```bash
go install github.com/nielsing/yar@latest
```

## Description

This command installs the Yar tool, a Git secrets scanner, using Go's package manager. It downloads, compiles, and places the binary in your Go bin directory, making it executable from the command line. Use this before scanning repositories for secrets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `github.com/nielsing/yar@latest` | The Go module path and version tag for Yar | Yes |

## Examples

### Basic Usage

```bash
go install github.com/nielsing/yar@latest
```

### Advanced Usage

If pinning a specific version:

```bash
go install github.com/nielsing/yar@v1.0.0
```

## Expected Output

Successful installation shows:

```
go: downloading github.com/nielsing/yar v0.0.0-20230101000000-...
go: built github.com/nielsing/yar@latest
```

No output or errors indicate failure (e.g., network issues or missing Go).

## Related

- [[procedures/Git-Secrets-Harvesting-with-Yar]]
- [[commands/yar-scan-git-repo-for-secrets]]
