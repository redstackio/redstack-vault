---
tags:
  - social-engineering
  - autofill
  - form-submission
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
updated_at: '2025-12-14T17:28:12.803Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 2a469fc1-d8ba-4745-ba5f-cf1ffdc2a452
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Induce-Victim-Interaction-for-Form-Submission

## Summary

This procedure covers tricking a victim into interacting with a hidden iframe containing a vulnerable form, leveraging browser autofill to submit unauthorized data and create fake reservations.

## Description

In a clickjacking scenario, the final stage involves social engineering to get the victim to visit the malicious site and click an element that propagates to the framed page. For Yelp's /reservations, this triggers autofill of contact details (email, phone) and submits a reservation form, exposing data to the business and potentially causing booking disruptions or fees. This relies on prior embedding and requires luring the victim via email, ads, or links.

## Requirements

1. Hosted malicious page with embedded iframe
2. Social engineering vector (e.g., phishing email or malicious link)
3. Victim with saved browser credentials or autofill enabled

## Defense

Defensive measures and detection strategies:

- Educate users on suspicious links and verify site authenticity
- Implement multi-factor authentication for sensitive actions like reservations
- Monitor for unusual booking patterns or rapid cancellations on the business side

## Objectives

1. Elicit a click that interacts with the hidden form
2. Trigger autofill and submission to expose private data
3. Achieve unauthorized reservation creation

## Instructions

### Step 1: Design the Interaction Trigger

**Context**: Align the visible element with the framed form's submit button.

Use JavaScript to ensure the click on the visible button forwards to the iframe's coordinates matching the reservation submit.

```javascript
 document.getElementById('trick').addEventListener('click', function() {
   var iframe = document.getElementById('hidden');
   var iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
   var submitBtn = iframeDoc.querySelector('input[type="submit"]'); // Adjust selector
   if (submitBtn) submitBtn.click();
 });
```

**Expected Output**: Click on visible button submits the framed form.

### Step 2: Lure the Victim

**Context**: Direct the victim to the malicious page.

Send a phishing email or host the page on a deceptive domain (e.g., "yelp-free-reservations.com"). Include a compelling call-to-action like "Claim your free table reservation now!"

**Expected Output**: Victim visits the site and clicks the trigger.

### Step 3: Validate Exploitation

**Context**: Confirm the impact post-interaction.

Check the business's Yelp reservation system or victim's account for the unauthorized booking and exposed data.

**Expected Output**: New reservation with victim's autofilled details.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[social-engineering]]
- [[autofill]]
- [[form-submission]]
