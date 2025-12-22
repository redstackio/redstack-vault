---
id: cmd-uuid-1
data: gem build securitytest.gemspec
tags:
  - gem-build
type: command
output: null
executor: bash
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:47.000Z'
verified: false
validated: true
submitted: true
---
# gem-build-securitytest

## Command

```bash
gem build securitytest.gemspec
```

## Description

Builds a RubyGem package from the specified Gemspec file, creating a .gem archive with embedded metadata including any malicious payloads like XSS in the homepage field.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| securitytest.gemspec | Path to the Gemspec file containing gem specifications and metadata | Yes |

## Examples

### Basic Usage

```bash
gem build securitytest.gemspec
```

### Advanced Usage

```bash
gem build --strict securitytest.gemspec
```

## Expected Output

Successfully built RubyGem
  Source path: /path/to/securitytest-0.1.0
  Caching disabled: metadata will not be cached
  Name: securitytest
  Version: 0.1.0
  File: securitytest-0.1.0.gem

Creates the .gem file in the current directory.

## Related

- [[commands/gem-install-securitytest]]
- [[procedures/Build-Malicious-Gem]]
