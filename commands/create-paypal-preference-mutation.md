---
data: >-
  curl -X POST 'https://hackerone.com/graphql?' -H 'Content-Type:
  application/json' -H 'X-Auth-Token: [TOKEN]' -H 'Cookie: [COOKIES]' -d
  '{"query":"mutation
  Create_paypal_preference_mutation($input_0:CreatePaypalPreferenceInput!,$first_1:Int!)
  {createPaypalPreference(input:$input_0) {clientMutationId,...F7,...F8}}
  ...","variables":{"input_0":{"paypal_email":"test@example.com","default_method":true,"clientMutationId":"0"},"first_1":100}}'
tags:
  - graphql
  - mutation
  - payment
type: command
output: JSON response with success status and updated user payout preferences
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.381Z'
id: f50cbadb-ae30-4cb8-a9f0-6993f4ddb11e
verified: false
validated: true
submitted: true
---
# create-paypal-preference-mutation

## Command

```bash
curl -X POST 'https://hackerone.com/graphql?' -H 'Content-Type: application/json' -H 'X-Auth-Token: [TOKEN]' -H 'Cookie: [COOKIES]' -d '{"query":"mutation Create_paypal_preference_mutation($input_0:CreatePaypalPreferenceInput!,$first_1:Int!) {createPaypalPreference(input:$input_0) {clientMutationId,...F7,...F8}} ...","variables":{"input_0":{"paypal_email":"test@example.com","default_method":true,"clientMutationId":"0"},"first_1":100}}'
```

## Description

GraphQL mutation to add a PayPal payout preference to the user's account.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| paypal_email | Email for PayPal | Yes |
| default_method | Set as default | Yes |
| clientMutationId | Mutation ID | Yes |
| first_1 | Errors to fetch | Yes |

## Examples

### Basic Usage

```bash
curl ... -d '{"variables":{"input_0":{"paypal_email":"attacker@evil.com",...}}}'
```

## Expected Output

JSON response with success status and updated user payout preferences

## Related

- [[procedures/Perform-Payment-Method-Mutation]]
