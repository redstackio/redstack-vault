---
tags:
  - ssrf
  - bypass
  - ruby
  - hackerone
  - internal-access
type: attack_chain
tools:
  - '[[tools/IRB]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/require-private-address-check]]'
  - '[[commands/private-address-check-0.0.0.0]]'
platforms:
  - Web
  - Ruby
complexity: medium
procedures:
  - '[[procedures/Test-Private-Address-Check-Gem-Bypass]]'
  - '[[procedures/Exploit-HackerOne-SSRF-with-0.0.0.0]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  A two-step attack chain exploiting a flaw in the private_address_check Ruby
  gem to bypass SSRF protections in HackerOne's integrations feature, allowing
  access to internal localhost services like port 22.
skill_level: intermediate
impact_level: high
id: 80090d09-a8c7-435d-b7bf-7e6b837a493f
created_at: '2025-12-14T04:08:54.885Z'
updated_at: '2025-12-14T04:08:54.885Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# HackerOne SSRF Bypass via 0.0.0.0 Private Address Check Flaw

Multi-stage attack chain demonstrating exploitation of a flaw in the private_address_check Ruby gem used by HackerOne for SSRF filtering. The gem fails to classify 0.0.0.0 as a private address, allowing attackers to bypass restrictions and access internal netblocks like localhost on port 22, potentially exposing sensitive internal services.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Test Gem Flaw] --> B[Exploit SSRF Bypass]
    B --> C[Access Internal Services]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/IRB]]

### Target Environment

- Web platform with HackerOne integrations feature
- Ruby environment for testing the private_address_check gem
- Required services/ports: Port 22 (SSH) on localhost
- Network access requirements: Ability to submit requests to HackerOne's SSRF endpoint

### Initial Access Requirements

- Access to HackerOne platform (e.g., via authenticated session or public endpoint)
- Network position: External attacker
- Prior access needed: None, but knowledge of the integrations feature

## Detailed Attack Procedures

### Step 1: Test Private Address Check Gem
procedure: [[procedures/Test-Private-Address-Check-Gem-Bypass]]

**Objective**: Verify the flaw in the private_address_check gem by loading it in IRB and checking if 0.0.0.0 is recognized as a private address.

**Instructions**: Launch IRB and execute the following commands to test the gem's behavior.

First, load the gem using [[commands/require-private-address-check]]:

```ruby
require 'private_address_check'
```

Expected output: `true` (gem loaded successfully).

Then, test the private address check using [[commands/private-address-check-0.0.0.0]]:

```ruby
PrivateAddressCheck.private_address?("0.0.0.0")
```

Expected output: `false`, confirming the bypass flaw as 0.0.0.0 is not classified as private.

**Expected Output**: Gem loads and returns false for 0.0.0.0, indicating the vulnerability.

**Success Indicators**:
- Gem loads without errors
- `private_address?` returns false for 0.0.0.0

### Step 2: Exploit SSRF Bypass
procedure: [[procedures/Exploit-HackerOne-SSRF-with-0.0.0.0]]

**Objective**: Submit a malicious URL to HackerOne's SSRF endpoint in the integrations feature to access internal localhost services.

**Instructions**: Using a tool like curl or a browser, submit a request to the HackerOne SSRF endpoint (typically in the integrations configuration) with the URL parameter set to `http://0.0.0.0:22/`. This evades the filter due to the gem flaw and probes internal port 22.

Example request (adapt to the exact endpoint, e.g., via POST to integrations webhook setup):

```bash
curl -X POST 'https://hackerone.com/integrations/webhook' -d 'url=http://0.0.0.0:22/'
```

**Expected Output**: Response indicating access to internal service, such as SSH banner or error revealing internal network details.

**Success Indicators**:
- Request accepted without private address rejection
- Internal service response (e.g., port 22 connection details)
- Potential information disclosure from localhost

## Attack Chain Summary

### Key Achievements

1. Identified and verified the private_address_check gem flaw using IRB testing.
2. Bypassed SSRF protections to access internal netblocks like localhost:22.
3. Demonstrated potential for broader internal network reconnaissance or exploitation.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01*
