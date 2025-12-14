---
id: proc-uuid-1
tags:
  - shopify
  - app-creation
  - google-analytics
type: procedure
tools:
  - '[[tools/Google-Analytics]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:57.303Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Shopify-App-with-Google-Analytics-Embedding

## Summary

This procedure outlines creating a Shopify Partner app and embedding Google Analytics tracking code to capture full URLs, including sensitive query parameters like CSRF tokens, during victim redirects.

## Description

Attackers with a Shopify Partner account can create a new app via the dashboard, then edit the app listing to insert GA code. This code tracks page views and sends complete URLs to the attacker's GA account without filtering sensitive data, exploiting Shopify's post-login redirect behavior that appends authenticity_token as a query parameter.

## Requirements

1. Valid Shopify Partner account with app creation permissions
2. Google Analytics account and tracking ID
3. Web browser for dashboard access

## Defense

Defensive measures and detection strategies:

- Disable or sanitize third-party analytics in app listings
- Avoid exposing tokens in URL query parameters; use session storage or headers
- Monitor GA dashboards for anomalous traffic from partner apps

## Objectives

1. Establish a tracking mechanism in the app listing
2. Prepare for passive URL capture during victim interactions
3. Enable real-time exfiltration of sensitive data

## Instructions

### Step 1: Create New Shopify App

**Context**: Navigate to the Partner Dashboard to initiate app creation, providing basic details to generate an app ID.

No specific command; use browser to access https://app.shopify.com/services/partners/api_clients/new, fill in app name and details, and submit to create the app.

> Expected output: Confirmation page with app ID, e.g., apps.shopify.com/[app_id].

### Step 2: Edit App Listing to Embed GA Code

**Context**: Access the app listing edit page and insert the GA tracking script in the designated field to activate URL tracking.

No specific command; in the Shopify dashboard, go to the app's listing settings, locate the 'Google analytics code' field, and paste the GA script (e.g., <script async src="https://www.googletagmanager.com/gtag/js?id=GA_TRACKING_ID"></script> with configuration for full URL capture).

> Expected output: Updated app listing with GA integration; verify by viewing page source.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Analytics]]

## Tags

- shopify
- app-creation
- google-analytics
