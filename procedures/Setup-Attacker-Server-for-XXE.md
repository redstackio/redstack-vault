---
tags:
  - xxe
  - server-setup
type: procedure
tools:
  - '[[tools/Ruby]]'
  - '[[tools/Sinatra]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/gem-install-sinatra]]'
  - '[[commands/ruby-server-rb]]'
platforms:
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: ceb78735-4ee9-4c7b-9e68-ca2ca1326ad5
created_at: '2025-12-13T09:00:27.304Z'
updated_at: '2025-12-13T09:00:27.304Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup Attacker Server for XXE

## Summary

This procedure sets up a malicious web server using Ruby and Sinatra to host files that exploit XXE vulnerabilities in web crawlers, enabling external entity injection for file exfiltration.

## Description

The attacker creates a simple web server that serves a robots.txt pointing to a crafted sitemap.xml with external entities. When parsed by vulnerable crawlers, it loads a DTD from the server and exfiltrates local file contents to an endpoint. This targets insecure XML parsing in applications like Elastic App Search.

## Requirements

1. Ruby installed on the attacker machine
2. Network-accessible domain or IP for the server
3. Ability to bind to port 80/443

## Defense

Defensive measures and detection strategies:

- Disable external entity processing in XML parsers
- Monitor for unusual outbound requests from servers

## Objectives

1. Host malicious sitemap for XXE trigger
2. Capture exfiltrated data
3. Confirm vulnerability exploitation

## Instructions

### Step 1: Install Sinatra

**Context**: Install the required web framework for the server.

**Command** ([[commands/gem-install-sinatra]]):
```bash
gem install sinatra
```

> Installs Sinatra gem; expect success message.

### Step 2: Run Server Script

**Context**: Launch the server with routes for malicious files.

**Command** ([[commands/ruby-server-rb]]):
```bash
ruby server.rb
```

> Starts Sinatra server; logs show routes and incoming requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/gem-install-sinatra]]
- [[commands/ruby-server-rb]]

## Tools Used

- [[tools/Ruby]]
- [[tools/Sinatra]]

## Tags

- [[xxe]]
- [[server-setup]]
