---
data: |-
  cat > test-iframe.html << EOF
  <!DOCTYPE html>
  <html>
  <head>
      <title>Clickjacking Test</title>
  </head>
  <body>
      <h1>Testing iframe embedding</h1>
      <iframe src="https://love.uber.com" width="800" height="600"></iframe>
  </body>
  </html>
  EOF
tags:
  - web-testing
  - clickjacking
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows (WSL)
id: a1901947-b595-4802-9fe1-2ac6852eacc8
created_at: '2025-12-14T17:28:04.676Z'
updated_at: '2025-12-14T17:28:04.676Z'
verified: false
validated: true
submitted: true
---
# create-iframe-test-html

## Command

```bash
cat > test-iframe.html << EOF
<!DOCTYPE html>
<html>
<head>
    <title>Clickjacking Test</title>
</head>
<body>
    <h1>Testing iframe embedding</h1>
    <iframe src="https://love.uber.com" width="800" height="600"></iframe>
</body>
</html>
EOF
```

## Description

This command creates a basic HTML file for testing iframe embedding of a target site, such as love.uber.com, to detect clickjacking vulnerabilities by checking if the site loads without X-Frame-Options restrictions. Use it in reconnaissance or vulnerability assessment phases.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `test-iframe.html` | Output filename for the HTML test file | Yes |
| `src="https://love.uber.com"` | Target URL to embed in iframe (customize as needed) | Yes |
| `width="800" height="600"` | Iframe dimensions (adjust for visibility) | No |

## Examples

### Basic Usage

```bash
cat > test-iframe.html << EOF
<!DOCTYPE html>
<html>
<head><title>Test</title></head>
<body>
<iframe src="https://love.uber.com" width="800" height="600"></iframe>
</body>
</html>
EOF
```

### Advanced Usage

```bash
cat > enhanced-test.html << EOF
<!DOCTYPE html>
<html>
<head>
    <title>Enhanced Test</title>
    <style>.overlay {position: absolute; background: transparent;}</style>
</head>
<body>
<iframe src="https://example.com"></iframe>
<div class="overlay">Overlay content</div>
</body>
</html>
EOF
```

## Expected Output

The command outputs nothing to stdout but creates the specified HTML file. Verify with `ls test-iframe.html` or `cat test-iframe.html`. Open in a browser to see the embedded site if vulnerable.

## Related

- [[Related Procedure: Test-Clickjacking-by-Embedding-in-Iframe]]
