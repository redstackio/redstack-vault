---
id: 5ce54c19-9058-4396-a39b-3ca6d219f5ae
name: install-subfinder
type: command
executor: bash
data: go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
output: null
created_at: '2023-04-06T03:56:25.499301+00:00'
updated_at: '2023-04-10T20:25:39.525193+00:00'
platforms:
  - Linux
tags:
  - installation
  - recon
verified: true
validated: true
---

# install-subfinder

## Command

```bash
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```

## Description

This command installs the latest version of Subfinder, a subdomain enumeration tool, using Go's package manager. It downloads, builds, and places the binary in your $GOPATH/bin directory for immediate use in reconnaissance tasks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -v | Verbose output showing download and build progress | No |
| github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest | Repository and version to install | Yes |

## Examples

### Basic Usage

```bash
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```

### Advanced Usage

If specifying a version:

```bash
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@v2.5.0
```

## Expected Output

Verbose build logs:

go: downloading github.com/projectdiscovery/subfinder/v2 v2.x.x
go: extracting github.com/projectdiscovery/subfinder/v2 v2.x.x
go build ...

Success is indicated by no errors and the binary being executable via `subfinder -version`.

## Related

- [[procedures/Subdomain-Enumeration-with-Subfinder]]
- [[tools/Subfinder]]
