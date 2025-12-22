---
tags:
  - node.js
  - undici
  - math.random
  - multipart-boundary
  - predictability
  - request-tampering
  - lcg
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/node]]'
  - '[[tools/php]]'
  - '[[tools/pip3]]'
  - '[[tools/z3-solver]]'
  - '[[tools/predict.py]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - Node.js
submitted: true
complexity: medium
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Extract-and-Setup-Vulnerable-Application]]'
  - '[[procedures/Start-Node.js-Webhook-Server]]'
  - '[[procedures/Start-PHP-Backend-API]]'
  - '[[procedures/Exploit-Predictable-Randomness-for-Request-Tampering]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:28.238Z'
description: >-
  Demonstrates exploitation of predictable Math.random() in undici library for
  multipart boundary generation, enabling prediction and tampering of backend
  API requests to modify sensitive order data.
skill_level: intermediate
impact_level: high
id: f5174520-0b30-40b8-9002-9f77dc5ce068
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Predictable Multipart Boundaries in Undici Leading to Unauthorized Request Tampering

Multi-stage attack chain exploiting the predictability of V8's Math.random() implementation in the undici library, used for generating multipart/form-data boundaries in Node.js fetch requests. By observing multiple boundaries from a controlled server, an attacker can reverse-engineer the linear congruential generator (LCG) state using a solver, predict future values, and tamper with uncontrolled fields in backend API requests, such as overwriting customer_id in order submissions to unauthorizedly modify data.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Vulnerable Environment] --> B[Start Node.js Server]
    B --> C[Start PHP Backend]
    C --> D[Collect Boundaries and Exploit Predictability]
    D --> E[Tamper Request and Modify Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/node]]
- [[tools/php]]
- [[tools/pip3]]
- [[tools/z3-solver]]
- [[tools/predict.py]]

### Target Environment

- Node.js v22.12.0 or compatible
- PHP runtime for backend simulation
- Local network access to ports 8000 and 2000
- report.tar.xz archive containing server.js, order.php, and exp.js

### Initial Access Requirements

- Local machine with Node.js, PHP, and Python installed
- No remote credentials needed; simulates controlled environment for observation and tampering
- Ability to run servers on localhost

## Detailed Attack Procedures

### Step 1: Extract and Setup Vulnerable Application
procedure: [[procedures/Extract-and-Setup-Vulnerable-Application]]

**Objective**: Obtain and prepare the vulnerable Node.js application, PHP backend, and exploit code to simulate the environment where undici's predictable boundaries can be observed.

**Instructions**: Download and unpack the report archive, verify Node.js version, and install dependencies.

First, extract the archive using standard tools (e.g., tar -xf report.tar.xz). Then, verify the Node.js version with [[commands/node-version-check]]:

```bash
node --version
```

Expected output: v22.12.0. Install dependencies with [[commands/npm-install]]:

```bash
npm install
```

This installs express and undici.

**Expected Output**: Dependencies installed, including undici for multipart requests.

**Success Indicators**:
- Archive unpacked successfully
- Node.js version confirmed
- No installation errors

### Step 2: Start Node.js Webhook Server
procedure: [[procedures/Start-Node.js-Webhook-Server]]

**Objective**: Launch the Express server that triggers multipart requests to the backend, exposing boundaries via the /trigger-webhook endpoint for observation.

**Instructions**: Run the server script using [[commands/node-server-start]]:

```bash
node ./server.js
```

The server listens on port 8000 and uses undici's fetch to send multipart/form-data requests with Math.random()-generated boundaries.

**Expected Output**: "Server listening on port 8000".

**Success Indicators**:
- Server starts without errors
- Endpoint /trigger-webhook accessible at http://127.0.0.1:8000

### Step 3: Start PHP Backend API
procedure: [[procedures/Start-PHP-Backend-API]]

**Objective**: Simulate the backend API that processes tampered multipart requests, parsing fields like customer_id, price, item_id, and description.

**Instructions**: Launch the PHP development server with [[commands/php-server-start]]:

```bash
php -S 127.0.0.1:2000
```

This serves order.php, which handles POST /order.php and processes form data.

**Expected Output**: "PHP 8.x Development Server (http://127.0.0.1:2000) started".

**Success Indicators**:
- PHP server running on port 2000
- /order.php endpoint ready to receive requests

### Step 4: Collect Boundaries and Exploit Predictability
procedure: [[procedures/Exploit-Predictable-Randomness-for-Request-Tampering]]

**Objective**: Observe boundaries from multiple requests, predict future Math.random() values using Z3 solver, and craft a tampered request to overwrite customer_id to 1337 and description to 'zzz'.

**Instructions**: Install z3-solver with [[commands/pip3-install-z3]]:

```bash
pip3 install z3-solver
```

Then execute the exploit with [[commands/node-exploit-run]]:

```bash
node ./exp.js
```

The script sends requests to /trigger-webhook to collect boundaries, solves for LCG state, predicts values, and submits a tampered order.

**Expected Output**: Logs showing boundary collection (e.g., "Need 5 more values"), followed by tampered response: "$4000 has been subtracted from the account of customer #1337 for item 1. description of order: (\"zzz\")".

**Success Indicators**:
- Boundaries collected and predicted successfully
- Tampered fields applied (customer_id=1337, description=zzz)
- Backend processes unauthorized modification

## Attack Chain Summary

### Key Achievements

1. Setup of vulnerable Node.js and PHP environment to replicate undici's multipart boundary generation.
2. Observation of predictable boundaries exposing V8 Math.random() LCG state.
3. Reverse-engineering and prediction of random values using Z3 solver.
4. Successful tampering of backend request fields, demonstrating unauthorized data alteration.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### MITRE ATT&CK Tactics

- [[Execution]] Execution
- [[Collection]] Collection

---
*Last updated: 2024-01-01T00:00:00Z*
