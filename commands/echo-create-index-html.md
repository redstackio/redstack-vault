---
data: echo "hi" > index.html
tags:
  - file-creation
  - shell
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.710Z'
id: 74f62672-a605-450d-965a-bbe9b7b3ba07
verified: false
validated: true
submitted: true
---
# echo-create-index-html

## Command

```bash
echo "hi" > index.html
```

## Description

Creates a basic index.html file by echoing content to it, needed for server startup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `"hi"` | Content string to write | Yes |
| `> index.html` | Output redirection to file | Yes |

## Examples

### Basic Usage

```bash
echo "hi" > index.html
```

### Advanced Usage

```bash
echo '<html><body>Server ready</body></html>' > index.html
```

## Expected Output

No output; file created. Verify with cat index.html showing "hi".

## Related

- [[Related Procedure]]
