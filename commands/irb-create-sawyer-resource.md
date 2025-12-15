---
id: cmd-irb-create-resource
name: irb-create-sawyer-resource
type: command
executor: irb
data: 'a = Sawyer::Resource.new( Sawyer::Agent.new(""),to_s:"example",length:1)'
output: '{:to_s=>"example", :length=>1}'
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.272Z'
platforms:
  - Linux
tags:
  - irb
  - sawyer
  - object-creation
verified: false
validated: true
submitted: true
---

# irb-create-sawyer-resource

## Command

```irb
a = Sawyer::Resource.new( Sawyer::Agent.new(""),to_s:"example",length:1)
```

## Description

Creates a Sawyer::Resource object from a hash, demonstrating key-to-method conversion for poisoning analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| to_s | String value | Yes |
| length | Integer value | Yes |

## Examples

### Basic Usage

As shown.

## Expected Output

Hash-like object with methods.

## Related

- [[tools/irb]]
