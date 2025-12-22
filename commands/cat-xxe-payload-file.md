---
data: cat foo
tags:
  - xxe
  - payload
type: command
output: Outputs the XXE payload content
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:07.961Z'
id: 6d71c75e-afef-4c31-8b26-8ade452ef41a
verified: false
validated: true
submitted: true
---
# cat-xxe-payload-file

## Command

```bash
cat foo
```

## Description

Displays the contents of the file 'foo' which contains a test XXE payload used to verify the vulnerability in XML parsing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| foo | File containing XXE payload | Yes |

## Examples

### Basic Usage

```bash
cat foo
```

### Advanced Usage

N/A

## Expected Output

The exact XML content: <!DOCTYPE a PUBLIC "-//B/A/EN" "HELLO_XXE"><a></a>

## Related

- [[commands/curl-post-xxe-test]]
