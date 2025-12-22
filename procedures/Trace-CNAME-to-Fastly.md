---
tags:
  - dns
  - cname
  - fastly
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dns-query]]'
verified: false
platforms:
  - DNS
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:51:26.668Z'
sub_techniques: []
id: fc2fc7f5-1adf-4b74-a9cd-0c1be728ee8a
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Trace-CNAME-to-Fastly

## Summary

This procedure traces a CNAME chain from a subdomain to underlying CDN infrastructure, such as Fastly, to identify service-specific vulnerabilities.

## Description

Following initial DNS discovery, this step chains queries to map the full resolution path. In the Node.js case, it reveals registry.npmjs.org aliasing to a.sni.fastly.net, highlighting Fastly's role and potential for subdomain-specific config issues. Outcomes include confirmation of CDN dependency and setup for gap verification.

## Requirements

1. Results from prior DNS query (e.g., intermediate domain like registry.npmjs.org)
2. DNS query tool access
3. Basic understanding of CDN architectures

## Defense

Defensive measures and detection strategies:

- Monitor CNAME chains in DNS audits to prevent orphaned pointers
- Configure CDNs to require explicit domain verification for all aliases
- Use tools like subjack to scan for takeover risks proactively

## Objectives

1. Follow the CNAME to the CDN endpoint
2. Confirm infrastructure provider (e.g., Fastly)
3. Prepare for service configuration checks

## Instructions

### Step 1: Query Next CNAME

**Context**: Use the discovered alias to trace further.

**Command** ([[commands/dig-dns-query]]):
```bash
dig registry.npmjs.org CNAME
```

> Output should show "registry.npmjs.org. 300 IN CNAME a.sni.fastly.net." indicating Fastly involvement.

### Step 2: Resolve Final Endpoint

**Context**: Verify the CDN's resolution.

**Command** ([[commands/dig-dns-query]]):
```bash
dig a.sni.fastly.net
```

> Expect A records pointing to Fastly IPs, confirming the chain ends at their infrastructure.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- None

## Commands Used

- [[commands/dig-dns-query]]

## Tools Used

- None

## Tags

- [[DNS]]
- [[fastly]]
