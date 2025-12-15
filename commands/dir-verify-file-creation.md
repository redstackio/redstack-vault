---
data: 'puts `dir C:\\Users\\rootx\\`'
tags:
  - verification
  - dir
type: command
executor: irb
platforms:
  - Windows
  - Ruby
id: 7e3eb926-9959-450c-ae25-046ab36c5c79
created_at: '2025-12-14T17:26:22.880Z'
updated_at: '2025-12-14T17:26:22.880Z'
verified: false
validated: true
submitted: true
---
# dir-verify-file-creation

## Command

```ruby
puts `dir C:\\Users\\rootx\\`
```

## Description

Executes the Windows dir command via Ruby backticks in IRB to list directory contents and verify the traversed file creation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| path | Target directory like "C:\\Users\\rootx\\" | Yes |

## Examples

### Basic Usage

```ruby
puts `dir C:\\Users\\rootx\\`
```

### Advanced Usage

```ruby
puts `dir /b C:\\Users\\rootx\\*.rb`
```

## Expected Output

Directory listing showing '21-03-2021 00:45 0 malicious20210321-22472-fvuodx.rb' among other files

## Related

- [[Related Procedure]]
