---
tags:
  - username-enumeration
  - timing-attack
  - ssh
  - openssh
  - cve-2016-6210
  - information-disclosure
type: attack_chain
tools:
  - '[[tools/POC-py-for-CVE-2016-6210]]'
tactics:
  - '[[Discovery]]'
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Download-OpenSSH-Username-Enumeration-POC-Script]]'
  - '[[procedures/Prepare-Username-List-for-Enumeration]]'
  - '[[procedures/Execute-Username-Enumeration-on-Newsletter-Subdomain]]'
  - '[[procedures/Extend-Enumeration-to-Additional-Nextcloud-Subdomains]]'
step_count: 4
techniques:
  - '[[Account Discovery]]'
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:30:58.949Z'
description: >-
  Multi-stage attack chain exploiting CVE-2016-6210 in OpenSSH 7.2p2 to
  enumerate valid usernames on Nextcloud subdomains through timing discrepancies
  in SSH authentication responses.
id: 201fd4c8-2b60-497d-ad91-db6a6ce016da
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Active Scanning]]'
---
# Timing-Based Username Enumeration via OpenSSH Authentication on Nextcloud Subdomains

Multi-stage attack chain demonstrating a complete reconnaissance workflow to enumerate valid usernames on Nextcloud subdomains using a timing-based side-channel attack in OpenSSH 7.2p2 (CVE-2016-6210). The attack leverages differences in SSH authentication response times when attempting logins with a large password against existing versus non-existing usernames, enabling remote information disclosure without credentials.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5-10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Download POC Script] --> B[Prepare Username List]
    B --> C[Enumerate on Primary Target]
    C --> D[Extend to Additional Targets]
    D --> E[Analyze Results for Valid Users]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/POC-py-for-CVE-2016-6210]]

### Target Environment

- Linux-based SSH servers running OpenSSH 7.2p2
- Exposed SSH service on ports 22 (default)
- Network access to Nextcloud subdomains: newsletter.nextcloud.com, stats.nextcloud.com, help.nextcloud.com, lists.nextcloud.com, nextcloud.com

### Initial Access Requirements

- No credentials required
- Direct network connectivity to targets (no prior access needed)
- Python 2/3 environment for script execution

## Detailed Attack Procedures

### Step 1: Download POC Script
procedure: [[procedures/Download-OpenSSH-Username-Enumeration-POC-Script]]

**Objective**: Obtain the exploit script necessary for performing the timing-based enumeration attack.

**Instructions**: Access the Exploit-DB repository and download the POC.py script, which implements the timing measurement for SSH authentication attempts.

**Expected Output**: POC.py file saved locally.

**Success Indicators**:
- Script downloaded successfully
- File integrity verified (e.g., via checksum if available)

### Step 2: Prepare Username List
procedure: [[procedures/Prepare-Username-List-for-Enumeration]]

**Objective**: Create or source a list of potential usernames to test against the target SSH servers.

**Instructions**: Generate a text file containing usernames, starting with common ones for testing and expanding to larger wordlists like rockyou.txt for comprehensive enumeration.

**Expected Output**: usernames.txt file with one username per line.

**Success Indicators**:
- List file created with at least 10-100 entries for initial testing
- No formatting errors (plain text, no duplicates)

### Step 3: Enumerate on Primary Target
procedure: [[procedures/Execute-Username-Enumeration-on-Newsletter-Subdomain]]

**Objective**: Run the enumeration against the initial vulnerable subdomain to identify valid usernames based on response times.

**Instructions**: Execute the POC script using [[commands/python-poc-py-username-enumeration-newsletter-nextcloud-com]] to attempt SSH logins with a large password and measure timings.

```bash
python POC.py newsletter.nextcloud.com -U usernames.txt
```

**Expected Output**: Console output listing usernames and their response times; times below ~0.047s indicate non-existing users.

**Success Indicators**:
- Script completes without errors
- Valid usernames identified (higher response times)

### Step 4: Extend to Additional Targets
procedure: [[procedures/Extend-Enumeration-to-Additional-Nextcloud-Subdomains]]

**Objective**: Apply the same enumeration technique to other affected subdomains to broaden the reconnaissance scope.

**Instructions**: Re-run the POC script on additional hosts using [[commands/python-poc-py-username-enumeration-stats-nextcloud-com]], [[commands/python-poc-py-username-enumeration-help-nextcloud-com]], [[commands/python-poc-py-username-enumeration-lists-nextcloud-com]], and [[commands/python-poc-py-username-enumeration-nextcloud-com]].

For example:

```bash
python POC.py stats.nextcloud.com -U usernames.txt
python POC.py help.nextcloud.com -U usernames.txt
python POC.py lists.nextcloud.com -U usernames.txt
python POC.py nextcloud.com -U usernames.txt
```

**Expected Output**: Per-target output with response times; compile results to identify overlapping valid usernames across subdomains.

**Success Indicators**:
- Enumeration successful on all targets
- List of valid usernames compiled for further attacks (e.g., brute-force)

## Attack Chain Summary

### Key Achievements

1. Successfully downloaded and prepared tools for OpenSSH timing attack
2. Enumerated valid usernames on newsletter.nextcloud.com via response time analysis
3. Extended discovery to four additional subdomains, revealing potential account overlaps
4. Enabled targeted follow-on attacks like password brute-forcing

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]] Account Discovery
- [[Active Scanning]] Active Scanning

### MITRE ATT&CK Tactics

- [[Discovery]] Discovery
- [[Reconnaissance]] Reconnaissance

---
*Last updated: 2023-10-01T00:00:00Z*
