---
tags:
  - dos
  - hash-collision
  - algorithmic-complexity
  - markdown-parser
type: attack_chain
tools:
  - '[[tools/Snudown]]'
  - '[[tools/HighwayHash]]'
  - '[[tools/SipHash]]'
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Review-Snudown-Source-Code]]'
  - '[[procedures/Identify-Hash-Table-Weaknesses]]'
  - '[[procedures/Generate-Malicious-Markdown-Inputs]]'
  - '[[procedures/Test-Locally-with-Proof-of-Concept]]'
  - '[[procedures/Reproduce-on-Live-Reddit]]'
step_count: 5
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:49.051Z'
description: >-
  Multi-stage attack chain exploiting hash table weaknesses in Reddit's Snudown
  markdown parser to cause algorithmic complexity-based denial-of-service
  through collisions and duplicates.
skill_level: intermediate
impact_level: high
id: 855c314f-ed03-421c-bcee-bb5a05c035de
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
  - '[[Exploit Public-Facing Application]]'
---
# Hash-Collision Denial-of-Service in Reddit's Snudown Markdown Parser

Multi-stage attack chain demonstrating the discovery and exploitation of hash table vulnerabilities in Reddit's Snudown markdown parser, leading to denial-of-service via algorithmic complexity attacks.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Source Code Review] --> B[Weakness Identification]
    B --> C[Malicious Input Generation]
    C --> D[Local Testing]
    D --> E[Live Reproduction]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Snudown]]

### Target Environment

- Web platform with Snudown markdown parser (e.g., Reddit's comment system)
- Access to source code on GitHub
- Local build environment for C (gcc or similar)

### Initial Access Requirements

- Public access to GitHub repository
- Ability to send private messages on Reddit for live testing
- No special credentials needed beyond standard user account

## Detailed Attack Procedures

### Step 1: Source Code Review
procedure: [[procedures/Review-Snudown-Source-Code]]

**Objective**: Analyze the Snudown markdown parser source to understand its reference link handling.

**Instructions**: Clone the Snudown repository from GitHub and examine the markdown.c file, focusing on the hash_link_ref function.

**Expected Output**: Identification of key functions and data structures in the hash table implementation.

**Success Indicators**:
- Source code downloaded and reviewed
- Hash table operations understood

### Step 2: Weakness Identification
procedure: [[procedures/Identify-Hash-Table-Weaknesses]]

**Objective**: Pinpoint flaws in the hash table, including weak hashing and lack of duplicate checks.

**Instructions**: Review lines 176, 188, 205, and 213 in markdown.c to note the SDBM hash usage, insertion without duplicates, and hash-only equality.

**Expected Output**: Documented weaknesses enabling collisions and duplicates.

**Success Indicators**:
- Weak SDBM hash confirmed
- Duplicate insertion and equality issues identified

### Step 3: Malicious Input Generation
procedure: [[procedures/Generate-Malicious-Markdown-Inputs]]

**Objective**: Craft markdown inputs that exploit hash collisions and duplicates to degrade performance.

**Instructions**: Generate strings with colliding hashes (e.g., same modulus for table size) or duplicates, formatted as multiple [ref]: /url definitions followed by [ref] uses.

**Expected Output**: Proof-of-concept markdown files causing long linked lists.

**Success Indicators**:
- Inputs created for Bug 1 (collisions) and Bug 2 (duplicates)
- Strings like '37qpypz' and 'uvhisfu' with same hash prepared

### Step 4: Local Testing
procedure: [[procedures/Test-Locally-with-Proof-of-Concept]]

**Objective**: Build and test the parser locally to measure performance degradation.

**Instructions**: Use the provided snudown_proof_of_concept.zip to build the parser, parse random vs. malicious inputs, and plot parsing time vs. N (number of references).

**Expected Output**: Graphs showing O(N) time for malicious inputs vs. O(1) for random.

**Success Indicators**:
- Parser built successfully
- Linear time growth observed for malicious cases

### Step 5: Live Reproduction
procedure: [[procedures/Reproduce-on-Live-Reddit]]

**Objective**: Confirm vulnerabilities persist in production by testing on Reddit.

**Instructions**: Send a private message with colliding reference names (e.g., '37qpypz' and 'uvhisfu' each with unique URLs) and observe rendered HTML using the last URL for all.

**Expected Output**: Rendered output showing incorrect URL resolution, confirming hash flaws.

**Success Indicators**:
- Message sent and rendered
- Wrong references resolved, indicating live vulnerability

## Attack Chain Summary

### Key Achievements

1. Discovered weak SDBM hash and implementation flaws in Snudown.
2. Crafted PoCs demonstrating O(N) complexity for DoS.
3. Confirmed impact on live Reddit, enabling server slowdown.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[OS Exhaustion Flood]] OS Exhaustion
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Impact]] Impact

---

*Last updated: 2023-10-01T00:00:00Z*
