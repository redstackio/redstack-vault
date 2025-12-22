---
type: procedure
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Network Service Scanning]]'
sub_techniques: []
tags:
  - brute-force
  - web-applications
  - reconnaissance
commands:
  - '[[commands/gobuster-vhost-enumeration]]'
tools:
  - '[[tools/Gobuster]]'
platforms:
  - Web
skill_level: beginner
impact_level: low
detection_risk: low
verified: true
validated: true
---

# Brute-Force-Virtual-Host-Domains-Gobuster

## Summary

This procedure uses Gobuster to brute-force virtual host (vhost) domains on a target web application by enumerating potential subdomains via the HTTP Host header. It helps discover hidden or administrative interfaces that may be accessible only through specific domain names, aiding in reconnaissance for further exploitation.

## Description

Many web applications rely on virtual hosting to serve different content based on the requested domain name, even when all traffic resolves to the same IP address. Attackers can exploit this by fuzzing the Host header with a wordlist of common subdomain names to identify valid vhosts. This technique is particularly useful in scenarios where DNS enumeration alone misses internal or aliased domains. The procedure assumes the target is a web server (e.g., Apache or Nginx) configured with name-based virtual hosting. Success reveals additional attack surfaces, such as admin panels or staging sites, but requires a good wordlist for effectiveness. Potential challenges include rate limiting or WAF blocking, which can be mitigated by adding delays or using proxies.

## Requirements

1. Gobuster tool installed on the attacker's machine.
2. A wordlist containing common subdomain names (e.g., admin, staging, dev).
3. Network access to the target web server over HTTP/HTTPS.
4. Optional: Local /etc/hosts file modifications if IP-to-domain mapping needs manual override.

## Defense

Defensive measures include implementing web application firewalls (WAFs) to detect and block anomalous Host header requests, enabling rate limiting on the server, and monitoring access logs for unusual domain patterns. Use HTTPS with HSTS to prevent header manipulation, and regularly audit virtual host configurations to minimize exposed surfaces.

## Objectives

1. Identify hidden virtual hosts on the target web application.
2. Expand the attack surface by discovering subdomain-specific content.
3. Validate findings for potential privilege escalation or further reconnaissance paths.

## Instructions

### Step 1: Prepare the Wordlist

**Context**: A quality wordlist is essential for effective brute-forcing. Use a pre-built list of common vhost names or generate one tailored to the target (e.g., based on company naming conventions). This step ensures the tool has relevant guesses to test.

Download or create a wordlist file, such as SecLists' vhost list.

> Expected: A text file (e.g., vhosts.txt) with one subdomain per line, like 'admin', 'test', 'portal'.

### Step 2: Verify Target Accessibility

**Context**: Confirm the target responds to HTTP requests before brute-forcing to avoid false negatives from connectivity issues. This also helps identify the base URL format.

Use a basic curl command to test:

```bash
curl -I http://$_TARGET_HOST
```

> Expected: HTTP response headers indicating a successful connection (e.g., 200 OK or 403 Forbidden). If DNS issues arise, add an entry to /etc/hosts mapping the domain to the IP.

### Step 3: Execute Gobuster Vhost Enumeration

**Context**: Run Gobuster in vhost mode to fuzz the Host header. This sends requests with guessed domains prepended to the target (e.g., admin.example.com) and analyzes responses for valid hosts based on status codes or content length changes.

**Command** ([[commands/gobuster-vhost-enumeration]]):

```bash
gobuster vhost -u http://$_TARGET_HOST -w $_WORDLIST
```

> This command probes the target using the specified wordlist. Gobuster automatically handles the prepending of guesses to the base domain. Monitor for 200/403 responses indicating valid vhosts. If the target uses HTTPS, replace 'http' with 'https'. For noisy environments, add '--delay' flag (not in base command) to slow requests.

### Step 4: Analyze and Verify Results

**Context**: Review Gobuster's output to identify valid vhosts, then manually verify them to confirm accessibility and content differences. This step distinguishes true positives from false ones.

Parse the output for lines like 'Found: https://guess.target.com [Status 200]'. Test each with a browser or curl:

```bash
curl -H "Host: $_FOUND_VHOST" http://$_TARGET_IP
```

> Expected: Unique content or redirects for valid vhosts, such as admin login pages. Update /etc/hosts if needed for local resolution (e.g., echo "$_TARGET_IP $_FOUND_VHOST" >> /etc/hosts).
