---
id: proc-woocommerce-api-key
tags:
  - api
  - woocommerce
  - credentials
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/create-woocommerce-api-key]]'
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:16:14.206Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create WooCommerce API Key with Read/Write Permissions

## Summary

This procedure generates a WooCommerce REST API key with Read/Write permissions, which can inherit advanced capabilities like unfiltered_html if the generating user has them, enabling subsequent malicious uploads.

## Description

In a WordPress site with WooCommerce, API keys are created via the admin interface or WP-CLI. The key provides access to endpoints like product creation, including image uploads from URLs. Without proper permission scoping, this grants attackers the ability to upload files if they compromise or own an admin account. The procedure assumes access to the WordPress backend and targets sites where unfiltered_html is enabled for the user role.

## Requirements

1. Administrative access to WordPress dashboard or WP-CLI
2. WooCommerce plugin installed and REST API enabled
3. User role with permission to generate API keys (e.g., admin)

## Defense

Defensive measures and detection strategies:

- Restrict API key generation to minimal permissions; audit keys regularly
- Disable unfiltered_html for non-super admins via WordPress roles
- Monitor API key creation logs and usage in WooCommerce settings

## Objectives

1. Obtain API credentials for Read/Write access to WooCommerce endpoints
2. Ensure inheritance of unfiltered_html for payload execution
3. Prepare for file upload exploitation

## Instructions

### Step 1: Access WooCommerce Settings

**Context**: Log in to WordPress admin and navigate to WooCommerce > Settings > Advanced > REST API to create a new key.

**Command** ([[commands/create-woocommerce-api-key]]):
```bash
# Use WP-CLI if available; otherwise, manual UI
wp woocommerce key generate --user=1 --permissions=read_write --description="Attacker Key" --user-friendly-name="Test"
```

> This command outputs the consumer key and secret. In the UI, select Read/Write and generate. Expected output: Key pair like ck_abc123 and cs_def456. Success if key is listed in API keys table.

### Step 2: Verify Key Permissions

**Context**: Test the key against a read endpoint to confirm access.

**Command** ([[commands/test-api-key]]):
```bash
curl -u "ck_abc123:cs_def456" "https://target.com/wp-json/wc/v3/products"
```

> Returns JSON list of products if successful, confirming Read access. For Write, attempt a simple POST.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/create-woocommerce-api-key]]
- [[commands/test-api-key]]

## Tools Used


## Tags

- [[api]]
- [[woocommerce]]
- [[Credentials]]
