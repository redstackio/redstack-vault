---
id: cmd-curl-get-fpd-001
data: >-
  curl -X GET "http://www.localize.io/pages/create_project/72" -o
  project_form.html
tags:
  - recon
  - web
  - http
type: command
output: HTML response saved to project_form.html containing form and CSRF token.
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.224Z'
verified: false
validated: true
submitted: true
---
# curl-get-project-creation

## Command

```bash
curl -X GET "http://www.localize.io/pages/create_project/72" -o project_form.html
```

## Description

This command performs a GET request to the project creation page of www.localize.io to retrieve the HTML form, which includes the CSRF token needed for the subsequent POST request. Use it as the initial step in exploiting the FPD vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| URL | Target endpoint with project ID (e.g., /pages/create_project/72) | Yes |
| `-o project_form.html` | Saves the response to a file for inspection | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "http://www.localize.io/pages/create_project/72" -o project_form.html
```

### Advanced Usage

```bash
curl -X GET "http://www.localize.io/pages/create_project/72" -H "User-Agent: Mozilla/5.0" -o project_form.html
```

## Expected Output

The command outputs the HTML content to project_form.html. Successful execution returns HTTP 200 and includes form fields like <input name="CSRFToken" value="...">. Errors may show 404 if the project ID is invalid.

## Related

- [[commands/curl-post-fpd-trigger]]
- [[procedures/Trigger-FPD-with-Array-Parameter-Manipulation]]
