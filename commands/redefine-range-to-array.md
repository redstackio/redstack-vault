---
data: Range = Array
tags:
  - mruby
  - ruby
  - type-confusion
type: command
executor: ruby
platforms:
  - mruby
  - Ruby
id: a621798c-2608-4621-ac22-d99d440f4261
created_at: '2025-12-11T03:47:48.548Z'
updated_at: '2025-12-11T03:47:48.548Z'
verified: false
validated: true
submitted: true
---
# redefine-range-to-array

## Command

```ruby
Range = Array
```

## Description

Redefines the Range constant to point to the Array class, exploiting runtime constant lookup in mruby to set up type confusion for subsequent exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Range = Array` | Assigns Range to Array class | Yes |

## Examples

### Basic Usage

```ruby
Range = Array
```

### Advanced Usage

```ruby
# Could redefine to other classes, e.g., Range = Hash
```

## Expected Output

No output; successfully redefines the constant for type confusion setup.

## Related

- [[commands/trigger-range-type-confusion]]
- [[procedures/Exploit-mruby-Range-Type-Confusion-for-DoS]]
