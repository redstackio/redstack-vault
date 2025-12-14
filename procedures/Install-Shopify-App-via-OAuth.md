---
tags:
  - shopify
  - oauth
  - app-installation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/shopify-oauth-authorize]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:45.018Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: bce51c15-5907-4ab3-a77d-eec1116e5bb7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-Shopify-App-via-OAuth

## Summary

This procedure installs the pre-created Shopify app with the malformed callback URL onto a target store via OAuth, triggering a failed redirect that corrupts the app management functionality.

## Description

After creating the app, construct an OAuth authorization URL using the app's client_id and a scope like read_customers. Visiting this URL on the target store (e.g., https://vulnstore.myshopify.com) prompts a permission dialog. Approving installation proceeds but the post-install redirect to the invalid 'shit:google.com' fails silently, leaving the app in a broken state that affects the /admin/apps endpoint. This requires admin access to the target store for testing.

## Requirements

1. Client_id from the created app
2. Target Shopify store URL (e.g., vulnstore.myshopify.com)
3. Admin access to the target store for installation
4. Web browser

## Defense

Defensive measures and detection strategies:

- Validate redirect_uris during OAuth callbacks server-side
- Log and alert on OAuth installations with non-standard URIs
- Implement app uninstall safeguards for failed redirects

## Objectives

1. Initiate OAuth flow to install the malicious app
2. Trigger redirect failure to induce DoS state
3. Confirm app is installed but unmanageable

## Instructions

### Step 1: Construct OAuth URL

**Context**: Build the authorization endpoint URL with required parameters.

**Instructions**: Use the format https://{store}.myshopify.com/admin/oauth/authorize?scope={scope}&client_id={client_id}. For example, scope=read_customers and client_id=cad94488c733b0f377a9a1d7952db802.

### Step 2: Visit and Approve Installation

**Context**: Execute the OAuth flow to install the app.

**Command** ([[commands/shopify-oauth-authorize]]):
Visit the constructed URL in a browser.

> The permission dialog will appear. Click 'Install App' to approve. Installation completes, but no redirect happens due to the malformed URI.

**Expected Output**: Dialog shows requested scopes; after approval, page may hang or error without redirecting.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/shopify-oauth-authorize]]

## Tools Used


## Tags

- shopify
- oauth
- app-installation
