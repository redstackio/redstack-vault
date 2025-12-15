---
id: proc-uuid-001
tags:
  - recon
  - intercept
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/Legitimate-GET-Request-to-CDN-File]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:56.694Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Legitimate-CDN-Request-with-Burp-Suite

## Summary

This procedure captures a legitimate HTTP request to a static file on Shopify's CDN using Burp Suite proxy interception, serving as the foundation for subsequent cache poisoning modifications. It allows attackers to analyze and alter requests in a controlled manner without disrupting normal traffic initially.

## Description

In the context of exploiting cache poisoning on cdn.shopify.com, this step involves setting up Burp Suite to proxy browser traffic and intercepting a GET request for a static asset like a JavaScript file. The target environment is any web browser accessing public CDN resources. Prerequisites include Burp Suite installed and configured as the system proxy. Expected outcome is a captured request that can be forwarded or modified, confirming normal access before poisoning.

## Requirements

1. Burp Suite installed and running with proxy listener on localhost:8080
2. Browser configured to use Burp as proxy (e.g., via FoxyProxy extension)
3. Internet access to target CDN domain (cdn.shopify.com)

## Defense

Defensive measures and detection strategies:

- Monitor proxy traffic anomalies in network logs for unusual interception tools
- Implement client certificate pinning to prevent proxy interception
- Use web application firewalls (WAFs) to detect modified request patterns

## Objectives

1. Capture baseline legitimate request for modification
2. Verify normal CDN response (200 OK with file content)
3. Prepare for path alteration in cache poisoning attack

## Instructions

### Step 1: Configure Burp Suite Proxy

**Context**: Set up Burp to intercept HTTP traffic from the browser, enabling request capture without prior authentication.

**Command** ([[commands/Legitimate-GET-Request-to-CDN-File]]):

No direct command; configure via Burp UI.

> Launch Burp Suite, navigate to Proxy > Options, ensure Intercept is on. In browser, set proxy to 127.0.0.1:8080.

### Step 2: Trigger and Intercept Request

**Context**: Access a legitimate CDN file to generate and intercept the request, observing the standard forward-slash path.

**Command** ([[commands/Legitimate-GET-Request-to-CDN-File]]):
```http
GET /static/javascripts/vendor/bugsnag.v7.4.0.min.js HTTP/1.1
Host: cdn.shopify.com
Connection: close
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
```

> Open https://cdn.shopify.com/static/javascripts/vendor/bugsnag.v7.4.0.min.js in browser. Intercept in Burp Proxy tab. Forward to see 200 OK with JS file. Expected output: Successful response with JavaScript content.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/Legitimate-GET-Request-to-CDN-File]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- recon
- intercept
- burp-suite
