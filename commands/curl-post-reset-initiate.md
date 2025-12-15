---
data: >-
  curl -X POST https://shoppers.instacart.com/password -d "utf8=%E2%9C%93" -d
  "authenticity_token=extracted_token" -d "driver[email]=target@example.com" -d
  "commit=Reset+password" -b cookies.txt
tags:
  - web
  - auth
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:06.552Z'
id: cf49403d-0d60-4902-a526-fbbec5b5182d
verified: false
validated: true
submitted: true
---
# curl-post-reset-initiate

## Command

```bash
curl -X POST https://shoppers.instacart.com/password -d "utf8=%E2%9C%93" -d "authenticity_token=extracted_token" -d "driver[email]=target@example.com" -d "commit=Reset+password" -b cookies.txt
```

## Description

Initiates a password reset by submitting the target email to the Instacart endpoint, triggering an email with the reset token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d "utf8=%E2%9C%93"` | UTF-8 encoding flag | Yes |
| `-d "authenticity_token=..."` | Rails CSRF token | Yes |
| `-d "driver[email]=..."` | Target email | Yes |
| `-d "commit=..."` | Form submit button | Yes |
| `-b cookies.txt` | Loads session cookies | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://shoppers.instacart.com/password -d "utf8=%E2%9C%93" -d "authenticity_token=abc123" -d "driver[email]=test@example.com" -d "commit=Reset+password" -b cookies.txt
```

### Advanced Usage

```bash
curl -X POST https://shoppers.instacart.com/password -d ... -v  # Verbose for headers
```

## Expected Output

Success response like "Email sent" or redirect to confirmation page.

## Related

- [[commands/curl-get-password-page]]
