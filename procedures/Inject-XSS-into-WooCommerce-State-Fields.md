---
tags:
  - xss
  - dom-xss
  - woocommerce
  - wordpress
type: procedure
tools:
  - '[[tools/Web-Intercept-Proxy]]'
tactics:
  - '[[Initial Access]]'
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:33.784Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 4ffd6008-f5dc-4e25-8bf2-abe6caade101
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Inject-XSS-into-WooCommerce-State-Fields

## Summary

This procedure exploits a stored DOM-based XSS vulnerability in WooCommerce 3.5.6 by injecting a malicious JavaScript payload into the _shipping_state or _billing_state fields during order creation or editing. The unescaped input is reflected on the order view page, executing arbitrary code in the admin's browser, potentially leading to session hijacking or data exfiltration.

## Description

In WooCommerce 3.5.6, user-supplied data from billing and shipping state fields is not properly escaped when rendered on the order edit page, allowing DOM manipulation. Attackers with admin access can directly inject payloads, or non-privileged users can tamper with checkout POST data using a proxy. Upon admin viewing, the payload executes, enabling theft of admin cookies or further attacks. This targets WordPress sites with the vulnerable plugin version and requires browser access to the admin panel.

## Requirements

1. Access to WordPress admin panel with WooCommerce 3.5.6 (for direct injection) or customer checkout access (for proxy-based).
2. Browser for navigation and form submission.
3. Optional: Web proxy like Burp Suite for non-privileged interception.

## Defense

Defensive measures and detection strategies:

- Upgrade WooCommerce to version 3.5.7 or later where escaping is fixed.
- Implement Content Security Policy (CSP) to restrict inline scripts and img src.
- Monitor order data for suspicious strings like '<img src=' or 'onerror='.
- Use web application firewall (WAF) rules to block XSS payloads in form submissions.

## Objectives

1. Inject and store a JavaScript payload in order state fields.
2. Trigger execution when an admin views the affected order.
3. Achieve arbitrary code execution in the victim's browser context for data theft.

## Instructions

### Step 1: Navigate to Order Interface

**Context**: Gain access to the WooCommerce order creation or editing page to expose vulnerable fields.

From the WordPress admin menu, select WooCommerce > Add Order (or edit an existing one).

> This loads the form where state fields can be manipulated.

### Step 2: Expand and Prepare Address Form

**Context**: Reveal the billing or shipping details section containing the vulnerable state input.

Click the pencil icon next to Billing or Shipping to expand the form, then select a country from the dropdown to enable the State field.

> Ensures the State / County input is available for payload entry.

### Step 3: Inject Payload

**Context**: Enter the malicious payload to break out of HTML context and inject script.

Input `'><img src=/ onerror="alert(location.host)"` into the State / County field. For cookie theft variant: `'><img src=/ onerror="alert(document.cookie)"`.

> The payload closes any open tag and inserts an onload error handler that executes JS.

### Step 4: Submit and Store Order

**Context**: Persist the tainted data in the database for later retrieval.

Click Create (or Update) to save the order.

> Order is stored with unescaped payload in _shipping_state or _billing_state.

### Step 5: Trigger Execution (Admin View)

**Context**: Load the order page to cause DOM insertion and script execution.

Navigate to the order's edit page in the admin panel.

> Payload renders without escaping, executing the alert or exfiltration code.

### Step 6: Alternative Non-Privileged Injection

**Context**: For users without admin access, intercept checkout to inject payload.

Add a product to cart, proceed to checkout, enable [[tools/Web-Intercept-Proxy]], fill details, and modify the POST request's billing_state to `billing_state="><img+src%3d/+onerror%3d\"alert(document.cookie)\"`. Then place the order and have an admin view it in the panel.

> Bypasses frontend validation via proxy tampering; executes on admin view.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Intercept-Proxy]]

## Tags

- xss
- dom-xss
- woocommerce
- wordpress
