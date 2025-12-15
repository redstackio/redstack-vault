---
data: >-
  UNUSABLE_CHARS = [File::SEPARATOR, File::ALT_SEPARATOR, File::PATH_SEPARATOR,
  ":"].uniq.join("").freeze
tags:
  - analysis
  - constant
type: command
executor: irb
platforms:
  - Windows
  - Ruby
id: 40143173-51dd-4b04-8c39-f8c246c1aecb
created_at: '2025-12-14T17:26:22.877Z'
updated_at: '2025-12-14T17:26:22.877Z'
verified: false
validated: true
submitted: true
---
# define-unusable-chars

## Command

```ruby
UNUSABLE_CHARS = [File::SEPARATOR, File::ALT_SEPARATOR, File::PATH_SEPARATOR, ":"].uniq.join("").freeze
```

## Description

Defines the UNUSABLE_CHARS constant used in Tempfile sanitization, inspecting Windows-specific path separators.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| separators | Array of File constants and ":" | Yes |

## Examples

### Basic Usage

```ruby
UNUSABLE_CHARS = [File::SEPARATOR, File::ALT_SEPARATOR, File::PATH_SEPARATOR, ":"].uniq.join("").freeze
puts UNUSABLE_CHARS
```

### Advanced Usage

```ruby
UNUSABLE_CHARS = (" /\\;:".chars.uniq.join).freeze
```

## Expected Output

"/\\;:"

## Related

- [[Related Procedure]]
