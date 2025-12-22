---
tags:
  - csrf
  - shopify
  - paypal
  - url-forgery
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:57.899Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 71ce2d24-eed4-4f89-b311-094d1ee8aaf3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-CSRF-URL-for-PayPal-Hijack

## Summary

This procedure forges a CSRF URL using the victim's static merchantId and attacker's PayPal ID to trick the victim into connecting their Shopify store to the attacker's payment account.

## Description

Exploiting the weak CSRF token (merchantId), the attacker crafts a GET request mimicking the legitimate PayPal OAuth completion. When visited by a logged-in victim, it bypasses protections and grants the attacker control over the store's payments. Targets the `/admin/payments/complete_paypal_incontext_oauth/` endpoint; vulnerable due to static token reusability within 24 hours.

## Requirements

1. Extracted victim merchantId from prior step
2. Attacker's PayPal merchant ID (e.g., 5NS8DHQCFGT84)
3. Method to deliver URL to victim (e.g., phishing email)
4. Victim must be logged into Shopify admin

## Defense

Defensive measures and detection strategies:

- Use dynamic, session-bound CSRF tokens instead of static IDs
- Require user confirmation for payment provider changes via secondary channels (e.g., email OTP)
- Implement rate limiting on activation endpoints and monitor for anomalous connections

## Objectives

1. Forge URL to impersonate legitimate PayPal activation
2. Induce victim to visit URL, completing the OAuth flow
3. Achieve unauthorized linkage of store to attacker's PayPal

## Instructions

### Step 1: Construct the Malicious URL

**Context**: Build the GET request by substituting the victim's merchantId and attacker's PayPal ID into the activation endpoint template.

Start with the base URL from the extraction step and replace parameters.

Example constructed URL:

`https://YOURSUBDOMAIN.myshopify.com/admin/payments/complete_paypal_incontext_oauth/41?merchantId=1583030504:010f06db85734b485ed095c45af1cfe7&merchantIdInPayPal=5NS8DHQCFGT84&permissionsGranted=true&accountStatus=BUSINESS_ACCOUNT&consentStatus=true&productIntentID=addipmt&productIntentId=addipmt&isEmailConfirmed=true`

> Ensure all boolean parameters are set to 'true' to simulate successful OAuth.

### Step 2: Deliver and Trigger the URL

**Context**: Send the URL to the victim and confirm execution upon visit.

Embed the URL in a phishing page, email, or direct link. Victim clicks while logged in.

> Upon visit, the endpoint processes the request, connecting the store without further prompts.

### Step 3: Verify Hijack

**Context**: Check the attacker's PayPal dashboard or victim's store settings for confirmation.

Log in to attacker's PayPal and look for new store integration; in victim's Shopify, payments should show the attacker's account.

> Success: Unauthorized connection established, enabling payment routing control.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[shopify]]
- [[paypal]]
- [[url-forgery]]
