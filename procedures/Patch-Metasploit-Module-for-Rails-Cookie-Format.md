---
tags:
  - metasploit
  - patch
  - rails
type: procedure
tools:
  - '[[tools/Metasploit-Framework]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:54.960Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 30e97062-861f-4456-8ed6-0dbc655856ab
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Patch-Metasploit-Module-for-Rails-Cookie-Format

## Summary

This procedure modifies the Metasploit rails_secret_deserialization module to correctly parse session cookies with hyphens, adapting it for the target's specific format to enable successful exploitation.

## Description

The default Metasploit module's regex fails on cookies containing '-', common in Rails apps. Edit the Ruby file to update the pattern. Requires Metasploit installed and basic Ruby knowledge. Outcome: A functional exploit module tailored to the vulnerability.

## Requirements

1. Metasploit Framework installed
2. Text editor for Ruby files
3. Knowledge of regex patterns

## Defense

Defensive measures and detection strategies:

- Keep Rails apps updated to versions without deserialization flaws (Rails 5+)
- Monitor for modified Metasploit modules or anomalous traffic to /auth endpoints
- Use WAF rules to block suspicious cookie payloads

## Objectives

1. Adapt exploit to target cookie structure
2. Ensure compatibility with Rails 4 CookieStore
3. Prepare for RCE payload injection

## Instructions

### Step 1: Locate the Module File

**Context**: Find the exploit script in Metasploit.

Path: /usr/share/metasploit-framework/modules/exploits/multi/http/rails_secret_deserialization.rb

### Step 2: Edit the Regex Pattern

**Context**: Update to handle hyphens in cookie names.

Change line with regex from:

```ruby
/(\[_A-Za-z0-9\]+)=(\[A-Za-z0-9%\]*)--(\[0-9A-Fa-f\]+);/
```

to:

```ruby
/(\[_A-Za-z0-9\\-\]+)=(\[A-Za-z0-9%\]*)--(\[0-9A-Fa-f\]+);/
```

> Expected output: No syntax errors on module load.

### Step 3: Save and Test Load

**Context**: Verify the patch.

Reload Metasploit and load the module.

> Expected output: Module loads successfully.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Metasploit-Framework]]

## Tags

- metasploit
- rails
- deserialization
