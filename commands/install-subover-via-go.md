---
id: bca9ecb5-ee48-4213-a375-d00f39dac06f
name: install-subover-via-go
type: command
executor: bash
data: go get github.com/Ice3man543/SubOver
output: null
created_at: '2023-04-06T03:56:25.834023+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - installation
  - reconnaissance
verified: true
validated: true
---

# install-subover-via-go

## Command

```bash
go get github.com/Ice3man543/SubOver
```

## Description

This command installs the SubOver tool, a Go-based utility for detecting subdomain takeover vulnerabilities, directly from its GitHub repository. It is used during the setup phase of reconnaissance activities to prepare the environment for subdomain analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `go get` | Go command to fetch and install the package | Built-in |
| `github.com/Ice3man543/SubOver` | Repository URL for SubOver | Yes |

## Examples

### Basic Usage

```bash
go get github.com/Ice3man543/SubOver
```

### Advanced Usage

If GOPATH is not set, export it first:
```bash
export GOPATH=$HOME/go
 go get github.com/Ice3man543/SubOver
```

## Expected Output

The command will show download progress:
```
go: downloading github.com/Ice3man543/SubOver v0.0.0-...
...
Success: Tool installed to $GOPATH/src/github.com/Ice3man543/SubOver
```
No errors if Go is properly configured; otherwise, it may prompt for Go installation.

## Related

- [[procedures/Subdomain-Enumeration-and-Takeover-Detection-using-SubOver]]
- [[commands/run-subover-subdomain-check]]
