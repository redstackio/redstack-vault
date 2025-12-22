---
id: proc-uuid-4
name: Brute-Force-Mass-User-Removals-with-Burp-Intruder
tags:
  - brute-force
  - mass-disruption
  - intruder
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:29:36.526Z'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Brute Force]]'
---
# Brute-Force-Mass-User-Removals-with-Burp-Intruder

## Summary

This procedure scales the IDOR exploit using Burp Intruder's brute-force capabilities to attempt removals across all possible 4-digit user_id and team_id combinations, potentially disrupting the entire platform.

## Description

In the attack on developers.mtn.com, a captured removal request is sent to Burp Intruder, with positions marked for user_id and team_id. Payloads generate 0000-9999 for each, resulting in 100 million requests. Valid pairs trigger removals and PII disclosures. This web attack requires a stable authenticated session and may take 12-20 hours based on request rate. Outcomes include widespread team disruptions and aggregated PII collection.

## Requirements

1. Burp Suite Professional (Intruder feature)
2. Captured base request with marked positions
3. Sufficient bandwidth and time for long-running attack

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on the removal endpoint (e.g., 10/min per user)
- Use CAPTCHA or secondary auth for repeated actions
- Monitor for high-volume requests from single sessions; block brute-force patterns

## Objectives

1. Enumerate and remove all valid user-team pairs
2. Collect disclosed PII from responses
3. Achieve platform-wide impact through disruption

## Instructions

### Step 1: Send Request to Intruder

**Context**: Prepare the base request for automated fuzzing.

From Proxy or Repeater, right-click the captured removal request and select "Send to Intruder."

> Expected: Intruder tab opens with the request loaded.

### Step 2: Configure Payload Positions

**Context**: Mark parameters for brute-forcing.

In Positions tab, highlight §user_id§ and §team_id§ (add § if needed). Clear other positions.

> Expected: Two payload sets defined.

### Step 3: Set Payloads and Run Attack

**Context**: Define 4-digit ranges and execute.

In Payloads tab, for both positions: Type=Numbers, From=0, To=9999, Step=1, Prefix= (pad to 4 digits with zeros). Set attack type to Sniper or Cluster bomb. Start the attack.

> Expected: Requests sent sequentially; responses show successes (e.g., 200 with PII) vs. failures (404/403). Monitor length or grep for keywords to identify hits.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Brute Force]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- brute-force
- mass-disruption
- intruder
