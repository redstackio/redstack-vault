---
tags:
  - github
  - verification
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dns-query]]'
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T05:32:31.271Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 93a57e58-112f-4e75-9571-a033c4a88f3d
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Verify-Unclaimed-GitHub-Custom-Domain

## Summary

This procedure confirms whether a subdomain with a GitHub DNS pointer is claimed by checking for associated repositories and testing resolution, essential for validating takeover potential.

## Description

For subdomains like dev.rbk.money pointing to GitHub via CNAME, verification involves searching GitHub for matching custom domains and observing site behavior. If unclaimed, the site shows GitHub's default error pages. This step assumes DNS analysis from prior reconnaissance; outcomes include confirmation of vulnerability for exploitation.

## Requirements

1. GitHub account access for searches (anonymous browsing possible)
2. Web browser or curl for HTTP checks
3. DNS query tool

## Defense

Defensive measures and detection strategies:

- Monitor GitHub for custom domain associations using API queries
- Set up alerts for DNS changes via services like Cloudflare or Route 53
- Conduct periodic subdomain audits with tools like Subjack or Takeover

## Objectives

1. Search for existing GitHub claims
2. Test subdomain resolution for unclaimed indicators
3. Document vulnerability status

## Instructions

### Step 1: Search GitHub Repositories

**Context**: Manually or via GitHub search, look for repos using the custom domain.

Visit https://github.com/search?q=dev.rbk.money&type=repositories and confirm no results.

### Step 2: Check Subdomain Resolution

**Context**: Query DNS and HTTP to verify unclaimed state.

**Command** ([[commands/dig-dns-query]]):
```bash
dig dev.rbk.money
```

> Output shows GitHub IPs but no custom content. Follow with HTTP check.

**Command** ([[commands/curl-http-check]]):
```bash
curl -I https://dev.rbk.money
```

> Expect 404 or GitHub Pages error, confirming unclaimed.

### Step 3: Validate No Active Pages

**Context**: Attempt to access potential Pages URL.

Browse to https://<username>.github.io if suspected, but for custom domains, rely on error pages.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-query]]
- [[commands/curl-http-check]]

## Tools Used


## Tags

- [[github]]
- [[verification]]
