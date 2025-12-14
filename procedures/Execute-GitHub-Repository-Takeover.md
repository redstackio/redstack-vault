---
tags:
  - github
  - takeover
  - supply-chain
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - GitHub
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Supply Chain Compromise]]'
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:33:12.079Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
id: d0e66aff-e9ca-4243-8948-654f7a748ef8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Supply Chain Compromise]]'
  - '[[Account Manipulation]]'
---
# Execute GitHub Repository Takeover

## Summary

This procedure details claiming control of a dormant or misconfigured GitHub repository referenced in a Gradle plugin, allowing potential injection of malicious code for supply chain compromise.

## Description

GitHub accounts or organizations that are inactive can be hijacked if not properly secured, especially when referenced in third-party tools like Palantir's Gradle launch config plugin. The attacker, having identified the vulnerable repo through reconnaissance, uses GitHub's mechanisms (e.g., username squatting or support requests) to transfer ownership. Once controlled, the repo can be altered to include malicious Gradle scripts, affecting projects that pull from it. This targets Java/Gradle environments and relies on improper access controls. Outcomes include full repo control, though real-world impact depends on plugin adoption.

## Requirements

1. Identified dormant GitHub repo from plugin analysis
2. GitHub account for claiming ownership
3. Knowledge of GitHub's takeover policies for inactive namespaces

## Defense

Defensive measures and detection strategies:

- Proactively claim and secure all referenced repos in configurations
- Implement two-factor authentication and organization security settings on GitHub
- Use repository scanning tools to detect unauthorized transfers

## Objectives

1. Gain ownership of the target GitHub repository
2. Enable modification of plugin contents for compromise
3. Assess potential for downstream supply chain effects

## Instructions

### Step 1: Initiate Takeover Request

**Context**: Leverage GitHub's policies to claim the inactive repo.

Log in to GitHub and navigate to the dormant repo. If the username/org is available or inactive, use the 'Transfer ownership' feature or contact GitHub support with evidence of dormancy (e.g., no activity for years). For hijackable cases, register the username if squattable.

> Expected output: GitHub confirmation email or dashboard update showing pending transfer.

### Step 2: Verify and Modify Control

**Context**: Confirm ownership and prepare for compromise.

After transfer, access the repo settings to verify admin rights. Clone the repo locally, introduce malicious changes (e.g., altered Gradle tasks for code injection), and push updates. Test by building a sample project using the plugin to ensure propagation.

> Expected output: Successful push with no errors, and plugin users potentially pulling malicious version.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Supply Chain Compromise]] Supply Chain Compromise
- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[github]]
- [[takeover]]
- [[supply-chain]]
