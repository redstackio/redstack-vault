---
data: 'Range.remove_method(:initialize_copy)'
tags:
  - ruby
  - method-removal
type: command
executor: ruby
platforms:
  - Ruby
  - mruby
id: 1ac02fc8-952e-474a-b77e-4e0bcc79aca4
created_at: '2025-12-11T03:47:48.382Z'
updated_at: '2025-12-11T03:47:48.382Z'
verified: false
validated: true
submitted: true
---
# remove-range-initialize-copy

## Command

```ruby
Range.remove_method(:initialize_copy)
```

## Description

Removes the initialize_copy method from the Range class in Ruby/mruby, preventing proper initialization during object duplication and enabling exploits like null pointer dereferences.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `:initialize_copy` | Symbol for the method to remove | Yes |

## Examples

### Basic Usage

```ruby
Range.remove_method(:initialize_copy)
```

### Advanced Usage

```ruby
# After removal, duplicate to exploit
Range.remove_method(:initialize_copy)
(1..2).dup
```

## Expected Output

No output if successful; the method is removed from the class.

## Related

- [[commands/(1..2)-dup-to_s]]
- [[procedures/Remove-Initialize-Copy-Method-from-Range-Class]]
