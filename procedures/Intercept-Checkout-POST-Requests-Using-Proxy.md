---
tags:
  - intercept
  - proxy
  - post-request
  - xml
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:28.461Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 4e33fb60-5b67-4233-983a-087fe2cf9aa5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Checkout-POST-Requests-Using-Proxy

## Summary

This procedure captures POST requests in the shopping cart checkout workflow of a web-based e-commerce system to identify XML payloads containing sensitive parameters like prices, enabling subsequent tampering.

## Description

In the context of Adobe's e-commerce system, the checkout process sends POST requests with XML payloads that include product details and prices. Without proper proxy interception, these requests cannot be modified. This step uses a web proxy to monitor and capture traffic, focusing on the unvalidated XML structure that allows parameter tampering. Prerequisites include a valid user session and network access to the target site. Expected outcomes include visibility into the request format for exploitation.

## Requirements

1. Web proxy tool (e.g., Burp Suite) installed and configured
2. Browser traffic routed through the proxy
3. Active shopping cart with items added on the target site
4. User-level access to initiate checkout

## Defense

Defensive measures and detection strategies:

- Implement client-side certificate pinning to prevent proxy interception
- Monitor for unusual traffic patterns or proxy tool signatures in logs
- Use HTTPS with HSTS to complicate interception

## Objectives

1. Capture the exact structure of the checkout POST request
2. Identify XML elements containing price parameters
3. Prepare for payload modification without alerting the server

## Instructions

### Step 1: Configure Proxy Interception

**Context**: Set up the proxy to route all traffic from the browser to the target site, ensuring the checkout workflow is intercepted.

Use [[tools/Burp-Suite]] to create a new project and configure the browser proxy settings (e.g., 127.0.0.1:8080). Install the Burp CA certificate in the browser to handle HTTPS.

### Step 2: Trigger and Capture Request

**Context**: Initiate the checkout process to generate the POST request and intercept it in the proxy.

Add items to the cart on the target site (e.g., Adobe e-commerce), proceed to checkout, and submit the form. In Burp's Proxy > Intercept tab, capture the outgoing POST request to the checkout endpoint.

**Expected Output**: Raw HTTP POST request with body containing XML payload, e.g., <cart><item><price>100.00</price></item></cart>.

### Step 3: Inspect Payload

**Context**: Analyze the captured XML to locate tamperable parameters.

In Burp's Repeater or Inspector, view the request body and parse the XML for price-related tags.

**Expected Output**: Confirmed presence of editable price values in XML.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[intercept]]
- [[proxy]]
- [[post-request]]
- [[xml]]
