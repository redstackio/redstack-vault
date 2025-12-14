---
id: proc-demonstrate-clickjacking-test-1195209
tags:
  - clickjacking
  - testing
  - web
type: procedure
tools:
  - '[[tools/Lookout-Clickjacking-Test]]'
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
updated_at: '2025-12-14T17:28:04.317Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate-Clickjacking-Using-Test-Page

## Summary

This procedure tests a web application's susceptibility to clickjacking by attempting to embed it in an iframe on a controlled test page, confirming the absence of anti-framing protections and demonstrating how attackers can overlay deceptive elements to hijack user clicks on sensitive UI.

## Description

Clickjacking exploits the ability to frame a site invisibly, tricking users into interacting with hidden elements while believing they are engaging with a legitimate overlay. Using a tool like the Lookout Clickjacking Test, load the target URL (e.g., from Sifchain's subdomain) into an iframe. If it loads without denial, attackers can craft decoy sites to steal data via unintended form submissions. The impact includes phishing-like theft of passwords or credit card info, with low detection risk in proof-of-concept stages.

## Requirements

1. Internet access to the test tool URL.
2. The identified vulnerable URL from prior reconnaissance.
3. A web browser to observe the framing behavior.

## Defense

Defensive measures and detection strategies:

- Enforce strict X-Frame-Options headers to block all framing.
- Audit CSP policies for frame-ancestors restrictions.
- Log and alert on cross-origin iframe attempts or anomalous user agent patterns.

## Objectives

1. Verify the site can be framed without protections.
2. Simulate UI overlay to show deception potential.
3. Document the vulnerability for reporting or exploitation.

## Instructions

### Step 1: Access Test Tool

**Context**: Navigate to the clickjacking test page to prepare the iframe environment.

No command; open https://www.lookout.net/test/clickjack.html in a browser.

> This loads a page with an iframe ready for embedding targets.

### Step 2: Embed Target URL

**Context**: Insert the vulnerable URL into the test iframe to check for framing success.

Use the tool's interface or modify the iframe src to https://cryptoeconomics.sifchain.finance/#sif10jatqfd88m8s2uhtdtdl3txtayjtzsve2klyhh&type=lm.

> If the site loads, it confirms vulnerability; overlay invisible elements (e.g., via CSS) to demonstrate click hijacking on sensitive parts like forms.

**Expected Output**: Target site renders inside the iframe without errors or redirects.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Lookout-Clickjacking-Test]]

## Tags

- [[clickjacking]]
- [[ui-redressing]]
