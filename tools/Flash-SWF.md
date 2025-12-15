---
id: tool-flash-swf
url: null
name: Flash SWF
tags:
  - flash
  - cross-domain
  - header-spoof
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.615Z'
validated: true
submitted: true
---
# Flash SWF

**Status**: Unverified

## Overview

Adobe Flash SWF files are legacy multimedia containers used here for offensive security to perform cross-domain requests and spoof HTTP headers, bypassing web protections like CSRF in pre-deprecation browsers.

## Description

In this context, a custom SWF (e.g., vimeo_pwn.swf) is compiled using ActionScript to load crossdomain.xml policies, follow HTTP redirects, and inject headers like 'X-Requested-With: XMLHttpRequest' during API calls. It's particularly effective against endpoints relying on custom headers for CSRF, as Flash can forge them via redirects from permissive domains before SOP/CORS enforcement. Deprecated since 2020, but useful for historical or legacy testing.

## Features

- Feature 1: Cross-domain policy fetching and enforcement bypassing via timing.
- Feature 2: HTTP redirect following with custom header injection.
- Feature 3: Silent execution without JavaScript dependencies.

## Installation

### Requirements

- Adobe Flash Professional or open-source compiler like Ming.
- ActionScript knowledge for custom logic.

### Install Commands

```bash
# No traditional install; compile SWF from .as source
# Example using Ming: mingc -s 9 vimeo_pwn.as -o vimeo_pwn.swf
```

## Basic Usage

Embed or direct-load the SWF in a browser: <embed src="vimeo_pwn.swf" type="application/x-shockwave-flash">

### Common Options

| Option | Description |
|--------|-------------|
| N/A | SWF is self-contained; configure via ActionScript code |

## Examples

### Example 1: Basic Cross-Domain Request

Compile SWF to request crossdomain.xml and redirect:

ActionScript snippet:

```actionscript
import flash.net.URLRequest;
import flash.net.navigateToURL;
var req:URLRequest = new URLRequest("https://attacker.com/vimeo_pwn.php");
navigateToURL(req, "_self");
```

### Example 2: Header Spoofing in Redirect

In SWF, set headers before following 307:

```actionscript
// Pseudo-code for header injection during request
var loader:URLLoader = new URLLoader();
loader.addRequestHeader("X-Requested-With", "XMLHttpRequest");
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Drive-by Compromise]] Drive-by Compromise

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for SWF loads from untrusted domains in browser logs.
- Detection method 2: Flash deprecation logs or anomalous cross-domain requests in network traces (e.g., via Wireshark).

## Related Procedures


## Related Tools

- [[tools/xss-swf]]

## References

- Adobe Flash Documentation (archived)
- HackerOne Report #44146
