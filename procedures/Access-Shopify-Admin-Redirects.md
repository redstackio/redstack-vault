---
id: proc-access-shopify-redirects-001
tags:
  - shopify
  - admin-access
  - redirects
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:15:52.896Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Shopify-Admin-Redirects

## Summary

This procedure outlines logging into the Shopify admin panel and navigating to the URL redirects management page, a prerequisite for exploiting vulnerabilities in the redirect creation feature.

## Description

In a Shopify store environment, administrators can manage URL redirects via the admin interface. This step requires valid admin credentials to access the protected area at https://[shop-name].myshopify.com/admin/redirects. It sets the stage for injecting malicious payloads into redirect URLs, exploiting the lack of scheme validation. Expected outcomes include successful page load, confirming access to the feature.

## Requirements

1. Valid Shopify store administrator credentials
2. Web browser with JavaScript enabled
3. Direct internet access to the Shopify domain

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls (RBAC) to limit redirect management to trusted admins
- Monitor admin login events for anomalous IP locations or times
- Use web application firewalls (WAF) to log access to sensitive admin endpoints

## Objectives

1. Establish authenticated session in the admin panel
2. Reach the URL redirects interface
3. Verify permissions for creating redirects

## Instructions

### Step 1: Log In to Admin Panel

**Context**: Authenticate to gain admin privileges.

Navigate to https://[shop-name].myshopify.com/admin and enter credentials.

> Successful login redirects to the dashboard.

### Step 2: Navigate to Redirects Page

**Context**: Access the specific feature for URL management.

From the dashboard, go to Online Store > Navigation > URL Redirects, or directly visit https://[shop-name].myshopify.com/admin/redirects.

> The page loads with a list of existing redirects and an 'Add URL Redirect' button.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[admin-access]]
