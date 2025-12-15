---
data: erb = ERB.allocate
tags:
  - payload
  - erb
  - ruby
type: command
output: Uninitialized ERB instance
executor: ruby
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.252Z'
id: 1b54636d-3fa1-4435-be2d-92aebc29a387
verified: false
validated: true
submitted: true
---
# allocate-erb-object

## Command

```ruby
erb = ERB.allocate
```

## Description

Allocate a new ERB object without initialization for malicious template.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Allocation | No |

## Examples

### Basic Usage

```ruby
erb = ERB.allocate
```

## Expected Output

Uninitialized ERB instance

## Related

- [[commands/define-malicious-code]]
