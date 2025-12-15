---
id: proc-webrick-source-analysis
tags:
  - redos
  - source-analysis
  - ruby
type: procedure
tools:
  - '[[tools/Ruby]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Ruby
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:31:19.609Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Analyze WEBrick DigestAuth Source for ReDoS

## Summary

This procedure involves reviewing the source code of Ruby's WEBrick::HTTPAuth::DigestAuth to identify a ReDoS vulnerability in the split_param_value method, focusing on a regex pattern susceptible to catastrophic backtracking.

## Description

The attack scenario targets the private method split_param_value in lib/webrick/httpauth/digestauth.rb at line 295. The regex ^\s*([\w-.*\%!"+)=\s*"((.|\[^"])*"\s*,? uses nested quantifiers and alternations that can lead to exponential time complexity on inputs with repeated patterns like \b. Prerequisites include access to Ruby source code via GitHub or local installation. Expected outcome is confirmation of the vulnerability for further exploitation planning.

## Requirements

1. Ruby source code access (e.g., via git clone https://github.com/ruby/ruby.git)
2. Text editor or IDE for code review
3. Basic knowledge of regular expressions and backtracking

## Defense

Defensive measures and detection strategies:

- Use static analysis tools like Brakeman or regex checkers to scan for ReDoS-prone patterns
- Implement regex timeout mechanisms in Ruby applications
- Monitor CPU usage spikes during authentication processing

## Objectives

1. Identify vulnerable regex in DigestAuth parsing
2. Document backtracking risks
3. Prepare for payload crafting

## Instructions

### Step 1: Access Source Code

**Context**: Locate the WEBrick DigestAuth implementation.

Navigate to lib/webrick/httpauth/digestauth.rb in the Ruby source repository.

### Step 2: Examine split_param_value Method

**Context**: Analyze the regex at line 295 for catastrophic backtracking.

Review the pattern ^\s*([\w-.*\%!"+)=\s*"((.|\[^"])*"\s*,?. Test it mentally or with a regex tool on inputs like repeated \b to simulate backtracking.

> The regex allows alternations inside quantifiers, leading to exponential trials on crafted strings.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Ruby]]

## Tags

- redos
- source-analysis
