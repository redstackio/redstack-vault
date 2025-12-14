---
tags:
  - rce
  - deserialization
  - ruby
type: procedure
tools:
  - '[[tools/Ruby]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/ruby-create-rce-payload]]'
verified: false
platforms:
  - Ruby
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:41.244Z'
sub_techniques: []
id: 550e9613-25bc-4be8-8053-aca062580417
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Prepare-Malicious-Marshal-Payload-for-Ruby-Deserialization-RCE

## Summary

This procedure creates a malicious Marshal-serialized payload using Ruby gadget chains to execute arbitrary commands upon deserialization, targeting Bundler's unsafe loading of dependencies from the RubyGems /api/v1/dependencies endpoint.

## Description

The attack leverages known Ruby deserialization vulnerabilities by constructing a chain with classes such as Gem::SpecFetcher, Gem::Installer, Gem::Requirement, Net::WriteAdapter, and Gem::RequestSet. When Bundler calls Marshal.load on the response, it triggers Kernel.system('date'), demonstrating RCE. This is based on reviewing RubyGems.org source and existing exploits.

## Requirements

1. Ruby environment installed (version 2.7+ recommended)
2. Knowledge of Ruby deserialization gadgets
3. Local file system access to write the script

## Defense

Defensive measures and detection strategies:

- Use safe deserialization libraries or switch to JSON for RubyGems responses
- Validate gem sources and use trusted mirrors only
- Monitor for anomalous command executions in Bundler processes

## Objectives

1. Generate a functional gadget chain for RCE
2. Output the payload as a string for server integration
3. Verify payload integrity before deployment

## Instructions

### Step 1: Create the Payload Script

**Context**: Write a Ruby script (create_rce.rb) that builds the deserialization chain to invoke system('date').

**Command** ([[commands/ruby-create-rce-payload]]):
```bash
ruby create_rce.rb
```

> This executes the script, dumping the Marshal payload to stdout. Expected output is the escaped string like "\\x04\\b\\[\\bc\\x15Gem::SpecFetcher..." containing the gadget invoking Kernel.system('date').

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used

- [[commands/ruby-create-rce-payload]]

## Tools Used

- [[tools/Ruby]]

## Tags

- rce
- deserialization
- ruby
