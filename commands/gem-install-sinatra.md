---
data: gem install sinatra
tags:
  - ruby
  - installation
type: command
executor: bash
platforms:
  - Linux
id: 558196dc-2175-44dc-be18-ec79ec6f1bd9
created_at: '2025-12-13T09:00:27.285Z'
updated_at: '2025-12-13T09:00:27.285Z'
verified: false
validated: true
submitted: true
---
# gem-install-sinatra

## Command

```bash
gem install sinatra
```

## Description

Installs the Sinatra gem, a lightweight web framework for Ruby, used to set up the attacker server for serving malicious files in XXE exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `gem` | Ruby package manager | Yes |
| `install` | Command to install packages | Yes |
| `sinatra` | Web framework for Ruby | Yes |

## Examples

### Basic Usage

```bash
gem install sinatra
```

## Expected Output

Installation success message, such as 'Successfully installed sinatra-3.0.0'.

## Related

- [[commands/ruby-server-rb]]
- [[procedures/Setup-Attacker-Server-for-XXE]]
