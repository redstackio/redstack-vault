---
data: gem install faraday
tags:
  - setup
  - ruby
type: command
output: Successfully installed faraday
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.670Z'
id: 47d8a7b4-aa6b-486c-ab3f-65eac48275aa
verified: false
validated: true
submitted: true
---
# gem-install-faraday

## Command

```bash
gem install faraday
```

## Description

Installs the Faraday Ruby gem, an HTTP client library used for making API requests like package uploads in exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| install | Specifies gem to install | Yes |
| faraday | Name of the HTTP client gem | Yes |

## Examples

### Basic Usage

```bash
gem install faraday
```

### Advanced Usage

```bash
gem install faraday --version 1.0.0
```

## Expected Output

Description of what output to expect when the command runs successfully.

Successfully installed faraday-1.x.x and related dependencies.

## Related

- [[commands/gem-install-rubyzip]]
- [[procedures/Upload-Malicious-NuGet-Package-to-GitLab-Registry]]
