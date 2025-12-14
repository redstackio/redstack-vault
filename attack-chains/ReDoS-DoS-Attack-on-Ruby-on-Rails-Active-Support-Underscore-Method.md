---
id: ac-redos-rails-underscore-001
tags:
  - redos
  - dos
  - ruby
  - rails
  - active-support
  - regex
type: attack_chain
tools: []
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
  - Ruby on Rails
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Craft-ReDoS-Malicious-String]]'
  - '[[procedures/Invoke-Underscore-Method-via-Web-Input]]'
step_count: 2
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:36.419Z'
description: >-
  A denial of service attack exploiting catastrophic backtracking in the Active
  Support underscore method, leading to excessive CPU and memory consumption in
  Ruby on Rails applications.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
---
# ReDoS DoS Attack on Ruby on Rails Active Support Underscore Method

Multi-stage attack chain demonstrating a complete DoS workflow by exploiting a Regular Expression Denial of Service (ReDoS) vulnerability in Active Support's underscore method. This vulnerability, identified as CVE-2023-22796, allows attackers to craft inputs that trigger catastrophic backtracking in the regex engine, causing severe CPU and memory exhaustion. Affected versions include all prior to 6.1.7.1 and 7.0.4.1. The attack targets web applications where user input is processed by underscore or related methods like titleize, tableize, or foreign_key.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Craft Malicious Input] --> B[Submit to Vulnerable Endpoint]
    B --> C[Resource Exhaustion DoS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard web client like curl or browser)

### Target Environment

- Ruby on Rails application using Active Support versions < 6.1.7.1 or < 7.0.4.1
- Web platform with endpoints that process user input via underscore, titleize, tableize, or foreign_key methods
- Network access to the target web service

### Initial Access Requirements

- No credentials required if the vulnerable endpoint accepts unauthenticated input
- Ability to send HTTP requests to the application
- Prior reconnaissance to identify endpoints using these inflector methods (e.g., via API docs or source code review)

## Detailed Attack Procedures

### Step 1: Craft Malicious Input
procedure: [[procedures/Craft-ReDoS-Malicious-String]]

**Objective**: Generate a specially crafted string that triggers catastrophic backtracking in the underscore method's regex, maximizing computation time.

**Instructions**: Create a string designed to exploit the backtracking in the regex pattern used for splitting camelCase words, such as repeated patterns that force the regex engine to explore exponential paths. For example, use a string with many lowercase letters followed by uppercase transitions that cause repeated failures in matching.

**Expected Output**: A malicious string, e.g., a long sequence like "a" * 10000 + "Abc" that hangs the processing.

**Success Indicators**:
- String generation completes without errors
- Local test in Ruby console shows delay or hang when processed with underscore

### Step 2: Submit Input to Vulnerable Endpoint
procedure: [[procedures/Invoke-Underscore-Method-via-Web-Input]]

**Objective**: Pass the malicious string to a Rails endpoint that invokes the underscore method on user input, triggering the DoS.

**Instructions**: Identify an endpoint (e.g., a search or naming API) that uses underscore or related methods on input. Submit the crafted string via HTTP POST or GET. For testing, use curl to send the payload:

```bash
curl -X POST 'http://target.com/api/naming' -d 'input=aaaaaaaaaaaaaaaa...Abc' -H 'Content-Type: application/json'
```

Monitor server resources to confirm exhaustion.

**Expected Output**: Server response delays significantly (>30 seconds) or times out, with high CPU/memory usage observed.

**Success Indicators**:
- Server becomes unresponsive to subsequent requests
- Resource monitor shows CPU spike to 100% and memory ballooning

## Attack Chain Summary

### Key Achievements

1. Successful crafting of ReDoS payload exploiting regex backtracking
2. Delivery of payload via web input to trigger DoS
3. Achievement of endpoint resource exhaustion, denying service to legitimate users

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[OS Exhaustion Flood]] Application or Service Exhaustion

### MITRE ATT&CK Tactics

- [[Impact]] Impact

---
*Last updated: 2023-10-01T00:00:00Z*
