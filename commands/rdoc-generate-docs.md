---
data: rdoc --all
tags:
  - xss
  - generation
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:53.388Z'
id: baa11fca-ea96-409d-b3a0-ac4e62d1fe64
verified: false
validated: true
submitted: true
---
# rdoc-generate-docs

## Command

```bash
rdoc --all
```

## Description

Generates HTML documentation for a Ruby project using RDoc, embedding unescaped filenames into output.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --all | Forces generation for all files, including malicious ones | Yes |

## Examples

### Basic Usage

```bash
rdoc --all
```

### Advanced Usage

```bash
rdoc --all --output doc/
``` (specify output dir)

## Expected Output

Creates doc/ directory with index.html containing injected XSS payload.

## Related

- [[procedures/Generate-RDoc-HTML-with-Embedded-Payload]]
- [[commands/ls-list-files]]
