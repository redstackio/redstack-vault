---
data: a = Decimal.new
tags:
  - mruby
  - decimal
type: command
executor: mruby
platforms:
  - Linux
id: 0f49c3c0-57ed-49f8-bc43-a1fac04deaa0
created_at: '2025-12-11T03:47:48.068Z'
updated_at: '2025-12-11T03:47:48.068Z'
verified: false
validated: true
submitted: true
---
# decimal-new

## Command

```mruby
a = Decimal.new
```

## Description

Creates a new instance of the Decimal class in mruby, used as the first step in setting up objects for vulnerability exploitation like self-initialization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | No parameters; instantiates with defaults | No |

## Examples

### Basic Usage

```mruby
a = Decimal.new
```

## Expected Output

A new Decimal object is returned, ready for method calls.

## Related

- [[commands/decimal-initialize-self]]
- [[procedures/Create-mruby-Decimal-Object]]
