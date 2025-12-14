---
data: ruby generate.rb payload.rb
tags:
  - payload
  - ruby
type: command
executor: bash
platforms:
  - Linux
id: 29335e92-40aa-4190-ade4-089c2421f584
created_at: '2025-12-14T17:23:53.939Z'
updated_at: '2025-12-14T17:23:53.939Z'
verified: false
validated: true
submitted: true
---
# ruby-generate-payload

## Command

```bash
ruby generate.rb payload.rb
```

## Description

Runs a custom Ruby script to generate a base64-encoded Marshal payload from Ruby code in payload.rb, used for deserialization exploits in YAML contexts like RubyGems checksums.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| generate.rb | Script file adapted from Rails RCE example | Yes |
| payload.rb | Input file with Ruby code to encode (e.g., system calls) | Yes |

## Examples

### Basic Usage

```bash
ruby generate.rb payload.rb
```

### Advanced Usage

Adapt payload.rb for different commands, then rerun.

```bash
ruby generate.rb new_payload.rb
```

## Expected Output

Base64-encoded string representing the malicious Marshal payload for insertion into checksums.yaml.

## Related

- [[Related Procedure: Craft-Malicious-Gem-with-Deserialization-Payload]]
