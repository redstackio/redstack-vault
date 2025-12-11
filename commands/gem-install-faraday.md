---
data: gem install faraday
tags:
  - ruby
  - install
type: command
executor: bash
platforms:
  - Linux
id: 80daf7db-943c-4049-b292-f3d9720b5a09
created_at: '2025-12-11T03:47:39.757Z'
updated_at: '2025-12-11T03:47:39.757Z'
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

Installs the Faraday gem, an HTTP client library required for exploit scripts interacting with APIs like GitLab's.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `gem` | Specifies the gem command | Yes |
| `install` | Installs the specified gem | Yes |
| `faraday` | The gem name for HTTP client library | Yes |

## Examples

### Basic Usage

```bash
gem install faraday
```

## Expected Output

Successful installation message, e.g., 'Successfully installed faraday-2.7.1'.

## Related

- [[commands/gem-install-rubyzip]]
- [[procedures/Exploit-Gitaly-Race-for-Arbitrary-File-Read]]
