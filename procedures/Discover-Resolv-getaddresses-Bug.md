---
id: proc-uuid-2
tags:
  - ruby
  - bug-discovery
  - resolv
type: procedure
tools:
  - '[[tools/irb]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/ruby-require-resolv]]'
  - '[[commands/ruby-resolv-getaddresses-127-000-000-1]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T03:53:38.156Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Discover-Resolv-getaddresses-Bug

## Summary

This procedure tests Ruby's Resolv.getaddresses function across different Linux environments to reveal a bug where encoded private IP addresses like '127.000.000.1' resolve to an empty array on some systems, enabling SSRF bypasses.

## Description

Ruby's native DNS resolver, Resolv.getaddresses, exhibits platform-dependent behavior when parsing octal or encoded IP formats. On certain Linux distributions, it fails to resolve these to valid IPs, returning [] instead of ["127.0.0.1"], which evades private IP checks. This procedure simulates discovery by running tests in IRB on multiple machines, highlighting variability that attackers can exploit for blind SSRF. Requires Ruby installed locally.

## Requirements

1. Multiple Linux machines or VMs with varying glibc versions
2. Ruby 2.x or later installed
3. IRB (Interactive Ruby) shell access

## Defense

Defensive measures and detection strategies:

- Patch or replace Resolv.getaddresses with consistent alternatives like Socket.getaddrinfo
- Normalize and decode all IP formats before resolution
- Log resolver calls and monitor for empty resolution attempts

## Objectives

1. Identify inconsistent resolution behavior for encoded IPs
2. Confirm bug triggers empty arrays on target-like environments
3. Document variations across systems for reliable exploitation

## Instructions

### Step 1: Prepare IRB Session

**Context**: Load the Resolv library to enable DNS resolution testing.

**Command** ([[commands/ruby-require-resolv]]):
```ruby
require 'resolv'
```

> This loads the Resolv module; expected output is no error, ready for getaddresses calls.

### Step 2: Test Encoded IP Resolution

**Context**: Execute resolution on encoded private IPs like '127.000.000.1' to observe outputs.

**Command** ([[commands/ruby-resolv-getaddresses-127-000-000-1]]):
```ruby
Resolv.getaddresses('127.000.000.1')
```

> On buggy machines, returns []; on others, ["127.0.0.1"]. Repeat for '0177.1' and '0x7f.1'.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used

- [[commands/ruby-require-resolv]]
- [[commands/ruby-resolv-getaddresses-127-000-000-1]]

## Tools Used

- [[tools/irb]]

## Tags

- ruby
- bug-discovery
