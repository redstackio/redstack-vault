---
id: proc-linkedin-intercept
tags:
  - intercept
  - proxy
  - burp
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:34.033Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-LinkedIn-Delete-Request

## Summary

This procedure captures the HTTP DELETE request for a legitimate skill assessment deletion on LinkedIn using a proxy tool, providing the base request for IDOR modification.

## Description

To exploit the IDOR, the attacker intercepts the request sent to /voyager/api/voyagerAssessmentsDashSkillAssessmentAttemptReports/ during their own deletion. This reveals the structure with URN-encoded profile and skill IDs. The target is the LinkedIn API over HTTPS; prerequisites include a configured proxy like Burp Suite. Success yields the raw request for alteration.

## Requirements

1. Burp Suite installed and running as proxy
2. Browser proxy configured to 127.0.0.1:8080
3. Active LinkedIn session with pending deletion

## Defense

Defensive measures and detection strategies:

- Enforce TLS certificate pinning to block proxy interception
- Log and alert on proxied traffic from internal networks
- Use request signing to detect tampering attempts

## Objectives

1. Capture the exact DELETE request format
2. Identify parameter structure for modification
3. Prepare for payload injection

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp Suite to intercept HTTPS traffic from the browser.

Launch Burp Suite, enable Intercept in Proxy tab, and install the CA certificate in the browser.

> Browser traffic routes through Burp; HTTPS sites load without errors.

### Step 2: Trigger Deletion

**Context**: Initiate the delete action to generate the request.

In LinkedIn assessments hub, select delete from kebab menu and confirm.

> Request appears in Burp Intercept tab as DELETE to the Voyager API endpoint.

### Step 3: Analyze Request

**Context**: Examine the path and headers for URN parameters.

View the request: DELETE /voyager/api/voyagerAssessmentsDashSkillAssessmentAttemptReports/urn%3Ali%3Afsd_skillAssessmentAttemptReport%3A(urn%3Ali%3Afsd_profile%3A{own-uuid}%2Curn%3Ali%3Askill%3A{skill-id}%2C{sequence})

> Parameters include profile UUID, skill ID, and attempt sequence; forward or drop as needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[intercept]]
- [[proxy]]
- [[burp]]
