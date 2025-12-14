---
id: proc-uuid-create-id
tags:
  - broken-access-control
  - traffic-interception
  - id-extraction
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
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:59.067Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-and-Extract-Access-Request-ID

## Summary

This procedure involves submitting a user access request form in a DoD system while intercepting the traffic with Burp Suite to extract the generated sequential request ID from the server response, enabling subsequent exploitation of broken access controls.

## Description

In the context of a web-based DoD information system, attackers can create access requests without authentication and capture the auto-generated ID, which is sequential and predictable. This ID serves as the key for unauthorized operations like deletion. The procedure assumes network access to the target endpoints and uses Burp Suite for proxying to inspect responses. Prerequisites include a configured Burp proxy; outcomes provide the ID needed for further steps, with low direct impact but foundational for data manipulation attacks.

## Requirements

1. Network access to https://█████████/████████ or https://█████████/██████
2. Burp Suite installed and running as a proxy (e.g., browser proxy set to 127.0.0.1:8080)
3. Basic knowledge of form submission and HTTP interception

## Defense

Defensive measures and detection strategies:

- Implement client-side certificate pinning or proxy detection to block traffic interception tools like Burp
- Rate-limit form submissions to prevent ID enumeration
- Log all request creations and monitor for anomalous proxy-like User-Agent strings

## Objectives

1. Generate a new user access request to obtain a valid sequential ID
2. Intercept and parse the server response for the ID
3. Prepare for unauthorized actions using the extracted ID

## Instructions

### Step 1: Configure Proxy and Navigate to Form

**Context**: Set up Burp Suite to intercept all traffic from the browser to capture the submission response.

Start Burp Suite and configure your browser to use it as a proxy. Navigate to https://█████████/████████ or https://█████████/██████.

### Step 2: Submit the Form

**Context**: Fill out the user access request form with test data and submit while ensuring interception is active.

Complete the form fields (e.g., user details, access type) and submit. In Burp, forward the request and inspect the response.

### Step 3: Extract the ID

**Context**: Locate the sequential request ID in the server response body.

In Burp's Proxy > HTTP history or Repeater, view the POST response. The ID appears as a numeric value referencing the new request (e.g., in JSON or HTML).

**Expected Output**: Response body containing the ID, such as {"request_id": 12345}.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[broken-access-control]]
- [[traffic-interception]]
- [[id-extraction]]
