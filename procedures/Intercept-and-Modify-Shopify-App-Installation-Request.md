---
tags:
  - open-redirect
  - intercept
  - modification
  - shopify
  - oauth
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:35.524Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: a88458b9-74a8-4b41-a9e2-dc03bdeaa2cb
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Modify-Shopify-App-Installation-Request

## Summary

This procedure intercepts the HTTP POST request during Shopify app installation on development stores and modifies the store selection parameter to an arbitrary domain, exploiting an open redirection vulnerability in the OAuth flow to enable phishing or unauthorized installations.

## Description

In Shopify's Partners dashboard, the app installation process sends a POST request to install the app on a selected development store. The 'install_app[Select a store]' parameter is not validated server-side, allowing attackers with a partner account to alter it to any store domain. This results in a redirect to the target store's OAuth endpoint, which can be weaponized for phishing by sharing the link with victims. The attack requires intercepting the request using a proxy tool like Burp Suite and relies on social engineering to deliver the link. Expected outcomes include victim redirection to malicious flows, potential app approvals, or credential exposure.

## Requirements

1. Valid Shopify partner account with access to the dashboard
2. Ownership of at least one development store for initial setup
3. Burp Suite or similar proxy tool configured to intercept traffic from the browser
4. Network access to proxy requests to partners.shopify.com

## Defense

Defensive measures and detection strategies:

- Implement server-side validation of store domains in installation parameters, restricting to authorized stores only
- Monitor for anomalous POST requests to /apps/*/install_on_dev_shop with mismatched store IDs
- Educate users on verifying app installation links and OAuth prompts
- Use web application firewalls (WAF) to detect parameter tampering in OAuth flows

## Objectives

1. Bypass store selection validation to target arbitrary development stores
2. Craft redirect URLs for phishing or unauthorized app installations
3. Redirect victims to controlled OAuth endpoints for credential harvesting

## Instructions

### Step 1: Configure Proxy Interception

**Context**: Set up Burp Suite to capture the app installation request from the Partners dashboard.

**Instructions**: Launch Burp Suite, configure your browser to use it as a proxy (e.g., via FoxyProxy extension), and ensure HTTPS interception is enabled for partners.shopify.com.

### Step 2: Initiate Legitimate Installation Flow

**Context**: Trigger the POST request by starting an app installation on your own store.

**Instructions**: In the dashboard, create or select an app, click "Test your app," and choose your development store to submit the form.

### Step 3: Intercept and Modify Request

**Context**: Alter the store parameter to an arbitrary victim store domain.

**Instructions**: In Burp's Proxy > Intercept tab, catch the POST to /526915/apps/2544979/install_on_dev_shop (adjust IDs as needed). Edit the body: change install_app[Select a store] from e.g., "mido-2.myshopify.com" to "victim-store.myshopify.com". Preserve other parameters like utf8=✓, authenticity_token=..., and headers (Host: partners.shopify.com, Content-Type: application/x-www-form-urlencoded). Forward the request.

### Step 4: Verify and Extract Response

**Context**: Confirm the server accepts the modification and capture the redirect.

**Instructions**: Observe the 302 response in Burp's Repeater or Inspector. Note the Location header with the arbitrary store's OAuth URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- open-redirect
- shopify
- oauth
- phishing
