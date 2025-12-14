---
data: 'app_class_name = VerifierRce::Application.name'
tags:
  - payload
  - ruby
type: command
output: '"VerifierRce::Application"'
executor: ruby
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.315Z'
id: 767343ce-35a4-4e17-b87d-75aea0a10e43
verified: false
validated: true
submitted: true
---
# get-app-class-name

## Command

```ruby
app_class_name = VerifierRce::Application.name
```

## Description

Get the application class name in console to derive secret_key_base.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Standard access | No |

## Examples

### Basic Usage

```ruby
app_class_name = VerifierRce::Application.name
```

## Expected Output

"VerifierRce::Application"

## Related

- [[commands/start-rails-console]]
