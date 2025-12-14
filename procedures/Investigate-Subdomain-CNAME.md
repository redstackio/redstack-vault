---
id: proc-uuid-investigate-cname
tags:
  - dns-investigation
  - cname-check
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:38:49.618Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Investigate-Subdomain-CNAME

## Summary

This procedure details the investigation of a suspicious subdomain to confirm a dangling CNAME record, as seen with creatorforum.roblox.com pointing to an unclaimed Discourse instance.

## Description

Accessing the subdomain in a browser reveals an inactive setup, and DNS queries confirm the CNAME points to a nonexistent Discourse site. This misconfiguration allows takeover if the attacker has a Discourse account, enabling control over the .roblox.com subdomain for malicious activities.

## Requirements

1. Web browser for accessing the subdomain
2. DNS query capability (e.g., browser dev tools or command-line tools)
3. Understanding of CNAME records and third-party services like Discourse

## Defense

Defensive measures and detection strategies:

- Scan for dangling DNS records periodically with tools like dnsdumpster or custom scripts
- Remove or re-point unused CNAMEs to null or internal sinks
- Integrate with third-party service APIs to detect unclaimed pointers

## Objectives

1. Confirm the subdomain's DNS configuration
2. Identify if it's claimable by external services
3. Assess potential impact on domain trust

## Instructions

### Step 1: Access Subdomain in Browser

**Context**: Visually inspect the subdomain's response to detect inactive services.

Navigate to creatorforum.roblox.com in a browser. Observe if it loads a Discourse error page or setup prompt indicating inactivity.

**Expected Output**: Page shows "This Discourse instance is not configured" or similar.

### Step 2: Query DNS CNAME Record

**Context**: Extract the underlying DNS pointer to verify the dangling nature.

Use browser developer tools (Network tab) or a DNS tool to query the CNAME for creatorforum.roblox.com. Confirm it points to a Discourse-hosted domain that's unclaimed.

**Expected Output**: CNAME record like creatorforum.roblox.com -> some.discourse.org (nonexistent).

### Step 3: Validate Takeover Feasibility

**Context**: Check if the pointed service allows claiming the custom domain.

Review Discourse documentation or test with a similar setup to confirm that a free account can claim the subdomain.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[dns-investigation]]
- [[cname-check]]
- [[subdomain-takeover]]
