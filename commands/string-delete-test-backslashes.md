---
data: '"FUZZ/../me/..\\please".delete(UNUSABLE_CHARS)'
tags:
  - test
  - delete-method
type: command
executor: irb
platforms:
  - Windows
  - Ruby
id: af462871-59d3-43a6-9b94-97dea55ed4f4
created_at: '2025-12-14T17:26:22.873Z'
updated_at: '2025-12-14T17:26:22.873Z'
verified: false
validated: true
submitted: true
---
# string-delete-test-backslashes

## Command

```ruby
"FUZZ/../me/..\\please".delete(UNUSABLE_CHARS)
```

## Description

Tests String.delete with UNUSABLE_CHARS on a fuzz string to show failure in removing escaped backslashes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| string | Input string with mixed separators like "FUZZ/../me/..\\please" | Yes |
| chars | UNUSABLE_CHARS constant | Yes |

## Examples

### Basic Usage

```ruby
"FUZZ/../me/..\\please".delete(UNUSABLE_CHARS)
```

### Advanced Usage

```ruby
"test\\..\\path".delete("/\\;: ")
```

## Expected Output

"FUZZ..me..\\please"

## Related

- [[Related Procedure]]
