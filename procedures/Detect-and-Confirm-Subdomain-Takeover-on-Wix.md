---
tags:
  - subdomain-takeover
  - dns
  - wix
  - cname
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-http-head]]'
  - '[[commands/curl-http-get]]'
  - '[[commands/dig-cname-lookup]]'
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:38:49.222Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 52e96a00-c4eb-4b0b-9527-4811b81604ab
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Hardware]]'
  - '[[Exploit Public-Facing Application]]'
---
# Detect-and-Confirm-Subdomain-Takeover-on-Wix

## Summary

This procedure outlines the steps to detect a subdomain takeover vulnerability by identifying a dangling CNAME record pointing to unclaimed Wix infrastructure, as seen with www.cyberlynx.lu. It involves HTTP probing and DNS resolution to confirm the subdomain is available for claiming, enabling an attacker to host malicious content and impersonate the organization.

## Description

Subdomain takeovers occur when a subdomain's DNS records point to a third-party service (like Wix) that is no longer in use or unclaimed, allowing anyone to register and control it. In this scenario, www.cyberlynx.lu (acquired by Acronis) has a CNAME to Wix DNS but returns a 404 unclaimed page. The process starts with accessing the subdomain, checking for Wix's default error, verifying the DNS chain, and confirming claimability. Prerequisites include internet access and basic command-line tools. Expected outcomes: Identification of the vulnerability, leading to potential brand damage, phishing, or reputation attacks on the parent domain.

## Requirements

1. Internet connectivity for HTTP and DNS queries
2. Command-line access to curl and dig (standard on Linux/macOS; install via package manager on Windows)
3. Target subdomain like www.cyberlynx.lu with suspected dangling CNAME
4. Browser for final manual verification on Wix

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling CNAMEs using tools like dnsdumpster or subjack
- Monitor third-party services for unclaimed domains associated with your organization
- Implement DNS monitoring alerts for changes in CNAME targets
- Use certificate transparency logs to detect unauthorized subdomain claims

## Objectives

1. Identify unclaimed subdomains pointing to external services
2. Verify takeover feasibility to assess risk
3. Document evidence for remediation, such as removing the CNAME or claiming the subdomain
4. Prevent attacker control leading to phishing or defacement

## Instructions

### Step 1: Probe HTTP Response

**Context**: Send an HTTP request to check if the subdomain resolves to an active site or an unclaimed error page.

**Command** ([[commands/curl-http-head]]):
```bash
curl -I http://www.cyberlynx.lu/
```

> This HEAD request fetches headers without the body, revealing server details like Wix redirects or 404 status. Look for HTTP/1.1 404 Not Found and Wix-specific headers.

### Step 2: Fetch Full Error Page

**Context**: Retrieve the complete response body to inspect for platform-specific unclaimed indicators.

**Command** ([[commands/curl-http-get]]):
```bash
curl http://www.cyberlynx.lu/
```

> The output should show a Wix 404 page stating the site is available for registration. Save to a file with `> output.html` for analysis.

### Step 3: Query DNS CNAME Chain

**Context**: Trace the DNS resolution to confirm the pointer to Wix infrastructure without active hosting.

**Command** ([[commands/dig-cname-lookup]]):
```bash
dig www.cyberlynx.lu CNAME +trace
```

> This displays the full CNAME chain, e.g., www.cyberlynx.lu -> www118.wixdns.net -> balancer.wixdns.net. Absence of an A record indicates dangling status.

### Step 4: Manual Claim Verification

**Context**: Use a browser to attempt registration on Wix and confirm availability.

**Instructions**: Navigate to Wix.com, search for the domain www.cyberlynx.lu, and check if it's claimable. No command; document screenshots.

> Success if Wix prompts for registration without ownership verification conflicts.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

### Techniques

- [[Hardware]] Gather Victim Host Information: Identify Infrastructure
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-http-head]]
- [[commands/curl-http-get]]
- [[commands/dig-cname-lookup]]

## Tools Used

- None

## Tags

- [[subdomain-takeover]]
- [[DNS]]
- [[wix]]
- [[cname]]
- [[Reconnaissance]]
