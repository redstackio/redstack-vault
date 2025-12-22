---
id: proc-uuid-3
tags:
  - csrf
  - poc
  - social-engineering
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:21.021Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Generate-and-Deliver-CSRF-PoC-HTML-Page

## Summary

This procedure generates an HTML-based Proof-of-Concept (PoC) for CSRF attacks that auto-submits forms with XSS payloads, delivering it via social engineering to exploit authenticated users.

## Description

For the DoD application's /submit-form endpoint, this creates a malicious HTML page with hidden inputs for parameters like building (containing XSS), using JavaScript to auto-POST. Chained with prior steps, it forces XSS execution. Prerequisites: Crafted payloads and endpoint details. Outcomes: Victim's session compromised without interaction beyond loading the page.

## Requirements

1. Burp Suite for PoC generation
2. Attacker-controlled hosting for the HTML file
3. Social engineering vector (e.g., email, link)

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens and validate origins
- Educate users on phishing and suspicious links
- Log and alert on unexpected form submissions

## Objectives

1. Forge POST request cross-origin
2. Inject XSS payload seamlessly
3. Achieve session hijacking or data theft

## Instructions

### Step 1: Generate PoC in Burp

**Context**: Use Burp's built-in tool to create the HTML form.

In [[tools/Burp-Suite]], go to the captured POST request, right-click > Engagement tools > Generate CSRF PoC. Customize hidden inputs with XSS payloads, e.g., <input name="building" value="%22%3E%3Cimg+src%3Dx+onerror%3Dalert(document.cookie)%3E">

**Expected Output**: HTML file with <form method="POST" action="https://target-site.com/submit-form"> and auto-submit script.

### Step 2: Add Auto-Submission

**Context**: Ensure immediate execution upon page load.

Edit the generated HTML to include <script>document.forms[0].submit();</script> at the end.

**Expected Output**: Page that submits without user input.

### Step 3: Host and Deliver

**Context**: Distribute to victims via phishing.

Host on attacker server (e.g., https://evil.com/csrf-poc.html). Send link disguised as legitimate (e.g., "Update your classroom booking" email).

**Expected Output**: Victim loads page, form submits, XSS triggers.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[poc]]
- [[social-engineering]]
