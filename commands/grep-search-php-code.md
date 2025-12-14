---
id: cmd-uuid-001
data: grep -r "sitemap_select_mode" /path/to/concrete/src/
tags:
  - code-search
  - audit
type: command
output: >-
  File paths and line numbers with matches, e.g.,
  /concrete/tools/pages/search_dialog.php:47: $sitemap_select_mode in
  Loader::element call
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:14.623Z'
verified: false
validated: true
submitted: true
---
# grep-search-php-code

## Command

```bash
grep -r "sitemap_select_mode" /path/to/concrete/src/
```

## Description

This command recursively searches for the string 'sitemap_select_mode' in PHP source files to locate potential vulnerability points during code audits for XSS issues.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-r` | Recursive search in directories | Yes |
| `"sitemap_select_mode"` | Pattern to match (vulnerable parameter) | Yes |
| `/path/to/concrete/src/` | Directory to search | Yes |

## Examples

### Basic Usage

```bash
grep -r "sitemap_select_mode" /path/to/concrete/src/
```

### Advanced Usage

```bash
grep -r -n "sitemap_select_mode" /path/to/concrete/src/ | grep -i "echo\|output"
```

## Expected Output

List of matching lines with file:line format, highlighting unsanitized uses in functions like echo or Loader::element.

## Related

- [[Related Procedure: Locate-Vulnerability-Source-Using-Grep]]
