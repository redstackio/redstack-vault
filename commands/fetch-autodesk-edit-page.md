---
data: >-
  curl -v -H "Cookie: your_session_cookie"
  "https://profile.autodesk.com/edit-photo?id=your_user_id"
tags:
  - web
  - recon
type: command
output: null
executor: bash
platforms:
  - Web
id: cbb20206-4f13-4287-b1b3-d84e33ea0ce2
created_at: '2025-12-14T17:30:27.244Z'
updated_at: '2025-12-14T17:30:27.244Z'
verified: false
validated: true
submitted: true
---
# Fetch Autodesk Edit Photo Page

## Command

```bash
curl -v -H "Cookie: your_session_cookie" "https://profile.autodesk.com/edit-photo?id=your_user_id"
```

## Description

This command retrieves the photo edit page for an Autodesk user profile, allowing inspection of the form and 'id' parameter structure. It requires an active session and is used to baseline the vulnerable endpoint before manipulation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output for request/response details | No |
| `-H "Cookie: ..."` | Session cookie for authentication | Yes |
| `id=...` | User profile ID in URL query | Yes |

## Examples

### Basic Usage

```bash
curl -v -H "Cookie: session=abc123" "https://profile.autodesk.com/edit-photo?id=123"
```

### Advanced Usage

```bash
curl -v -H "Cookie: session=abc123" -H "User-Agent: Mozilla/5.0" "https://profile.autodesk.com/edit-photo?id=123"
```

## Expected Output

Verbose logs showing GET request headers, followed by HTTP 200 response with HTML containing the photo upload form. Errors like 401 indicate invalid session.

## Related

- [[commands/update-autodesk-profile-photo]]
