---
data: 'erb.instance_variable_set :@filename, ''1'''
tags:
  - payload
  - erb
  - ruby
type: command
output: '"1"'
executor: ruby
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.234Z'
id: 0262a10a-8d27-458d-b2d8-90f6a390e8a4
verified: false
validated: true
submitted: true
---
# set-erb-filename

## Command

```ruby
erb.instance_variable_set :@filename, '1'
```

## Description

Set the filename instance variable for ERB deserialization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| @filename | '1' | Yes |

## Examples

### Basic Usage

```ruby
erb.instance_variable_set :@filename, '1'
```

## Expected Output

"1"

## Related

- [[commands/set-erb-src]]
