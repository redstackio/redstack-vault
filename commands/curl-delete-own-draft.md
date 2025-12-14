---
id: cmd-curl-delete-own
data: >-
  curl -c cookies.txt -b cookies.txt -X GET
  "https://apps.topcoder.com/wiki/users/viewmydrafts.action?discardDraftId=YOUR_OWN_DRAFT_ID"
  -H "Cookie: JSESSIONID=your_session"
tags:
  - testing
  - http
  - deletion
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:33.577Z'
verified: false
validated: true
submitted: true
---
# curl-delete-own-draft

## Command

```bash
curl -c cookies.txt -b cookies.txt -X GET "https://apps.topcoder.com/wiki/users/viewmydrafts.action?discardDraftId=YOUR_OWN_DRAFT_ID" -H "Cookie: JSESSIONID=your_session"
```

## Description

Tests deletion of an owned draft by passing the draft ID as a GET parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `discardDraftId=YOUR_OWN_DRAFT_ID` | ID of the draft to delete | Yes |
| Other flags as in base curl | Authentication and method | Yes |

## Examples

### Basic Usage

Replace YOUR_OWN_DRAFT_ID with actual ID.

## Expected Output

Redirect to drafts page or success message; draft removed.

## Related

- [[Related Procedure]]
