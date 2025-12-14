---
tags:
  - app-creation
  - oauth
  - shopify
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-visit-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:35.506Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: f2a0ac45-ff3d-4739-b8fd-cd4c7b032833
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Shopify-App-with-Custom-Redirect

## Summary

This procedure registers a custom app on Shopify's developer platform, configuring a redirect URI to an external attacker-controlled site, setting the stage for OAuth exploitation.

## Description

In the context of Shopify's OAuth flow, attackers create a test app via the Shopify partners dashboard. The app is assigned a client ID, and the redirect URI is set to an arbitrary external domain (e.g., a phishing page on Facebook). This step is prerequisite for testing the open redirection vulnerability, as it provides the necessary app credentials. The target environment is Shopify's web-based app management, requiring a developer account. Expected outcome: App ready for OAuth authorization testing, enabling subsequent redirection bypass.

## Requirements

1. Shopify partner/developer account with app creation permissions
2. Access to an external domain for redirect URI (e.g., http://www.facebook.com/abc/ for testing)
3. Web browser for Shopify dashboard navigation

## Defense

Defensive measures and detection strategies:

- Monitor app creation logs for suspicious redirect URIs pointing to external domains
- Implement rate limiting on app registrations from new accounts
- Require manual review for apps with non-Shopify redirect URIs

## Objectives

1. Establish a malicious app with external redirect capability
2. Obtain client ID for OAuth URL construction
3. Prepare for scope-based validation bypass

## Instructions

### Step 1: Access Shopify App Creation

**Context**: Log into the Shopify partners dashboard and navigate to create a new app.

**Command** ([[commands/curl-visit-url]]):
```bash
curl -c cookies.txt "https://partners.shopify.com/signup" # Simulate login if automated, but manual browser recommended
```

> This command sets up session cookies; in practice, use a browser to complete registration and app setup with client_id=616ce3efcd495007438000ad958a6629 and redirect_uri=http://www.facebook.com/abc/. Expected output: Confirmation page with app details.

### Step 2: Configure App Details

**Context**: Set the redirect URI during app configuration to point to the phishing target.

No direct command; manual input in dashboard form.

> Verify configuration by reviewing app settings. Expected output: App saved with custom redirect URI.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-visit-url]]

## Tools Used


## Tags

- app-creation
- oauth
- shopify
