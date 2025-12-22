---
id: cmd-uuid-2
data: gem install securitytest-0.1.0.gem
tags:
  - gem-install
type: command
output: null
executor: bash
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:46.994Z'
verified: false
validated: true
submitted: true
---
# gem-install-securitytest

## Command

```bash
gem install securitytest-0.1.0.gem
```

## Description

Installs a local .gem file into the RubyGems environment, registering its metadata (including potentially malicious homepage URLs) for use in tools like the gem server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| securitytest-0.1.0.gem | Path to the .gem package file | Yes |

## Examples

### Basic Usage

```bash
gem install securitytest-0.1.0.gem
```

### Advanced Usage

```bash
gem install --local --no-document securitytest-0.1.0.gem
```

## Expected Output

Successfully installed securitytest-0.1.0

Parsed the gem and added it to the local registry.

## Related

- [[commands/gem-build-securitytest]]
- [[procedures/Install-Malicious-Gem]]
