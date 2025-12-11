---
data: gem install rubyzip
tags:
  - ruby
  - install
type: command
executor: bash
platforms:
  - Linux
id: 958895a2-c05d-46c4-b94f-f0ea7691ab98
created_at: '2025-12-11T03:47:39.751Z'
updated_at: '2025-12-11T03:47:39.751Z'
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

Installs the rubyzip gem, a library for creating and handling zip files, used in crafting .nupkg packages for exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `gem` | Specifies the gem command | Yes |
| `install` | Installs the specified gem | Yes |
| `rubyzip` | The gem name for zip file manipulation | Yes |

## Examples

### Basic Usage

```bash
gem install rubyzip
```

## Expected Output

Successful installation message, e.g., 'Successfully installed rubyzip-2.3.2'.

## Related

- [[commands/gem-install-faraday]]
- [[procedures/Exploit-Gitaly-Race-for-Arbitrary-File-Read]]
