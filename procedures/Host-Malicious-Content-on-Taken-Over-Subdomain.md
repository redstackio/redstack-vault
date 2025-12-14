---
tags:
  - subdomain-takeover
  - phishing
  - webflow
  - malware
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:23.968Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: d7c42fd6-1c6c-442f-8e1f-a96069afa4ea
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Host-Malicious-Content-on-Taken-Over-Subdomain

## Summary

This procedure details claiming a dangling subdomain via Webflow and hosting malicious content, such as a phishing login page, to exploit user traffic and steal credentials or distribute malware.

## Description

Following account registration, the attacker creates a site in Webflow and adds the target's subdomain (e.g., learnstormindia.khanacademy.org) as a custom domain. The CNAME record (pointing to proxy-ssl.webflow.com) allows Webflow to recognize and serve the attacker's content. Impacts include phishing for Khan Academy credentials, XSS via injected scripts, or malware downloads, potentially affecting users who bookmark or are redirected to the subdomain. Propagation occurs within minutes of domain verification, with the original 404 response replaced by the attacker's page. A paid Webflow plan is required for this functionality.

## Requirements

1. Active Webflow account with paid plan for custom domains.
2. Knowledge of the target's dangling CNAME (verifiable via dig or nslookup).
3. Basic web design skills to create convincing phishing pages.

## Defense

Defensive measures and detection strategies:

- Use DNS monitoring tools to alert on unresolved CNAMEs returning 404s.
- Enforce strict subdomain management and periodic sweeps for takeovers using services like SecurityTrails.
- Educate users on verifying URLs and implement HSTS to prevent MITM on subdomains.

## Objectives

1. Claim and control the subdomain to serve attacker-controlled content.
2. Deploy phishing or malicious payloads to capture sensitive data.
3. Achieve high impact through user deception on a trusted domain.

## Instructions

### Step 1: Create New Site in Webflow

**Context**: Set up a hosting environment for the malicious content.

In the Webflow dashboard, click 'New Site' and choose a blank template.

> This creates a project where you can design pages; no code required, use the visual editor.

### Step 2: Design Malicious Webpage

**Context**: Build a fake interface to mimic the target (e.g., Khan Academy login).

Use Webflow's designer to add HTML elements like forms for username/password, styled to match Khan Academy's branding. Include JavaScript for credential exfiltration (e.g., POST to attacker's server).

> For phishing, add a form that submits to a controlled endpoint; test locally in Webflow preview.

### Step 3: Add Custom Domain

**Context**: Associate the target's subdomain with the site to claim it.

Go to Site Settings > Custom Domains, enter learnstormindia.khanacademy.org, and follow Webflow's verification (it checks the existing CNAME).

> Webflow will detect the dangling record and claim it; wait 5-10 minutes for DNS propagation.

### Step 4: Publish and Verify

**Context**: Deploy the content and confirm takeover.

Click 'Publish' in the dashboard. Access https://learnstormindia.khanacademy.org to verify it loads the new page instead of 404.

> Use browser dev tools or curl to check response; successful takeover shows 200 OK with attacker content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[Phishing]]
- [[webflow]]
- [[Malware]]
