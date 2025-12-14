---
id: proc-uuid-1
tags:
  - recon
  - shopify
  - web
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
updated_at: '2025-12-13T23:52:55.665Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Navigate-to-Shopify-Storefront

## Summary

This procedure establishes initial access to a target Shopify storefront by navigating to its public URL, serving as the entry point for subsequent vulnerability assessment in a reflected XSS attack chain.

## Description

In the context of exploiting Shopify's theme preview XSS, this step involves accessing the unauthenticated storefront at <store>.myshopify.com. No special tools or credentials are required, making it accessible for reconnaissance. The expected outcome is a fully loaded page ready for source inspection, setting the stage for theme ID extraction.

## Requirements

1. Web browser with internet access
2. Knowledge of the target store's subdomain (e.g., echo.myshopify.com)
3. No authentication or special permissions needed

## Defense

Defensive measures and detection strategies:

- Implement web application firewalls (WAF) to monitor unusual storefront access patterns
- Log and alert on rapid page source inspections via browser developer tools

## Objectives

1. Gain visibility into the live storefront environment
2. Confirm the target is a valid Shopify-hosted site
3. Prepare for client-side code analysis

## Instructions

### Step 1: Launch Browser and Navigate

**Context**: Open a standard web browser to access the public-facing storefront without any prior setup.

Instructions: Enter the URL https://<store-name>.myshopify.com in the address bar and press Enter. Replace <store-name> with the actual store identifier.

> The page should load the shop's homepage, displaying products and theme elements. If it fails, verify the store name and internet connectivity.

### Step 2: Verify Page Load

**Context**: Ensure the storefront is operational and under the myshopify.com domain to confirm the target environment.

Instructions: Check the browser's address bar for the correct domain and observe that no errors or redirects occur.

> Successful load indicates the site is active; proceed to source inspection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[shopify]]
- [[web]]
