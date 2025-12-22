---
id: cmd-uuid-9012
data: 'curl https://hackerone.com/assets/application.css -o application.css'
tags:
  - reconnaissance
  - information-gathering
type: command
output: >-
  Downloaded CSS file content to application.css (text/css, unminified with
  comments and source maps)
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:08.029Z'
verified: false
validated: true
submitted: true
---
# curl-retrieve-css

## Command

```bash
curl https://hackerone.com/assets/application.css -o application.css
```

## Description

This command uses curl to fetch a publicly exposed CSS file from a target website and save it locally for inspection. It is useful for reconnaissance to identify misconfigurations where development artifacts are leaked in uncompiled files.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | The full URL of the CSS file to retrieve | Yes |
| -o | Output file name to save the response | Yes |

## Examples

### Basic Usage

```bash
curl https://example.com/assets/application.css -o app.css
```

### Advanced Usage

```bash
curl -s https://hackerone.com/assets/application.css -o application.css | grep -i "comment"
```

> The -s flag silences progress output, and piping to grep searches for comments inline.

## Expected Output

The command downloads the raw CSS content to the specified file. Successful execution shows no errors and a file size greater than 0 bytes. Inspect the file for unminified code, SASS variables, or source maps to confirm disclosure.

## Related

- [[Related Procedure|Inspect-Exposed-CSS-Files-for-Internal-Information]]
