---
id: cmd-check-version
data: 'puts Rails::Html::Sanitizer::VERSION'
tags:
  - version
  - check
type: command
output: 1.4.3
executor: ruby
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:25.741Z'
verified: false
validated: true
submitted: true
---
# check-rails-sanitizer-version

## Command

```ruby
puts Rails::Html::Sanitizer::VERSION
```

## Description

Prints the installed version of the rails-html-sanitizer gem to confirm vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | No parameters | Yes |

## Examples

### Basic Usage

```ruby
puts Rails::Html::Sanitizer::VERSION
```

## Expected Output

1.4.3

## Related

- [[commands/load-rails-html-sanitizer-gem]]
- [[procedures/Verify-XSS-in-Rails-Sanitizer-Using-IRB]]
