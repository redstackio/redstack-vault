---
tags:
  - crossdomain
  - flash
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:36.192Z'
sub_techniques: []
id: 89e31ec8-b50e-4505-bbf1-12ed6d8a6b5f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Host Malicious Crossdomain Policy

## Summary

Host a crossdomain.xml file on an attacker-controlled domain to permit Flash cross-origin requests to the target site, enabling header forgery.

## Description

Flash SWF files respect crossdomain policies for cross-origin access. By hosting a permissive crossdomain.xml, the attacker allows their Flash to interact with https://my.stripo.email/, bypassing some browser restrictions in older environments.

## Requirements

1. Web hosting access (e.g., thehackerblog.com)
2. Basic XML knowledge
3. Victim's browser supports Flash (legacy)

## Defense

Defensive measures and detection strategies:

- Disable Flash in browsers
- Block or audit crossdomain.xml files
- Use Content-Security-Policy (CSP) to restrict Flash

## Objectives

1. Enable Flash cross-origin access
2. Prepare for header forging
3. Avoid same-origin policy blocks

## Instructions

### Step 1: Create crossdomain.xml

**Context**: Define policy allowing access to target domain.

Create file with content:

```xml
<?xml version="1.0"?>
<cross-domain-policy>
    <allow-access-from domain="*" />
</cross-domain-policy>
```

> Upload to https://thehackerblog.com/crossdomain/.

### Step 2: Verify Policy

**Context**: Test if policy loads.

Visit https://thehackerblog.com/crossdomain/crossdomain.xml in browser.

> Expected: XML displays without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[crossdomain]]
- [[flash]]
