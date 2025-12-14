---
id: cmd-curl-get-drafts
data: >-
  curl -c cookies.txt -b cookies.txt -X GET
  "https://apps.topcoder.com/wiki/users/viewmydrafts.action" -H "Cookie:
  JSESSIONID=your_session"
tags:
  - recon
  - http
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:33.578Z'
verified: false
validated: true
submitted: true
---
# curl-get-drafts

## Command

```bash
curl -c cookies.txt -b cookies.txt -X GET "https://apps.topcoder.com/wiki/users/viewmydrafts.action" -H "Cookie: JSESSIONID=your_session"
```

## Description

Retrieves the user's drafts page from the TopCoder wiki, using cookie-based authentication to maintain session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-c cookies.txt` | Saves cookies to file | Yes |
| `-b cookies.txt` | Loads cookies from file | Yes |
| `-X GET` | HTTP method | Yes |
| `JSESSIONID=your_session` | Session cookie value | Yes |

## Examples

### Basic Usage

```bash
curl -c cookies.txt -b cookies.txt -X GET "https://apps.topcoder.com/wiki/users/viewmydrafts.action" -H "Cookie: JSESSIONID=your_session"
```

### Advanced Usage

Add verbose output:

```bash
curl -v -c cookies.txt -b cookies.txt -X GET "https://apps.topcoder.com/wiki/users/viewmydrafts.action" -H "Cookie: JSESSIONID=your_session"
```

## Expected Output

HTML response containing the list of drafts, including draft IDs in links or forms.

## Related

- [[Related Procedure]]
