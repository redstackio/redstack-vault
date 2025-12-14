---
data: 'erb.instance_variable_set :@lineno, 1'
tags:
  - payload
  - erb
  - ruby
type: command
output: '1'
executor: ruby
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.227Z'
id: c8190511-dfc5-48e0-91f8-d57c7f0e8ebb
verified: false
validated: true
submitted: true
---
# set-erb-lineno

## Command

```ruby
erb.instance_variable_set :@lineno, 1
```

## Description

Set the line number instance variable for ERB deserialization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| @lineno | 1 | Yes |

## Examples

### Basic Usage

```ruby
erb.instance_variable_set :@lineno, 1
```

## Expected Output

1

## Related

- [[commands/set-erb-filename]]
