---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - xss
  - intercept
  - http-request
type: procedure
tools:
  - '[[tools/Burp-Repeater]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:31.422Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Craft-Checkout-POST-Request

## Summary

This procedure captures or manually crafts a legitimate POST request to the WordPress /store/checkout/ endpoint using Burp Repeater, providing a baseline for injecting payloads in subsequent XSS exploitation steps.

## Description

In a WordPress-based e-commerce site, the checkout process sends sensitive form data via POST to /store/checkout/. By intercepting this with Burp Repeater, attackers can analyze and modify parameters like billing[address] without triggering server-side validations prematurely. This step is crucial for reflected XSS attacks where user input is echoed back unsanitized. The target environment is a web application running WordPress and PHP, accessible over HTTP/HTTPS.

## Requirements

1. Burp Suite installed and running with proxy enabled
2. Browser configured to route traffic through Burp (e.g., via FoxyProxy extension)
3. Access to the target site's checkout page (e.g., masterplan.wordpress.net/store/checkout/)
4. Basic understanding of HTTP POST requests and form parameters

## Defense

Defensive measures and detection strategies:

- Implement web application firewall (WAF) rules to monitor unusual request patterns to checkout endpoints
- Enable HTTPS and HSTS to prevent interception in transit
- Log all POST requests to /store/checkout/ and alert on proxy-like tool signatures (e.g., Burp UA strings)

## Objectives

1. Obtain a valid, interceptable POST request structure
2. Identify editable parameters for payload injection
3. Ensure request can be replayed without authentication issues

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up Burp Suite to intercept browser traffic for capturing the checkout request.

In Burp Suite, ensure the Proxy tab is active and listening on localhost:8080. Configure your browser's proxy settings to 127.0.0.1:8080.

> Expected output: Traffic from the browser routes through Burp, visible in the Proxy > Intercept tab.

### Step 2: Trigger Legitimate Checkout

**Context**: Perform a normal checkout to capture the baseline request.

Navigate to the target site's store, add an item to cart, proceed to checkout, and fill in form fields (e.g., billing[address]=1 Main Street, shipping details, payment info). Submit the form while interception is enabled.

In Burp's Intercept tab, capture the POST /store/checkout/ request.

> Expected output: Raw HTTP request displayed, including headers (e.g., Content-Type: application/x-www-form-urlencoded) and body with parameters like action=woocommerce_checkout.

### Step 3: Send to Repeater

**Context**: Move the captured request to Repeater for modification in the next procedure.

Right-click the intercepted request in Burp and select "Send to Repeater". Drop the interception to allow the request to complete if needed.

> Expected output: Request loaded in Burp Repeater tab, ready for editing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Repeater]]

## Tags

- xss
- intercept
- http-request
