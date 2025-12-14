---
id: ac-uuid-001
tags:
  - rce
  - deserialization
  - yaml
  - ruby
  - rdoc
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Ruby
submitted: true
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-RDoc-YAML-Deserialization-for-RCE]]'
step_count: 1
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:24:07.907Z'
description: >-
  Attack chain exploiting CVE-2024-27281 in RDoc for remote code execution
  through unsafe YAML deserialization in configuration files.
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# RCE via Unsafe YAML Deserialization in RDoc .rdoc_options File

Multi-stage attack chain demonstrating a complete attack workflow exploiting CVE-2024-27281 in RDoc versions 6.3.3 through 6.6.2, bundled with Ruby 3.x through 3.3.0. The vulnerability allows remote code execution via unsafe YAML deserialization in the .rdoc_options file, enabling object injection when the 'rdoc' command is executed on untrusted repositories containing a crafted file. Discovered by researcher ooooooo_q and reported on March 27, 2024, this chain focuses on crafting and triggering the exploit in a Ruby development environment.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare Malicious Repository] --> B[Execute RDoc on Untrusted Input]
    B --> C[Trigger RCE via Deserialization]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (built-in Ruby tools)

### Target Environment

- Ruby 3.x through 3.3.0 with RDoc 6.3.3 through 6.6.2
- Access to a Ruby development setup
- Untrusted repository or documentation cache

### Initial Access Requirements

- Local or remote access to execute Ruby commands
- No specific credentials needed; assumes developer workflow
- Prior access to clone or access a repository

## Detailed Attack Procedures

### Step 1: Trigger RCE via Crafted .rdoc_options
procedure: [[procedures/Exploit-RDoc-YAML-Deserialization-for-RCE]]

**Objective**: Execute the rdoc command on a repository containing a crafted .rdoc_options file to achieve remote code execution through unsafe YAML deserialization.

**Instructions**: First, prepare a malicious .rdoc_options file with YAML payload that injects objects leading to RCE, such as using a class that executes system commands upon deserialization. Place this file in an untrusted repository. Then, run the [[commands/rdoc-generate-documentation]] command on the repository directory:

```bash
rdoc
```

This parses the .rdoc_options as YAML without class restrictions, triggering object injection and RCE. Alternatively, load a crafted documentation cache file to bypass repository access.

**Expected Output**: Successful RCE, such as execution of injected commands (e.g., spawning a shell or running arbitrary code), visible in command output or system processes.

**Success Indicators**:
- Arbitrary code executes (e.g., 'whoami' output or file creation)
- No parsing errors; documentation generation starts but deviates due to injection

## Attack Chain Summary

### Key Achievements

1. Achieved RCE in Ruby documentation generation workflow
2. Exploited unsafe deserialization in .rdoc_options and cache files
3. Demonstrated impact on developers processing untrusted repos

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2024-10-01T00:00:00Z*
