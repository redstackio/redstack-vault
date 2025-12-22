---
id: proc-trigger-ssrf-user-001
tags:
  - ssrf
  - csrf
  - user-execution
  - wordpress
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T04:09:00.725Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
---
---
id: proc-trigger-ssrf-user-001
name: Trigger-SSRF-via-Authenticated-User
type: procedure
verified: false
submitted: false
created_at: 2024-01-01T00:00:00Z
updated_at: 2024-01-01T00:00:00Z
tactics: [[Initial Access]], [[Execution]]
techniques: [[Exploit Public-Facing Application]], [[Drive-by Compromise]]
sub_techniques: []
tags: ssrf, csrf, user-execution, wordpress
commands: []
platforms: Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
---

# Trigger-SSRF-via-Authenticated-User

## Summary

This procedure lures an authenticated WordPress user to a malicious page, triggering CSRF to initiate scraping that leads to SSRF via the prepared redirect, allowing internal access.

## Description

By exploiting user execution, the attacker induces a privileged user to visit a page that forges the Press This request. The server then scrapes the attacker's domain, follows the redirect to private IPs/ports, and performs the SSRF with potential basic-auth, compromising internal services like routers or caches.

## Requirements

1. Authenticated victim with WordPress admin/editor access
2. Malicious page and redirect endpoint already hosted
3. Social engineering capability to lure the victim

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and suspicious links
- Enable CSRF protections and referer checks on admin actions
- Monitor server logs for Press This scrapes and outbound requests to private IPs

## Objectives

1. Leverage user privileges to trigger server-side actions
2. Complete the SSRF chain to access internal resources
3. Validate impact through internal service interactions

## Instructions

### Step 1: Distribute Malicious Link

**Context**: Send the CSRF page URL to the target user via email, chat, or embedded link.

No command; example phishing message: "Check this article: http://attackers-domain.com/malicious.html"

> The user visits while logged into WordPress, triggering the img src request.

### Step 2: Monitor and Confirm SSRF

**Context**: Observe the chain: scrape request, redirect follow, internal hit.

Check your server logs for the incoming scrape, then internal service logs for the SSRF request.

Example log check (if using file logs):

> Expected: Scrape GET from WP IP, then internal log: GET from WP IP with User-Agent: Press This, Authorization header if injected.

### Step 3: Exfiltrate or Exploit Response

**Context**: If the internal service responds, the data may be processed or logged; chain to further attacks.

No command; review WP error logs or your redirect logs for any echoed response.

> Success: Internal data accessed, e.g., Memcached keys from 11211 or router config from 12345.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[csrf]]
- [[user-execution]]
- [[wordpress]]
