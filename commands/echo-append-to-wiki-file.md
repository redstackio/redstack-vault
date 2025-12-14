---
data: echo "Hi" >> home.md
tags:
  - echo
  - file-modify
  - markdown
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 12582816-cf87-4a74-9c5a-2a2e4fa608e5
created_at: '2025-12-13T23:52:55.048Z'
updated_at: '2025-12-13T23:52:55.048Z'
verified: false
validated: true
submitted: true
---
---

# echo-append-to-wiki-file

## Command

```bash
echo "Hi" >> home.md
```

## Description

Appends a simple string to a Markdown file in the wiki repo, creating a minimal change to trigger a commit with malicious metadata.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `"Hi"` | Text to append | Yes |
| `home.md` | Target wiki page file | Yes |
| `>>` | Append operator (use > to overwrite) | Yes |

## Examples

### Basic Usage

```bash
echo "Hi" >> home.md
```

### Advanced Usage

```bash
echo "# New Page\nContent here" > new-page.md
```

## Expected Output

No stdout; file updated. Check with `ls -l home.md` for size change.

## Related

- [[Related Procedure: Modify Wiki Page Content]]
