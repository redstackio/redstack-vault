---
id: cmd-002
data: gem install nokogiri
tags:
  - dependency
  - ruby
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.682Z'
verified: false
validated: true
submitted: true
---
# gem-install-nokogiri

## Command

```bash
gem install nokogiri
```

## Description

Installs the nokogiri Ruby gem, required for HTML/XML parsing in the Drupalgeddon2 exploit script.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| gem_name | Name of the gem (nokogiri) | Yes |

## Examples

### Basic Usage

```bash
gem install nokogiri
```

### Advanced Usage

```bash
gem install nokogiri --version 1.10.0
```

## Expected Output

'Successfully installed nokogiri-1.x.x' if not already present.

## Related

- [[Related Procedure: Download-and-Setup-Drupalgeddon2-Exploit]]
