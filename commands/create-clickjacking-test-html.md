---
data: >-
  cat > index.html << EOF

  <!DOCTYPE html>

  <html>

  <body>

  <iframe sandbox="allow-scripts allow-forms"
  src="https://app.legalrobot-uat.com/pending-verification" width="1000"
  height="600"></iframe>

  </body>

  </html>

  EOF
tags:
  - html-creation
  - iframe-test
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:28:12.305Z'
id: 1ac8f745-32eb-4287-b353-ebf8f07bf5bb
verified: false
validated: true
submitted: true
---
# create-clickjacking-test-html

## Command

```bash
cat > index.html << EOF
<!DOCTYPE html>
<html>
<body>
<iframe sandbox="allow-scripts allow-forms" src="https://app.legalrobot-uat.com/pending-verification" width="1000" height="600"></iframe>
</body>
</html>
EOF
```

## Description

This command uses a bash heredoc to create an HTML file named `index.html` that embeds a target URL in an iframe, configured with sandbox attributes to allow scripts and forms for clickjacking testing. Use it to quickly generate a proof-of-concept page for verifying frameable vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `index.html` | Output filename for the HTML file | Yes |
| `sandbox="allow-scripts allow-forms"` | Iframe attribute to permit necessary interactions | Yes |
| `src="https://..."` | Target URL to embed | Yes |
| `width="1000" height="600"` | Iframe dimensions for visibility | No |

## Examples

### Basic Usage

```bash
cat > index.html << EOF
<!DOCTYPE html>
<html>
<body>
<iframe sandbox="allow-scripts allow-forms" src="https://app.legalrobot-uat.com/pending-verification" width="1000" height="600"></iframe>
</body>
</html>
EOF
```

### Advanced Usage

To target a different URL, modify the src:

```bash
cat > test.html << EOF
<!DOCTYPE html>
<html>
<body>
<iframe sandbox="allow-scripts allow-forms allow-same-origin" src="https://example.com/vulnerable" width="800" height="500"></iframe>
</body>
</html>
EOF
```

## Expected Output

The command runs silently if successful, creating `index.html` in the current directory. Verify with `cat index.html` to see the embedded iframe code. No stdout unless errors occur (e.g., permission denied).

## Related

- [[Related Procedure: Create-HTML-File-for-Clickjacking-Test]]
