---
data: |-
  {
    me{
      _id #388246
      id #gid://hackerone/User/388246
      otp_backup_codes
      username
    }
  }
tags:
  - graphql
  - self-query
type: command
executor: graphql
platforms:
  - Web
id: 93ad43a8-6d8c-41fb-af7b-71dc8c08e9df
created_at: '2025-12-11T06:10:40.201Z'
updated_at: '2025-12-11T06:10:40.201Z'
verified: false
validated: true
submitted: true
---
# graphql-self-otp-query

## Command

```graphql
{
  me{
    _id #388246
    id #gid://hackerone/User/388246
    otp_backup_codes
    username
  }
}
```

## Description

GraphQL query for a user to retrieve their own OTP backup codes hashes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `me` | Current user object | Yes |
| `otp_backup_codes` | Hashed OTP backup codes | No |

## Examples

### Basic Usage

```graphql
{
  me {
    otp_backup_codes
  }
}
```

## Expected Output

User's own hashed OTP backup codes.

## Related

- [[commands/graphql-user-data-leak-query]]
- [[procedures/Access-Own-OTP-Backup-Codes-via-GraphQL-Query]]
