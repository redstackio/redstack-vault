---
id: initiate-checkout-001
name: Initiate Checkout Process
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:48.040Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - web
  - checkout
  - preparation
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
commands: []
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Initiate Checkout Process

## Summary

This procedure sets up the initial purchase flow on the Acronis.cz website by navigating to a product and filling in basic checkout details, preparing for subsequent request interception and manipulation.

## Description

In the context of exploiting an IDOR vulnerability in the checkout process, this procedure involves accessing the public-facing e-commerce site, selecting a product like Acronis Cyber Protect Home Office, and entering contact details in the form. It requires no authentication and serves as the foundation for triggering the vulnerable 'Buy Now' request. Expected outcomes include reaching the pre-submission stage where the request can be intercepted, enabling price tampering without server-side validation of the original cart data.

## Requirements

1. Direct internet access to acronis.cz
2. Standard web browser (e.g., Firefox or Chrome)
3. Proxy configuration for Burp Suite (optional at this stage but recommended)

## Defense

Defensive measures and detection strategies:

- Implement client-side request signing or HMAC to prevent tampering
- Monitor for anomalous price discrepancies in logs
- Use CAPTCHA or rate limiting on checkout forms

## Objectives

1. Access and prepare the target product's purchase flow
2. Fill mandatory form fields to simulate legitimate user behavior
3. Position for request interception without alerting defenses

## Instructions

### Step 1: Navigate to Product Page

**Context**: Load the target website and select a high-value product to maximize impact of price manipulation.

No specific command; use browser to visit https://www.acronis.cz/produkt/acronis-cyber-protect-home-office/ and click 'Buy Now' to enter checkout.

> Browser navigation; expected output: Checkout form displayed.

### Step 2: Enter Purchase Details

**Context**: Provide minimal required information to advance to the submission stage.

Fill fields like name, email, and address in the form.

> Form submission not yet executed; expected output: Form ready for 'Buy Now' click.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[web]]
- [[checkout]]
- [[preparation]]
