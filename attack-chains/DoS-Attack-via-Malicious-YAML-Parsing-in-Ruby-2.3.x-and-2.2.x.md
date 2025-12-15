---
id: ac-uuid-1234
name: DoS Attack via Malicious YAML Parsing in Ruby 2.3.x and 2.2.x
tags:
  - dos
  - yaml
  - ruby
  - cve-2014-9130
  - memory-corruption
type: attack_chain
tools: []
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Software
  - Ruby
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-libYAML-DoS-in-Ruby-2-3-x-and-2-2-x]]'
step_count: 1
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:36.912Z'
description: >-
  Attack chain exploiting the bundled vulnerable libYAML 0.1.6 in Ruby 2.3.x and
  2.2.x to cause denial of service through memory corruption during YAML
  parsing.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# DoS Attack via Malicious YAML Parsing in Ruby 2.3.x and 2.2.x

Multi-stage attack chain demonstrating a complete attack workflow targeting Ruby applications vulnerable to CVE-2014-9130 due to outdated libYAML.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Vulnerable Ruby Version] --> B[Provide Malicious YAML Input]
    B --> C[Trigger DoS and Memory Corruption]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#e74c3c
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard Ruby interpreter)

### Target Environment

- Ruby 2.3.x or 2.2.x installed
- Application that parses untrusted YAML input (e.g., web app, script)
- No specific services/ports required; local or remote access to Ruby process

### Initial Access Requirements

- Access to provide YAML input to the target Ruby application
- No credentials needed if input is via public endpoint; otherwise, valid user access

## Detailed Attack Procedures

### Step 1: Exploit libYAML Vulnerability
procedure: [[procedures/Exploit-libYAML-DoS-in-Ruby-2-3-x-and-2-2-x]]

**Objective**: Identify the vulnerable Ruby version and feed malicious YAML to cause memory corruption and DoS.

**Instructions**: First, verify the Ruby version using a simple check:

```bash
ruby -v
```

If it reports 2.3.x or 2.2.x, proceed to craft and provide malicious YAML input to a parsing function, such as in a test script:

Create a file `malicious.yaml` with content exploiting the integer overflow in URI escape parsing (e.g., a long string of escaped characters leading to stack overflow):

```yaml
!!str "\x09\x09\x09..."  # Repeated escapes to trigger overflow (repeat ~10000 times for effect)
```

Then, run a Ruby script to parse it:

```ruby
require 'yaml'
yaml_content = File.read('malicious.yaml')
YAML.load(yaml_content)
```

Execute with:

```bash
ruby parse_yaml.rb
```

**Expected Output**: The Ruby process crashes or hangs due to memory corruption, consuming excessive resources.

**Success Indicators**:
- Ruby process terminates unexpectedly
- High memory usage or segmentation fault observed
- Application becomes unresponsive to further requests

## Attack Chain Summary

### Key Achievements

1. Confirmed vulnerable libYAML version in target Ruby installation
2. Delivered malicious YAML input to trigger DoS
3. Achieved application denial of service via memory corruption

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]]

### MITRE ATT&CK Tactics

- [[Impact]]

---
*Last updated: 2023-10-01T00:00:00Z*
