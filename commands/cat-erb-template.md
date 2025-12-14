---
data: cat app/views/books/show.text.erb
tags:
  - inspection
type: command
output: 'name: <% `touch me` %>'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.352Z'
id: 13cad560-82db-4494-b0e6-ed7d45189230
verified: false
validated: true
submitted: true
---
# cat-erb-template

## Command

```bash
cat app/views/books/show.text.erb
```

## Description

Inspects the overwritten ERB template.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| app/views/books/show.text.erb | File path | Yes |

## Examples

### Basic Usage

```bash
cat app/views/books/show.text.erb
```

## Expected Output

Malicious ERB content.

## Related

- [[commands/curl-traversal-erb-overwrite]]
