---
data: ruby -v
tags:
  - setup
  - ruby
type: command
output: 'ruby 2.6.0p0 (2018-12-25 revision 66547) [x86_64-darwin16]'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.380Z'
id: c6e19dff-2c27-470e-9775-6b96821bb93a
verified: false
validated: true
submitted: true
---
# check-ruby-version

## Command

```bash
ruby -v
```

## Description

Check the Ruby version during setup of vulnerable environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -v | Version flag | Yes |

## Examples

### Basic Usage

```bash
ruby -v
```

## Expected Output

ruby 2.6.0p0 (2018-12-25 revision 66547) [x86_64-darwin16]

## Related

- [[commands/check-rails-version]]
