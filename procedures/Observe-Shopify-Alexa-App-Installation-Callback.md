---
id: proc-observe-shopify-callback
tags:
  - recon
  - shopify
  - app-installation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-observe-callback]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:24:26.672Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Observe-Shopify-Alexa-App-Installation-Callback

## Summary

This procedure involves monitoring the installation process of the Amazon Alexa app in Shopify to capture and analyze the callback URL, revealing parameters like 'shop' that are susceptible to manipulation.

## Description

During the installation of the Amazon Alexa app for Shopify, a callback URL is invoked at https://assistant-client.meteorapp.com/shopify/callback with query parameters including code, hmac, shop, and timestamp. By observing this URL, attackers can identify the lack of validation in the 'shop' parameter, setting the stage for open redirect exploitation. This is typically done in a legitimate Shopify store environment to mimic user behavior and inspect network requests.

## Requirements

1. Valid Shopify account with app installation permissions
2. Web browser with developer tools or curl for request inspection
3. Network access to Shopify and meteorapp.com domains

## Defense

Defensive measures and detection strategies:

- Monitor app installation logs for unusual callback parameters
- Implement URL validation in app callbacks to restrict domains
- Use web application firewalls to detect parameter tampering

## Objectives

1. Capture the exact callback URL and parameters during app installation
2. Identify the 'shop' parameter as a potential injection point
3. Validate the endpoint's behavior with legitimate requests

## Instructions

### Step 1: Initiate App Installation

**Context**: Start the Amazon Alexa app installation in your Shopify admin panel to trigger the callback.

**Command** ([[commands/curl-observe-callback]]):
```bash
# Note: This simulates observation; in practice, use browser dev tools to capture the full URL during install
curl -v "https://assistant-client.meteorapp.com/shopify/callback?code=6aae881ab9c4f12d5b264e6c871a108a&hmac=6109806a12b0439d6a2dce2d547344eb1c2c53e9691259f39eefbb93b9c9c97b&shop=pappuza-2.myshopify.com&timestamp=1494008598"
```

> This command sends a verbose request to the callback, showing headers and response. Expected output includes a 302 redirect to the shop domain, confirming the parameter structure.

### Step 2: Analyze Parameters

**Context**: Extract and document the parameters from the observed URL to understand their role.

No specific command; manually note parameters like shop=pappuza-2.myshopify.com.

> Review the response for redirect location; success if it matches the shop domain without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/curl-observe-callback]]

## Tools Used


## Tags

- recon
- shopify
- app-installation
