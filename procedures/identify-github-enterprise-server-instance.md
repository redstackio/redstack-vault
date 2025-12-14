---
tags:
  - reconnaissance
  - github-enterprise
  - instance-discovery
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:24:08.741Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 255e5344-0b90-4cad-8443-847b271dd29f
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify GitHub Enterprise Server Instance

## Summary

This procedure involves locating a target GitHub Enterprise Server instance through domain enumeration and verification of ownership, enabling subsequent vulnerability assessment.

## Description

In the context of targeting development environments, attackers search for staging or dev instances of GitHub Enterprise Servers associated with organizations like Imgur. By identifying URLs such as https://git.imgur-dev.com/, ownership is confirmed via SSL certificates and public repository contents revealing sensitive source code. This reconnaissance step sets the foundation for exploiting known vulnerabilities without requiring authentication.

## Requirements

1. Internet access to perform domain lookups and web browsing
2. Basic knowledge of SSL certificate inspection tools or browser dev tools
3. Awareness of common naming conventions for dev instances (e.g., -dev.com)

## Defense

Defensive measures and detection strategies:

- Restrict public access to dev instances behind firewalls or VPNs
- Monitor for anomalous traffic to internal GitHub instances from external IPs
- Use certificate transparency logs to detect exposed subdomains early

## Objectives

1. Discover the exact URL of the GitHub Enterprise dev instance
2. Confirm it hosts the target's source code repositories
3. Establish it as a viable attack surface

## Instructions

### Step 1: Enumerate Potential Domains

**Context**: Use search engines or OSINT techniques to find development subdomains.

Search for "git.imgur-dev" or similar patterns in public sources. Access the URL https://git.imgur-dev.com/ in a web browser.

> Expected output: A GitHub Enterprise login or dashboard page loads.

### Step 2: Verify Ownership

**Context**: Inspect elements to confirm association with the target organization.

Check the SSL certificate details for the domain owner (e.g., Imgur). Browse to public repositories and look for Imgur-specific code or project names.

> Expected output: Certificate issuer matches Imgur, repositories contain Imgur source code.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[github-enterprise]]
