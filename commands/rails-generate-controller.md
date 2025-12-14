---
data: rails generate controller Help
tags:
  - rails
  - development
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:12.375Z'
id: 1da7707c-06a5-446c-9523-21d3d8d556e0
verified: false
validated: true
submitted: true
---
# rails-generate-controller

## Command

```bash
rails generate controller Help
```

## Description

Generates a new controller named 'Help' in a Ruby on Rails application, creating necessary files for routing and views. Used to set up the controller for wildcard route exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| controller | Name of the controller to generate (e.g., Help) | Yes |

## Examples

### Basic Usage

```bash
rails generate controller Help
```

### Advanced Usage

```bash
rails generate controller Help --skip-routes
```

## Expected Output

create  app/controllers/help_controller.rb
create  app/views/help
create  app/views/help/index.html.erb
...
invoke  test_unit
create    test/controllers/help_controller_test.rb

## Related

- [[Related Procedure]]
