---
id: proc-recon-subdomains
tags:
  - reconnaissance
  - subdomains
  - web
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
updated_at: '2025-12-14T03:47:18.656Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Reconnaissance on Target Subdomains

## Summary

This procedure involves enumerating and examining outscope subdomains of a target domain to identify potential entry points or assets, such as cache manifests referencing vulnerable files. It is a foundational step in web vulnerability assessments to expand the attack surface.

## Description

In the context of web security testing, reconnaissance on subdomains like *.pinion.gg helps uncover hidden or out-of-scope assets. By inspecting files like cache manifests (e.g., motd2.manifest on templ4d2.pinion.gg), attackers can discover embedded resources such as outdated SWF files. This passive reconnaissance requires no special tools beyond a web browser and leverages public accessibility. Expected outcomes include a list of subdomains and referenced assets, setting the stage for vulnerability identification. Prerequisites include public access to the target domain and basic web navigation skills.

## Requirements

1. Public network access to target domain and subdomains
2. Web browser with developer tools for file inspection
3. Knowledge of common web asset types (e.g., manifests, SWFs)

## Defense

Defensive measures and detection strategies:

- Implement subdomain takeover monitoring and wildcard DNS restrictions
- Use web application firewalls (WAFs) to log anomalous reconnaissance traffic
- Regularly audit and remove unused subdomains

## Objectives

1. Discover outscope subdomains to broaden attack surface
2. Identify files referencing potential vulnerabilities
3. Gather intelligence on embedded assets like Flash content

## Instructions

### Step 1: Enumerate Subdomains

**Context**: Manually or semi-automatically list subdomains using known techniques like certificate transparency logs or brute-forcing common names.

No specific command; use browser to search for subdomains like templ4d2.pinion.gg.

> Focus on web-facing subdomains and access their root or common paths.

### Step 2: Examine Files for Assets

**Context**: Inspect discovered files, such as cache manifests, for references to external resources.

Access http://templ4d2.pinion.gg/motd2.manifest and review contents.

> Look for lines referencing SWF files or other embeddable content.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[subdomains]]
