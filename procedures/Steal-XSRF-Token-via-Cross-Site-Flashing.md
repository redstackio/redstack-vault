---
id: proc-vimeo-steal-token-001
tags:
  - xsrf-token-theft
  - cross-site-flashing
  - information-disclosure
type: procedure
tools:
  - '[[tools/evil-swf]]'
  - '[[tools/moogaloop-swf]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Flash
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
  - '[[Forge Web Credentials]]'
updated_at: '2025-12-14T17:27:36.205Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Credentials In Files]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
  - '[[Forge Web Credentials]]'
---
# Steal-XSRF-Token-via-Cross-Site-Flashing

## Summary

This procedure uses a malicious SWF (evil.swf) to load Vimeo's legitimate moogaloop.swf and exploit a permissive crossdomain.xml policy, allowing access to the /moogaloop 404 page where the XSRF token is exposed in the HTML source, enabling token theft for subsequent CSRF attacks.

## Description

The attack leverages Flash's cross-site capabilities: evil.swf, hosted externally, loads moogaloop.swf from vimeocdn.com and sets its config_url to https://vimeo.com/moogaloop, triggering a request to the 404 page. The crossdomain.xml at http://vimeo.com/moogaloop/crossdomain.xml permits access from *.vimeocdn.com, allowing evil.swf to read the response containing the token, user name, ID, and account type. This occurs in the victim's browser session.

## Requirements

1. evil.swf compiled to load and control moogaloop.swf
2. Victim's browser with Flash enabled and Vimeo session active
3. Access to Vimeo's public Flash resources and 404 page

## Defense

Defensive measures and detection strategies:

- Remove or restrict crossdomain.xml policies to block external domain access
- Avoid embedding sensitive tokens in error pages; use server-side rendering without client exposure
- Monitor for anomalous Flash requests to internal endpoints from external domains

## Objectives

1. Load moogaloop.swf cross-site using evil.swf
2. Extract XSRF token and user info from 404 response
3. Prepare token for CSRF exploitation

## Instructions

### Step 1: Load moogaloop.swf in evil.swf

**Context**: evil.swf dynamically embeds and configures moogaloop.swf to request the target URL.

In Flash ActionScript within evil.swf:

```actionscript
loadMovie("https://f.vimeocdn.com/p/flash/moogaloop/6.3.5/moogaloop.swf", this);
this.config_url = "https://vimeo.com/moogaloop";
```

> This loads the SWF and sets the parameter. Expected: moogaloop.swf initializes without errors.

### Step 2: Access and Parse 404 Page

**Context**: moogaloop.swf requests /moogaloop, reads the HTML, and evil.swf intercepts to extract data.

Use Flash's loader to capture response:

```actionscript
var loader:Loader = new Loader();
loader.load(new URLRequest("https://vimeo.com/moogaloop"));
loader.contentLoaderInfo.addEventListener(Event.COMPLETE, onLoaded);
function onLoaded(e:Event):void {
    var html:String = e.target.data;
    var token:RegExp = /xsrf_token=([\w-]+)/;
    var match:Array = html.match(token);
    // Extract and store token
}
```

> Parses HTML for token (e.g., 'xsrf_token=abc123'). Also extract name, ID, type. Success: Token value obtained.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials
- [[Forge Web Credentials]] Forge Web Credentials

### Sub-Techniques

- [[Credentials In Files]] Credentials In Files

## Commands Used


## Tools Used

- [[tools/evil-swf]]
- [[tools/moogaloop-swf]]

## Tags

- xsrf-token-theft
- cross-site-flashing
- flash-exploitation
