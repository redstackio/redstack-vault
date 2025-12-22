---
tags:
  - xss
  - trigger
  - exfiltration
  - csrf
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/shopify-xss-payload-injection]]'
  - '[[commands/external-php-csrf-extractor]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 747e39e9-01fd-450b-b72b-9cebb99cd975
created_at: '2025-12-14T17:30:18.185Z'
updated_at: '2025-12-14T17:30:18.185Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-in-Email-App-Template

## Summary

This procedure triggers the stored XSS by rendering an Email App template that includes the vulnerable store address field, executing JavaScript to exfiltrate CSRF tokens via an external server.

## Description

Upon template selection, the app unsafely renders the apartment field, firing the onerror event. The payload posts page HTML to the external server, which parses it with DOM and XPath to extract the CSRF token from <meta name='csrf-token'>, then returns eval-able JS to alert it. This allows unauthorized access to GraphQL endpoints.

## Requirements

1. Installed Email App with injected payload.
2. External server running the PHP extractor.
3. Template that displays store address.

## Defense

Defensive measures and detection strategies:

- Escape HTML in template rendering.
- Monitor outbound requests from app context.
- Implement strict CSP in iframes/apps.

## Objectives

1. Execute arbitrary JS in app context.
2. Steal sensitive data like CSRF tokens.
3. Enable follow-on attacks like unauthorized API calls.

## Instructions

### Step 1: Open Template Editor

**Context**: Access the app's template management.

**Command** (Manual Browser Action):

In Shopify dashboard, open Email App > Templates.

> Expected output: Template list loads.

### Step 2: Select Vulnerable Template

**Context**: Choose a template rendering the store address to trigger XSS.

**Command** (Manual Browser Action):

Select and edit a template including apartment field.

> The [[commands/shopify-xss-payload-injection]] executes: onerror sends head HTML to https://fbs.ninja, processed by [[commands/external-php-csrf-extractor]]. Expected output: After 2000ms, alert shows CSRF token.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/shopify-xss-payload-injection]]
- [[commands/external-php-csrf-extractor]]

## Tools Used


## Tags

- [[xss]]
- [[trigger]]
- [[Exfiltration]]
- [[csrf]]
