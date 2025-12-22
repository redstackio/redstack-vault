---
id: proc-trigger-xss-shopify-dashboard
tags:
  - xss
  - execution
  - shopify
  - dashboard
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:44.539Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-in-Live-Dashboard

## Summary

This procedure triggers the stored XSS payload by viewing the Shopify live dashboard, executing JavaScript in the admin context to demonstrate arbitrary code execution and potential data exfiltration.

## Description

After injecting the payload into the street address field, navigating to the live dashboard renders the stored address, parsing the SVG onload script. This executes JavaScript upon page load, alerting the document domain as proof-of-concept. In a real attack, this could extend to stealing admin session cookies via document.cookie or performing other client-side manipulations, highlighting the risk of session hijacking.

## Requirements

1. Previously injected and saved XSS payload in settings
2. Authenticated admin session
3. Access to /admin/dashboards/live endpoint

## Defense

Defensive measures and detection strategies:

- Sanitize all rendered user-controlled data in dashboard views
- Implement Content Security Policy (CSP) to block inline scripts and SVG onload
- Monitor for anomalous JavaScript execution or alerts in browser consoles

## Objectives

1. Render the stored payload to trigger execution
2. Verify JavaScript runs in the admin domain context
3. Demonstrate impact like domain alerting or cookie access

## Instructions

### Step 1: Navigate to Dashboard

**Context**: Load the page that renders the vulnerable stored data.

From the admin sidebar, go to "Analytics" > "Live" or directly access https://[store].myshopify.com/admin/dashboards/live.

> The page should load the dashboard with embedded store details.

### Step 2: Observe Execution

**Context**: Allow the onload event to fire automatically.

Upon page load, the SVG in the rendered address triggers the alert(document.domain).

> Expected output: Browser alert box shows the store's domain (e.g., xxx.myshopify.com).

### Step 3: Validate Impact

**Context**: Inspect for broader exploitation potential.

Open browser developer tools (F12), check the Console for errors or executed code, and verify session cookies remain accessible via the executed context.

> Success if no CSP blocks occur and domain is alerted.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- execution
- dashboard
