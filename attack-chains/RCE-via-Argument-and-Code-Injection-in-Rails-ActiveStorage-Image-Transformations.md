---
tags:
  - rce
  - argument-injection
  - code-injection
  - rails
  - activestorage
  - imagemagick
type: attack_chain
tools:
  - '[[tools/ImageMagick]]'
  - '[[tools/MiniMagick]]'
  - '[[tools/ImageProcessing]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/convert-with-argument-injection]]'
  - '[[commands/convert-with-hash-injection]]'
  - '[[commands/ruby-system-touch-file]]'
platforms:
  - Web
  - Linux
complexity: medium
procedures:
  - '[[procedures/Identify-Vulnerable-ActiveStorage-Variant-Usage]]'
  - '[[procedures/Exploit-Argument-Injection-with-Array-Parameters]]'
  - '[[procedures/Exploit-Transformation-Injection-with-Hash-Parameters]]'
  - '[[procedures/Exploit-Code-Injection-via-Arbitrary-Method-Calls]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
description: >-
  Multi-stage exploit chain leveraging argument injection and code injection in
  Ruby on Rails ActiveStorage to achieve arbitrary file writes and remote code
  execution via ImageMagick and Ruby eval.
skill_level: intermediate
impact_level: high
id: 306ebab6-4917-4c52-b07b-5d0d4a1cbf25
created_at: '2025-12-14T17:28:28.340Z'
updated_at: '2025-12-14T17:28:28.340Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# RCE via Argument and Code Injection in Rails ActiveStorage Image Transformations

## Overview

This attack chain exploits vulnerabilities in Ruby on Rails ActiveStorage's variant() and preview() methods, where user-supplied parameters are passed unsanitized to the ImageProcessing gem and MiniMagick, leading to execution of ImageMagick's convert command. By injecting arrays or hashes into parameters, attackers can inject arbitrary CLI arguments or trigger method_missing in MiniMagick. Additionally, the send() method in ImageProcessing allows arbitrary Ruby method calls, such as eval, enabling direct code execution. The chain progresses from identifying vulnerable code patterns to achieving full RCE, including arbitrary file writes for overwriting ERB templates, SSRF, file leakage, and server compromise.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Vulnerable Variant Usage] --> B[Argument Injection via Arrays]
    B --> C[Transformation Injection via Hashes]
    C --> D[Code Injection via Eval]
    D --> E[RCE Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/ImageMagick]]
- [[tools/MiniMagick]]
- [[tools/ImageProcessing]]

### Target Environment

- Ruby on Rails application with ActiveStorage 6.1.3.1 or similar
- Image upload functionality using variant() or preview()
- ImageProcessing 1.12.1 and MiniMagick 4.11.0
- Server-side ImageMagick installation

### Initial Access Requirements

- Authenticated access to upload images and request variants (e.g., user account)
- Knowledge of the endpoint handling image variant requests
- Network access to the web application

## Detailed Attack Procedures

### Step 1: Identify Vulnerable ActiveStorage Variant Usage
procedure: [[procedures/Identify-Vulnerable-ActiveStorage-Variant-Usage]]

**Objective**: Locate and confirm the use of user-controlled parameters in ActiveStorage variant() or preview() calls to identify injection points.

**Instructions**: Analyze the application's ERB templates or controller code for patterns like `<%= image_tag user.avatar.variant(resize: params[:new_size]) %>`. Use browser developer tools or intercept requests to verify if parameters like :new_size or :t/:v are passed directly from user input to variant(). Send a test request with a benign parameter to observe if it affects image processing.

**Expected Output**: Confirmation that parameters influence the ImageMagick convert command without sanitization.

**Success Indicators**:
- Parameters appear unsanitized in the transformation pipeline
- Image processing errors reveal internal command details

### Step 2: Exploit Argument Injection with Array Parameters
procedure: [[procedures/Exploit-Argument-Injection-with-Array-Parameters]]

**Objective**: Inject arbitrary ImageMagick arguments using array parameters to write files to unauthorized locations, enabling RCE via template overwrites.

**Instructions**: Craft a request to the variant endpoint with array parameters, such as new_size[]=123&new_size[]=-set&new_size[]=comment&new_size[]=MYCOMMENT&new_size[]=-write&new_size[]=/tmp/file.erb. This triggers the execution of [[commands/convert-with-argument-injection]]. Monitor server logs or file system for the written file.

**Expected Output**: Arbitrary file written, e.g., /tmp/file.erb containing injected content.

**Success Indicators**:
- File created at specified path
- Image processing completes without errors, indicating successful injection

### Step 3: Exploit Transformation Injection with Hash Parameters
procedure: [[procedures/Exploit-Transformation-Injection-with-Hash-Parameters]]

**Objective**: Use hash parameters to inject ImageMagick options like -write, allowing output to arbitrary files and potential SSRF or leakage.

**Instructions**: Send a request with parameters t=write&v=/tmp/file2.erb to the variant call. This generates [[commands/convert-with-hash-injection]]. Verify by checking if the processed image is written to the target path.

**Expected Output**: Processed image saved to /tmp/file2.erb.

**Success Indicators**:
- Arbitrary file write confirmed
- No validation errors in response

### Step 4: Exploit Code Injection via Arbitrary Method Calls
procedure: [[procedures/Exploit-Code-Injection-via-Arbitrary-Method-Calls]]

**Objective**: Leverage the send() method to execute arbitrary Ruby code, achieving direct RCE on the server.

**Instructions**: Submit parameters t=eval&v=system("touch /tmp/hacked") to trigger [[commands/ruby-system-touch-file]] via ImageProcessing's send(). Validate by confirming the file creation on the server.

**Expected Output**: Ruby system command executed, e.g., file /tmp/hacked created.

**Success Indicators**:
- File /tmp/hacked exists
- Potential server logs show command execution

## Attack Chain Summary

### Key Achievements

1. Identified unsanitized parameter handling in ActiveStorage
2. Achieved arbitrary file writes via ImageMagick argument injection
3. Performed SSRF and file leakage through transformation options
4. Executed arbitrary Ruby code for full RCE

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
