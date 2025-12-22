---
id: cmd-generate-controller
data: bin/rails generate controller Poc1 index --skip-routes
tags:
  - generate
  - controller
type: command
output: Generated files
executor: bash
platforms:
  - Ruby on Rails
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:25.720Z'
verified: false
validated: true
submitted: true
---
# rails-generate-poc1-controller

## Command

```bash
bin/rails generate controller Poc1 index --skip-routes
```

## Description

Generates a Poc1 controller with index action, skipping route addition.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| controller | Poc1 | Yes |
| action | index | Yes |
| --skip-routes | Avoid adding routes | Yes |

## Examples

### Basic Usage

As above.

## Expected Output

create  app/controllers/poc1_controller.rb
create  app/views/poc1

## Related

- [[procedures/Build-Sample-Vulnerable-Rails-Application-with-Docker]]
