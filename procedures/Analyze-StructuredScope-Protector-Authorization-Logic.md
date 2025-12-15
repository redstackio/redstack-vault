---
id: proc-uuid-analyze-781150
name: Analyze-StructuredScope-Protector-Authorization-Logic
tags:
  - code-review
  - authorization
  - ruby
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:25:53.571Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Analyze-StructuredScope-Protector-Authorization-Logic

## Summary

This procedure involves static code analysis of the StructuredScope protector in HackerOne's Ruby on Rails application to identify missing authorization checks that allow unauthorized access to private program scopes.

## Description

In the context of penetration testing HackerOne's platform, review the authorization logic in app/protectors/protected_structured_scope.rb. The protector incorrectly grants access to any H1_PENTESTER role holder without verifying association to a specific Pentest object or invitation to the target private program. This flaw enables broader access than intended, leading to potential information disclosure. Prerequisites include access to the source code (e.g., via decompilation, leaks, or internal review) and familiarity with Ruby on Rails Pundit policies.

## Requirements

1. Access to HackerOne Ruby source code (app/protectors/protected_structured_scope.rb)
2. Knowledge of Ruby and Rails authorization patterns (e.g., Pundit)
3. Authenticated pentester session for context

## Defense

Defensive measures and detection strategies:

- Implement comprehensive authorization checks in protectors, including program-specific validations
- Use code scanning tools like Brakeman or RuboCop to detect missing auth checks
- Monitor GraphQL queries for anomalous node fetches

## Objectives

1. Confirm the absence of Pentest association verification in the protector policy
2. Document the root cause for reporting
3. Identify exploitable entry points like the GraphQL node interface

## Instructions

### Step 1: Locate and Review Protector Code

**Context**: Navigate to the relevant file and examine the policy definition to spot the flawed role-based access.

No specific command; perform manual code review:

- Open app/protectors/protected_structured_scope.rb
- Focus on line 42 and surrounding policy methods
- Verify that access is granted via `h1_pentester?` without additional checks like `pentest_for(user)` or program invitation validation

> Expected: Policy code similar to `def show?` or `def read?` that returns true for H1_PENTESTER without scope restrictions.

### Step 2: Map to Exploitation Vector

**Context**: Correlate the code flaw to API endpoints that query StructuredScope objects.

No command; analyze dependencies:

- Trace usage of the protector in GraphQL resolvers, particularly the node interface
- Note that global IDs (e.g., gid://hackerone/StructuredScope/1) bypass direct ID checks

> Expected: Understanding that GraphQL node queries can fetch any object without program context.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- code-review
- authorization
- ruby
