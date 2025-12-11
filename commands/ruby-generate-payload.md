---
data: ruby ./gen_payload3.rb
tags:
  - payload-generation
  - ruby
type: command
executor: bash
platforms:
  - Linux
id: 0925d150-11c1-4f7d-b3b5-48eb0cb01af7
created_at: '2025-12-11T03:48:06.034Z'
updated_at: '2025-12-11T03:48:06.034Z'
verified: false
validated: true
submitted: true
---
# ruby-generate-payload

## Command

```bash
ruby ./gen_payload3.rb
```

## Description

Executes a Ruby script to generate a malicious payload for Redis injection and deserialization in GitLab exploits, used after modifying the script with custom commands.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `./gen_payload3.rb` | Path to the payload generation script | Yes |

## Examples

### Basic Usage

```bash
ruby ./gen_payload3.rb
```

### Advanced Usage

Modify script first, then:
```bash
ruby ./gen_payload3.rb > payload.txt
```

## Expected Output

A string payload ready for injection, including Redis commands and deserialization object.

## Related

- [[procedures/Generate-Malicious-Redis-Injection-Payload]]
- [[tools/Ruby]]
