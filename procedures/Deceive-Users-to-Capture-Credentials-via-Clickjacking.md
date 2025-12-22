---
id: p-deceive-capture-clickjacking
tags:
  - phishing
  - credential-theft
  - clickjacking
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[T1566.001]]'
updated_at: '2025-12-14T17:28:04.995Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
---
# Deceive Users to Capture Credentials via Clickjacking

## Summary

This procedure uses the framed login page to trick users into entering credentials, capturing sensitive data like emails and passwords through deceptive overlays on the attacker's site.

## Description

Once embedded, the clickjacked page mimics a legitimate interface. Users are lured via phishing links to the attacker's site, where clicks intended for fake elements interact with the hidden login form. Due to same-origin policy, direct capture may require server-side proxying or form post interception. Targets like https://hackers.upchieve.org/login enable theft of auth data, resembling phishing but exploiting UI manipulation.

## Requirements

1. Hosted malicious page with iframe
2. Phishing vector (e.g., email/link) to direct victims
3. Server-side logging for captured data

## Defense

Defensive measures and detection strategies:

- User awareness training on suspicious sites
- Multi-factor authentication to mitigate credential theft
- Endpoint detection for anomalous browser behavior

## Objectives

1. Lure and deceive users into interaction
2. Capture submitted login credentials
3. Exfiltrate data to attacker control

## Instructions

### Step 1: Enhance Page for Deception

**Context**: Add JavaScript to align overlays and simulate interactions.

Modify attack.html to include JS for dynamic positioning:

```html
<script>
  document.getElementById('frame').onload = function() {
    // Align fake button over real login button
    var fakeBtn = document.querySelector('button');
    fakeBtn.onclick = function() {
      // Trigger click on framed login (limited by SOP)
      alert('Login clicked!'); // Placeholder for capture
    };
  };
</script>
```

> JS simulates clicks; for real capture, proxy requests. Expected output: Clicks on fake elements interact with frame.

### Step 2: Lure and Capture

**Context**: Distribute the page URL and monitor submissions.

Send phishing link to victims (e.g., "Update your login at [attacker-site]"). On server, log any proxied POST data from the form.

> Victims enter credentials thinking it's legitimate. Expected output: Captured email/password in server logs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.001]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[credential-theft]]
- [[Phishing]]
