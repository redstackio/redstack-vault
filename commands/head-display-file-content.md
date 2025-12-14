---
id: cmd-head-001
data: head lorem-1MB
tags:
  - file-inspect
type: command
output: >-
  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor
  incididunt ut labore et dolore magna aliqua.
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.387Z'
verified: false
validated: true
submitted: true
---
# head-display-file-content

## Command

```bash
head lorem-1MB
```

## Description

Displays the first 10 lines of the 1MB gibberish file to confirm content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `lorem-1MB` | Input file | Yes |

## Examples

### Basic Usage

```bash
head filename.txt
```

### Advanced Usage

```bash
head -n 5 filename.txt
```

## Expected Output

First 10 lines of lorem ipsum text.

## Related

- [[Related Command: ls-list-files]]
