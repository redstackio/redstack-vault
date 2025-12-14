---
tags:
  - csrf
  - shopify
  - poc
  - invitation
  - wholesale
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:50.026Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e12006c1-8abe-4346-b909-ee2ea095213b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Execute CSRF to Generate Invitation Token

## Summary

This core procedure exploits the CSRF vulnerability in Shopify's Wholesale app by loading a malicious PoC webpage that forges an invitation request, generating a token and updating customer status without user consent.

## Description

The attack leverages the lack of CSRF protection on the invitation endpoint (e.g., /admin/shops/{shop_id}/accounts/{customer_id}/invite_link_modal_single). While the victim is authenticated in Shopify admin, they are tricked into visiting a PoC page (HTML or PHP) that auto-submits a forged POST request using the victim's session cookies. This invites the tagged customer unauthorizedly. Environment: Victim's browser with active Shopify session. Outcomes: Invitation token created, status changed to 'invited', potential for spam or access abuse.

## Requirements

1. Victim authenticated in Shopify admin
2. Tagged customer prepared from prior steps
3. Hosted PoC webpage (e.g., with customer ID parameter)

## Defense

Defensive measures and detection strategies:

- Enable CSRF tokens on all state-changing endpoints in the Wholesale app
- Monitor for anomalous invitation requests in Shopify logs, especially from non-admin sources
- Educate users on avoiding untrusted links while authenticated

## Objectives

1. Forge request to invitation endpoint via PoC
2. Generate unauthorized invite token
3. Change customer status to 'invited'

## Instructions

### Step 1: Prepare PoC Page

**Context**: Set up the malicious webpage to target the specific customer ID.

Use a PoC like http://poc.rhynorater.com/wholesaleShopify/CSRF.php?id={customer_id}, replacing {customer_id} with the target's ID from Shopify customers section. Host locally if needed using a simple HTTP server.

> Expected: PoC URL ready; test load in incognito to ensure no errors.

### Step 2: Lure Victim to PoC

**Context**: Ensure victim loads the page while their Shopify session is active to hijack cookies for the forged request.

Direct the victim (e.g., via phishing email or link) to the PoC URL. The page auto-triggers the CSRF request upon load.

> Expected: Page loads; browser sends POST to Shopify endpoint using victim's session.

### Step 3: Monitor Request Execution

**Context**: Allow time for the backend processing without user interaction.

Wait approximately 30 seconds for the request to process. Use browser dev tools (Network tab) to inspect the outgoing request if testing.

> Expected: No visible alerts; request completes silently.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[poc]]
- [[invitation-token]]
