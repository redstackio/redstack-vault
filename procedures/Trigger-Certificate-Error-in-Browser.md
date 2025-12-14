---
id: proc-uuid-002
tags:
  - certificate-error
  - browser-trigger
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Internet-Explorer]]'
  - '[[tools/Microsoft-Edge]]'
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Windows
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:12.471Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Trigger-Certificate-Error-in-Browser

## Summary

Navigate to a redirected HTTPS site in a vulnerable browser to invoke Kaspersky Internet Security's certificate warning page, setting the stage for clickjacking exploitation.

## Description

After hosts file modification, accessing the site causes a domain-IP mismatch, prompting Kaspersky's web protection to display a framable warning UI. Tested across multiple browsers to confirm consistency in triggering the vulnerable page.

## Requirements

1. Hosts file modified to redirect target domain
2. Kaspersky Internet Security active with web protection enabled
3. Supported browser installed

## Defense

Defensive measures and detection strategies:

- Enable strict certificate pinning in browsers
- Configure security software to block framable warning pages (e.g., add X-Frame-Options)
- Log anomalous certificate warnings for anomaly detection

## Objectives

1. Display the vulnerable certificate warning UI
2. Ensure the page is iframe-compatible for clickjacking
3. Prepare for user interaction overlay

## Instructions

### Step 1: Launch Browser

**Context**: Select a tested browser to ensure compatibility.

**Instructions**: Open [[tools/Firefox]] (version 64) or alternatives like [[tools/Internet-Explorer]] (11) or [[tools/Microsoft-Edge]].

### Step 2: Navigate to Target Site

**Context**: Trigger the HTTPS request to invoke the mismatch.

**Instructions**: Enter https://www.google.com/ in the address bar and press Enter.

> Kaspersky intercepts and shows the certificate error page with an override link.

### Step 3: Observe Warning

**Context**: Confirm the UI elements are present for framing.

**Instructions**: Note the 'I understand the risks and wish to continue' link; do not click yet.

> Expected: Warning page loads without X-Frame-Options, allowing embedding.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Internet-Explorer]]
- [[tools/Microsoft-Edge]]

## Tags

- certificate-error
- browser-trigger
