---
data: gem install rubyzip
tags:
  - setup
  - ruby
type: command
output: Successfully installed rubyzip
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.665Z'
id: d79385ef-d138-4e95-831f-7a45cdde2450
verified: false
validated: true
submitted: true
---
# gem-install-rubyzip

## Command

```bash
gem install rubyzip
```

## Description

Installs the RubyZip gem for creating and manipulating ZIP archives, essential for packaging .nuspec into .nupkg files.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| install | Specifies gem to install | Yes |
| rubyzip | Name of the ZIP library gem | Yes |

## Examples

### Basic Usage

```bash
gem install rubyzip
```

### Advanced Usage

```bash
gem install rubyzip --version 2.3.0
```

## Expected Output

Successful installation of RubyZip gem, confirming archive handling capability.

## Related

- [[commands/gem-install-faraday]]
- [[procedures/Create-Malicious-NuGet-Package-with-Path-Traversal-Payload]]
