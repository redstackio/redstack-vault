---
type: command
executor: bash
data: 'grep -i -o ''<a[^>]*target=[\"'''']_blank[\"''''][^>]*>'' file.html'
output: null
created_at: '2023-04-06T03:56:40Z'
updated_at: '2023-04-06T03:56:40Z'
platforms:
  - Linux
  - macOS
tags:
  - search
  - html
  - detection
verified: true
validated: true
---

# grep-search-html-target-blank-links

## Command

```bash
grep -i -o '<a[^>]*target="_blank"[^>]*>' file.html
```

## Description

This command searches an HTML file for anchor tags containing the `target="_blank"` attribute, which opens links in a new tab or window. It is used in phishing detection workflows to identify links that could facilitate Tabnabbing attacks by allowing potential manipulation of the parent window.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `file.html` | Path to the HTML file or log to search | Yes |
| `-i` | Perform case-insensitive matching | No (recommended for robustness) |
| `-o` | Show only the matching part of each line | Yes |
| `<a[^>]*target=[\"'']_blank[\"''][^>]*>` | Regex pattern matching opening `<a>` tags with `target="_blank"` or `target='_blank'` | Built-in |

## Examples

### Basic Usage

```bash
grep -i -o '<a[^>]*target="_blank"[^>]*>' page.html
```

Outputs matching `<a>` tags from `page.html`.

### Advanced Usage

```bash
grep -i -o '<a[^>]*target="_blank"[^>]*>' logs.txt | head -10
```

Limits output to the first 10 matches from a log file.

## Expected Output

Matching lines like:

`<a href="https://example.com" target="_blank">Click here</a>`

If no matches, no output is produced, indicating no such links found.

## Related

- [[procedures/Hunt-for-Tabnabbing-Enabling-Links]]
