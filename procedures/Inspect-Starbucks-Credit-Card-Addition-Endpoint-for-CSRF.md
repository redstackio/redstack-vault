---
tags:
  - csrf
  - web
  - recon
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:35.723Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: aaf7ffd0-53a7-4877-817b-3e018ff2ba45
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Inspect-Starbucks-Credit-Card-Addition-Endpoint-for-CSRF

## Summary

This procedure involves inspecting the legitimate credit card addition form on store.starbucks.com to identify the POST endpoint and confirm the absence of CSRF protection, enabling subsequent exploitation.

## Description

In a web application like Starbucks' online store built on Demandware, the payment functionality allows users to save credit cards. By examining the form using browser developer tools, attackers can uncover the endpoint https://store.starbucks.com/on/demandware.store/Sites-Starbucks-Site/default/COBilling-AddCreditCard and its fields (e.g., dwfrm_billing_paymentMethods_creditCard_type, owner, number, month, year, saveCard). The lack of a CSRF token means cross-origin submissions are possible, setting the stage for unauthorized actions when a victim is tricked into submitting data.

## Requirements

1. Access to a web browser with developer tools (e.g., Chrome)
2. Ability to navigate to store.starbucks.com and reach the payment section
3. Basic knowledge of HTML forms and network inspection

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing forms
- Use Content-Security-Policy (CSP) headers to restrict form actions
- Monitor for anomalous payment method additions via logging

## Objectives

1. Confirm the vulnerable endpoint and form structure
2. Verify absence of anti-CSRF protections
3. Gather details for crafting exploit payload

## Instructions

### Step 1: Navigate to Payment Form

**Context**: Access the legitimate interface to inspect the form.

Open store.starbucks.com, log in if needed, and go to the billing or payment settings where credit cards can be added.

### Step 2: Inspect Form Elements

**Context**: Use developer tools to reveal the backend endpoint and fields.

Right-click the form and select "Inspect Element". In the Network tab, submit a test form to capture the POST request. Note the URL and parameters like dwfrm_billing_paymentMethods_creditCard_type=Visa, owner=Test User, number=4111111111111111, month=10, year=2024, saveCard=true.

> Look for any CSRF token field (e.g., _csrf or similar); absence confirms vulnerability.

### Step 3: Validate Cross-Origin Potential

**Context**: Test if the endpoint accepts submissions without origin checks.

Attempt a simple cross-origin POST from a local HTML file to confirm it processes without errors.

**Expected Output**: Request succeeds, indicating no CSRF protection.

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
- [[web]]
- [[recon]]
