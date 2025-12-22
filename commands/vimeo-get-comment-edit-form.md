---
data: >-
  curl -X GET
  "https://vimeo.com/forums/wanted_and_offered/topic:130606?comment_id=13010973&is_sticky=0&action=comment_edit_form"
  -H "X-Requested-With: XMLHttpRequest" -H "Referer:
  https://vimeo.com/forums/wanted_and_offered/topic:130606" -H "Cookie:
  [auth_cookies]"
tags:
  - get
  - edit-form
  - vimeo
type: command
output: HTML edit form for the comment
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:23.412Z'
id: b632e41e-e9ed-4a71-8aac-c7d1f8de7374
verified: false
validated: true
submitted: true
---
# vimeo-get-comment-edit-form

## Command

```bash
curl -X GET "https://vimeo.com/forums/wanted_and_offered/topic:130606?comment_id=13010973&is_sticky=0&action=comment_edit_form" \
  -H "X-Requested-With: XMLHttpRequest" \
  -H "Referer: https://vimeo.com/forums/wanted_and_offered/topic:130606" \
  -H "Cookie: [insert full authentication cookies]"
```

## Description

This command retrieves the edit form for a specific Vimeo forum comment using a GET request, simulating the AJAX call triggered by the UI edit button. Use it to load the legitimate edit interface.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| comment_id | ID of the comment to edit (e.g., 13010973) | Yes |
| is_sticky | Sticky flag (usually 0) | No |
| action | Set to comment_edit_form | Yes |
| Cookie | Full session cookies for authentication | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://vimeo.com/forums/wanted_and_offered/topic:130606?comment_id=13010973&is_sticky=0&action=comment_edit_form" -H "X-Requested-With: XMLHttpRequest" -H "Cookie: [cookies]"
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X GET "https://vimeo.com/forums/wanted_and_offered/topic:130606?comment_id=13010973&is_sticky=0&action=comment_edit_form" -H "X-Requested-With: XMLHttpRequest" -H "Cookie: [cookies]"
```

## Expected Output

HTML response containing the editable comment form, including textarea with current text and hidden fields like token.

## Related

- [[commands/vimeo-get-modified-comment-edit-form]]
- [[procedures/Load-Vimeo-Comment-Edit-Form]]
