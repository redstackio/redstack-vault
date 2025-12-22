---
tags:
  - reconnaissance
  - enumeration
  - hackerone
type: procedure
tools:
  - '[[tools/Curl]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-saml-request]]'
  - '[[commands/jq-parse-response]]'
platforms:
  - Web
techniques:
  - '[[Gather Victim Network Information]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 6b8ec3ba-204d-4377-a8f7-b77c467c96de
created_at: '2025-12-13T09:01:26.540Z'
updated_at: '2025-12-13T09:01:26.540Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Network Information]]'
---
# Identify Target HackerOne Programs

## Summary

This procedure involves gathering and probing potential HackerOne program handles to identify candidates for further enumeration, serving as the initial reconnaissance step in targeting private programs.

## Description

In the context of HackerOne's ecosystem, programs may be private and not publicly listed. This procedure uses basic web requests to compile and test a list of suspected handles, looking for subtle indicators like HTTP responses that suggest existence without full disclosure. It sets the stage for exploiting specific vulnerabilities like SAML weaknesses. Expected outcomes include a refined list of targets for deeper probing.

## Requirements

1. Access to the internet and HackerOne's public endpoints
2. A wordlist or known handles for programs
3. Basic command-line tools like curl

## Defense

Defensive measures and detection strategies:

- Monitor for unusual probing patterns on program URLs
- Implement rate limiting on sensitive endpoints

## Objectives

1. Compile a list of potential private program handles
2. Perform initial availability checks
3. Prepare targets for enumeration exploitation

## Instructions

### Step 1: Compile Program Handle List

**Context**: Generate or source a list of potential HackerOne program handles (e.g., company names, domains).

**Command** ([[commands/curl-saml-request]]):

```bash
curl -s https://hackerone.com/[program-handle] -I
```

> This checks HTTP headers for status codes that might indicate a live program.

### Step 2: Parse Responses

**Context**: Analyze responses to filter viable targets.

**Command** ([[commands/jq-parse-response]]):

```bash
curl -s https://hackerone.com/[program-handle] | jq '.status'
```

> Extracts relevant fields if the response is parseable, helping identify patterns.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Network Information]]

### Sub-Techniques



## Commands Used

- [[commands/curl-saml-request]]
- [[commands/jq-parse-response]]

## Tools Used

- [[tools/Curl]]

## Tags

- [[Reconnaissance]]
- [[hackerone]]
