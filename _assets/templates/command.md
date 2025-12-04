---
id: <% tp.system.uuid() %>
name: <% tp.file.title %>
type: command
executor: bash
data: |
  command --flag argument
output: null
created_at: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>Z
updated_at: <% tp.date.now("YYYY-MM-DDTHH:mm:ss") %>Z
platforms: []
tags: []
---

# <% tp.file.title %>

## Command

```bash
command --flag argument
```

## Description

Brief description of what this command does and when to use it.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--flag` | Description of flag | Yes/No |
| `argument` | Description of argument | Yes/No |

## Examples

### Basic Usage

```bash
command --flag value
```

### Advanced Usage

```bash
command --flag value --option2 value2
```

## Expected Output

Description of what output to expect when the command runs successfully.

## Related

- [[Related Command]]
- [[Related Procedure]]
