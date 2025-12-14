---
data: rdoc --all
tags:
  - documentation
  - xss
  - rdoc
type: command
output: null
executor: bash
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:12.927Z'
id: 8d220964-6f54-450f-835f-197fd231383a
verified: false
validated: true
submitted: true
---
# rdoc-generate-documentation

## Command

```bash
rdoc --all
```

## Description

This command generates HTML documentation from Ruby source files using RDoc, processing comments into formatted output. In vulnerable versions, it enables stored XSS by failing to escape HTML in paragraph text.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--all` | Processes all Ruby files in the current directory and subdirectories | Yes |

## Examples

### Basic Usage

```bash
rdoc --all
```

Generates docs for all .rb files.

### Advanced Usage

```bash
rdoc --all --output doc --main example.rb
```

Specifies output dir and main file.

## Expected Output

Creates a 'doc' directory with HTML files, e.g., 'doc/example.html' containing unescaped content like `<p>x\[<script>alert(1);</script>\]</p>` if payload injected.

## Related

- [[procedures/Exploit-Stored-XSS-in-RDoc]]
