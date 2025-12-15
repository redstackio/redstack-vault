---
id: proc-add-extract-blog-id
tags:
  - idor
  - data-extraction
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:48.119Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Add-and-Extract-Victim-Blog-ID

## Summary

This procedure adds a blog or website to the victim's IntenseDebate profile and extracts the unique hidBlogID from the page source, which serves as the direct object reference for IDOR exploitation.

## Description

To exploit IDOR, the attacker needs the victim's object identifier (hidBlogID), obtained by inspecting the HTML after adding data to the profile. This step occurs under the victim's authenticated session. The ID is a hidden form field vulnerable to substitution. Prerequisites include a logged-in victim account. Expected outcome: A copied hidBlogID value for use in request modification.

## Requirements

1. Logged-in victim account
2. Access to https://www.intensedebate.com/edit-user-profile
3. Web browser developer tools for source inspection

## Defense

Defensive measures and detection strategies:

- Obfuscate or encrypt object IDs to prevent easy extraction
- Log and monitor profile editing actions for anomalies
- Implement client-side validation tied to server-side checks

## Objectives

1. Populate victim's profile with target data
2. Identify and extract the vulnerable ID parameter
3. Prepare ID for substitution in attacker requests

## Instructions

### Step 1: Log In and Access Profile Editor

**Context**: Authenticate as victim to reach the editing interface.

**Instructions**: Log in to the victim's account and navigate to https://www.intensedebate.com/edit-user-profile.

> The profile page should load with editing options visible.

### Step 2: Add Blog/Website

**Context**: Create an entry to generate the hidBlogID.

**Instructions**: Click 'Add Blog / Website', fill in the form (e.g., blog URL, name), and click 'Save Settings'.

> The page refreshes, confirming the addition.

### Step 3: Extract hidBlogID

**Context**: Inspect source to find the ID.

**Instructions**: Right-click the page, select 'View Page Source', search for 'radMainSite', and copy the value of the nearby hidBlogID input field (e.g., <input type="hidden" name="hidBlogID" value="12345">).

> Note the exact value for later use.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[idor]]
- [[data-extraction]]
