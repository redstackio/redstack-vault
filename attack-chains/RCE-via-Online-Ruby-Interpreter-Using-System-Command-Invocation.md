---
id: ac-rce-ruby-online-system
tags:
  - rce
  - ruby
  - online-interpreter
  - system-command
type: attack_chain
tools:
  - '[[tools/Online-Ruby-Execution-Site]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Ruby
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Locate-Online-Ruby-Execution-Site]]'
  - '[[procedures/Submit-Malicious-Ruby-Code-for-RCE]]'
  - '[[procedures/Execute-Code-and-Observe-Shell-Output]]'
step_count: 3
techniques:
  - '[[Command-Line Interface]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:27.886Z'
description: >-
  Demonstrates remote code execution on servers hosting online Ruby interpreters
  by submitting Ruby code that invokes shell commands via the system function.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
  - '[[Exploit Public-Facing Application]]'
---
# RCE via Online Ruby Interpreter Using System Command Invocation

Multi-stage attack chain exploiting online Ruby execution platforms to achieve remote code execution on the hosting server by leveraging Ruby's built-in system function to run arbitrary shell commands.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Locate Online Interpreter] --> B[Submit Malicious Ruby Code]
    B --> C[Execute and Observe RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Online-Ruby-Execution-Site]]

### Target Environment

- Web-based online Ruby code execution platforms
- No specific ports or services required beyond web access
- Internet connectivity to access public online interpreters

### Initial Access Requirements

- No credentials needed
- Public network access to online Ruby sites
- No prior access to the target server

## Detailed Attack Procedures

### Step 1: Locate Online Ruby Execution Site
procedure: [[procedures/Locate-Online-Ruby-Execution-Site]]

**Objective**: Identify a publicly available web-based platform that allows execution of arbitrary Ruby code without local installation.

**Instructions**: Search for online Ruby interpreters using a web search engine. Look for sites that provide an interactive code editor and execution button for Ruby snippets.

**Expected Output**: Access to a web interface where Ruby code can be pasted and run, such as a text area for code input and a run/execute button.

**Success Indicators**:
- Webpage loads with Ruby code execution functionality
- No authentication required for basic code execution

### Step 2: Submit Malicious Ruby Code for RCE
procedure: [[procedures/Submit-Malicious-Ruby-Code-for-RCE]]

**Objective**: Craft and input Ruby code that uses the system function to execute shell commands on the server.

**Instructions**: In the code input field of the online interpreter, paste the following Ruby code:

```ruby
# Hello World Program in Ruby
system "clear;ls;uname -a;echo RCE in Ruby Language By Black_EyE";
```

This code invokes the Ruby [[commands/ruby-system-shell-invocation]] command to run a chain of shell commands.

**Expected Output**: The code is accepted and ready for execution, with no immediate errors in the input interface.

**Success Indicators**:
- Code pasted without syntax rejection
- Execute button available and functional

### Step 3: Execute Code and Observe Shell Output
procedure: [[procedures/Execute-Code-and-Observe-Shell-Output]]

**Objective**: Run the submitted code to trigger shell command execution and capture the output demonstrating RCE.

**Instructions**: Click the execute or run button on the online site to trigger the Ruby code. Observe the output console for shell command results, including screen clear, directory listing, system info, and the echo message. Record the session via screen capture for proof-of-concept.

**Expected Output**: Output showing cleared screen, `ls` directory contents, `uname -a` system details (e.g., Linux kernel version), and the message "RCE in Ruby Language By Black_EyE".

**Success Indicators**:
- Shell commands execute successfully on the server
- Arbitrary output from server environment visible in the response
- Video POC confirms RCE impact

## Attack Chain Summary

### Key Achievements

1. Identified vulnerable online Ruby execution platform
2. Achieved arbitrary shell command execution via Ruby system call
3. Demonstrated server compromise potential through command output

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
