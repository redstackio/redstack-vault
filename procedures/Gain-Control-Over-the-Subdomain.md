---
tags:
  - subdomain-control
  - phishing-hosting
  - malicious-content
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T04:51:10.581Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 5b1a5fd4-bf23-485c-8789-4cc4c5fa68d6
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Gain Control Over the Subdomain

## Summary

This procedure deploys custom content on the claimed UserVoice instance, redirecting the original subdomain to attacker-controlled pages for phishing or exploitation.

## Description

Once claimed, the UserVoice dashboard allows customization of feedback.screenhero.com content. Attackers can clone legitimate sites, add phishing forms for credential theft, inject JavaScript for cookie stealing, or set redirects to malicious domains, damaging trust in the brand.

## Requirements

1. Active UserVoice account from claim step
2. Basic web development knowledge for content setup
3. Target subdomain CNAME intact

## Defense

Defensive measures and detection strategies:

- Implement certificate pinning or HSTS to detect subdomain hijacks
- Monitor for unexpected content changes on subdomains via web scanners
- Educate on phishing risks from acquired domains

## Objectives

1. Host phishing or malicious payloads under trusted subdomain
2. Steal user credentials or session data
3. Achieve reputational harm or redirects to attacker sites

## Instructions

### Step 1: Access UserVoice Dashboard

**Context**: Log in to configure the claimed instance.

Navigate to your UserVoice admin panel post-signup.

### Step 2: Customize and Deploy Content

**Context**: Upload or edit site elements to serve malicious content, which propagates to feedback.screenhero.com via the CNAME.

Add custom HTML/JS for phishing forms or redirects (e.g., <script>window.location='http://attacker.com';</script>).

**Expected Output**: Subdomain loads attacker content when visited.

### Step 3: Verify Control

**Context**: Test the subdomain to confirm resolution to your content.

Browse to https://feedback.screenhero.com and observe the deployed page.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[phishing-hosting]]
- [[subdomain-control]]
