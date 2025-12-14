---
tags:
  - xss
  - web-exploit
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.700Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: bb61bc2a-b1da-4a47-a049-82016142f741
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger Unauthorized Modal by Omitting client_id

## Summary

This procedure omits the client_id parameter in requests to the Mapbox /authorize endpoint, forcing the server to render an unauthorized modal template that uses the redirect_uri without escaping, setting up for XSS exploitation.

## Description

In the Mapbox authorization flow, omitting client_id causes the server to return a 401 Unauthorized response and render the 'template-modal-unauthorized' template client-side. This template inserts the redirect_uri directly into an <a> tag href without HTML escaping, allowing subsequent payload injection. The attack targets public-facing web applications vulnerable to parameter mishandling in auth flows.

## Requirements

1. Access to a web browser
2. Network connectivity to https://www.mapbox.com/authorize/
3. Basic understanding of URL parameters

## Defense

Defensive measures and detection strategies:

- Implement proper HTML escaping for all user-controlled inputs in templates (e.g., use <%= obj.redirect %> with escaping helpers)
- Validate and sanitize redirect_uri parameters against a whitelist of allowed domains
- Monitor for anomalous requests to /authorize without client_id

## Objectives

1. Trigger the vulnerable modal rendering
2. Expose the unescaped redirect_uri insertion point
3. Prepare for payload injection

## Instructions

### Step 1: Construct Request Without client_id

**Context**: Build and send a GET request to the endpoint omitting the required client_id to invoke the error handling path.

Navigate to the following URL in a web browser:

```url
https://www.mapbox.com/authorize/
```

> This loads the page and triggers a 401 response, rendering the modal via client-side JavaScript.

### Step 2: Inspect Rendered Template

**Context**: Verify the template insertion by examining the page source or developer tools.

Use browser dev tools (F12) to inspect the modal element. Look for the anchor tag with href containing the redirect_uri.

> Expected: <a href='<%= obj.redirect %>'> in the template source, confirming lack of escaping.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- xss-setup
- auth-bypass
