---
tags:
  - csrf
  - exploitation
  - drive-by
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:03.834Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 4fbdd343-3780-4e26-b75b-32c98a5a33e8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Execute CSRF Attack on Authenticated User

## Summary

This procedure outlines the delivery and execution of a CSRF attack using a malicious HTML page to force an authenticated user to perform unauthorized actions, such as creating a group in their Localize account, without their awareness.

## Description

In a real-world scenario, the attacker lures the victim to the PoC page while they are logged into the vulnerable application. The auto-submitting form leverages the victim's existing session cookies to authenticate the forged request. Prerequisites include a deployed PoC from prior steps and a delivery method like phishing. The expected outcome is successful account modification, highlighting the vulnerability's impact.

## Requirements

1. Deployed malicious HTML page accessible via URL
2. Authenticated victim session to the target application
3. Delivery vector (e.g., email with link, social engineering)

## Defense

Defensive measures and detection strategies:

- Deploy anti-phishing training and email filters
- Implement behavioral analytics to detect unexpected form submissions
- Use short-lived session tokens and logout on suspicious activity

## Objectives

1. Deliver the malicious page to the victim
2. Confirm exploitation through account changes
3. Assess potential for broader unauthorized modifications

## Instructions

### Step 1: Prepare Delivery

**Context**: Select and set up a method to trick the victim into visiting the page.

Craft a phishing email or message with a link to the hosted HTML, disguising it as a legitimate resource (e.g., 'Click to view update'). Ensure the victim is authenticated to Localize.

**Expected Output**: Victim receives and clicks the link.

### Step 2: Trigger the Attack

**Context**: Load the page to initiate the auto-submission.

When the victim opens the page, the JavaScript executes, submitting the form to the target endpoint using the victim's cookies.

**Expected Output**: Silent POST request; no visible alerts to the user.

### Step 3: Verify Impact

**Context**: Check the victim's account for unauthorized changes.

Instruct the victim (or monitor if testing) to log into Localize and view their groups. Alternatively, if coordinated, confirm via API or dashboard.

**Expected Output**: New 'test' group present without user initiation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[exploitation]]
