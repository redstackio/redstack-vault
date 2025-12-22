---
type: command
executor: bash
data: gem install winrm-fs
output: >-
  root@kali:~# gem install winrm-fs

  Fetching: erubi-1.9.0.gem (100%)

  Successfully installed erubi-1.9.0

  Fetching: little-plugger-1.1.4.gem (100%)

  Successfully installed little-plugger-1.1.4

  Fetching: logging-2.2.2.gem (100%)

  Successfully installed logging-2.2.2

  Fetching: rubyzip-2.0.0.gem (100%)

  Successfully installed rubyzip-2.0.0

  Fetching: builder-3.2.3.gem (100%)

  Fetching: gssapi-1.3.1.gem (100%)

  Successfully installed gssapi-1.3.1

  Fetching: gyoku-1.3.1.gem (100%)

  Successfully installed gyoku-1.3.1

  Fetching: nori-2.6.0.gem (100%)

  Successfully installed nori-2.6.0

  Fetching: rubyntlm-0.6.3.gem (100%)

  Successfully installed rubyntlm-0.6.3

  Fetching: winrm-2.3.4.gem (100%)

  Successfully installed winrm-2.3.4

  Fetching: winrm-fs-1.3.3.gem (100%)

  Successfully installed winrm-fs-1.3.3

  Parsing documentation for erubi-1.9.0

  Installing ri documentation for erubi-1.9.0

  Parsing documentation for little-plugger-1.1.4

  Installing ri documentation for little-plugger-1.1.4

  Parsing documentation for logging-2.2.2

  Installing ri documentation for logging-2.2.2

  Parsing documentation for rubyzip-2.0.0

  Installing ri documentation for rubyzip-2.0.0

  Parsing documentation for builder-3.2.3

  Installing ri documentation for builder-3.2.3

  Parsing documentation for gssapi-1.3.1

  Installing ri documentation for gssapi-1.3.1

  Parsing documentation for gyoku-1.3.1

  Installing ri documentation for gyoku-1.3.1

  Parsing documentation for nori-2.6.0

  Installing ri documentation for nori-2.6.0

  Parsing documentation for rubyntlm-0.6.3

  Installing ri documentation for rubyntlm-0.6.3

  Parsing documentation for winrm-2.3.4

  Installing ri documentation for winrm-2.3.4

  Parsing documentation for winrm-fs-1.3.3

  Installing ri documentation for winrm-fs-1.3.3

  Done installing documentation for erubi, little-plugger, logging, rubyzip,
  builder, gssapi, gyoku, nori, rubyntlm, winrm, winrm-fs after 2 seconds

  12 gems installed
platforms:
  - Linux
tags:
  - ruby
  - winrm
  - installation
  - package-manager
verified: true
validated: true
---

# gem-install-winrm-fs

## Command

```bash
gem install winrm-fs
```

## Description

This command installs the winrm-fs Ruby gem, which provides file system access over Windows Remote Management (WinRM). It is commonly used in offensive security operations to set up dependencies for remote file operations on Windows targets from a Ruby-based environment, such as during post-exploitation or lateral movement scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| winrm-fs | The specific gem package to install, enabling WinRM file system capabilities | Yes |

## Examples

### Basic Usage

```bash
gem install winrm-fs
```

This installs winrm-fs along with its dependencies like winrm, rubyntlm, and others.

### Advanced Usage

To install without documentation (faster):

```bash
gem install winrm-fs --no-document
```

## Expected Output

The command fetches and installs dependencies, showing progress for each gem:

```
root@kali:~# gem install winrm-fs
Fetching: erubi-1.9.0.gem (100%)
Successfully installed erubi-1.9.0
Fetching: little-plugger-1.1.4.gem (100%)
Successfully installed little-plugger-1.1.4
Fetching: logging-2.2.2.gem (100%)
Successfully installed logging-2.2.2
Fetching: rubyzip-2.0.0.gem (100%)
Successfully installed rubyzip-2.0.0
Fetching: builder-3.2.3.gem (100%)
Fetching: gssapi-1.3.1.gem (100%)
Successfully installed gssapi-1.3.1
Fetching: gyoku-1.3.1.gem (100%)
Successfully installed gyoku-1.3.1
Fetching: nori-2.6.0.gem (100%)
Successfully installed nori-2.6.0
Fetching: rubyntlm-0.6.3.gem (100%)
Successfully installed rubyntlm-0.6.3
Fetching: winrm-2.3.4.gem (100%)
Successfully installed winrm-2.3.4
Fetching: winrm-fs-1.3.3.gem (100%)
Successfully installed winrm-fs-1.3.3
Parsing documentation for erubi-1.9.0
Installing ri documentation for erubi-1.9.0
... (additional parsing output)
Done installing documentation for erubi, little-plugger, logging, rubyzip, builder, gssapi, gyoku, nori, rubyntlm, winrm, winrm-fs after 2 seconds
12 gems installed
```

Success is indicated by "Successfully installed" messages for all dependencies and the target gem.

## Related

- [[tools/gem]]
- [[commands/gem-list-installed]] (to verify installation)
