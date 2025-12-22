---
id: 3030f79b-3d02-40ef-9454-324882591829
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T14:30:33.950158+00:00'
updated_at: '2023-05-26T01:35:04.157839+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - '[[tags/Clickjacking]]'
  - '[[tags/Web Applications]]'
commands: []
platforms:
  - Web
tools: []
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Clickjacking-Test

## Summary

This procedure tests for clickjacking vulnerabilities by embedding a target web application within an iframe on a malicious or test webpage. If the target loads without restrictions, it may be susceptible to clickjacking attacks where users are tricked into performing unintended actions.

## Description

Clickjacking, also known as a UI redress attack, involves overlaying transparent or hidden elements over a legitimate webpage loaded in an iframe to deceive users into clicking on malicious actions. This procedure simulates the attacker's side by creating a simple HTML page that attempts to load the target application in an iframe. Successful loading indicates the absence of defenses like the X-Frame-Options header or Content-Security-Policy (CSP) frame-ancestors directive, allowing potential exploitation. It is commonly used in web penetration testing to identify misconfigurations in public-facing applications. The target environment is any web application without proper framing protections.

## Requirements

1. A modern web browser (e.g., Chrome, Firefox) to render the HTML file.
2. The URL of the target web application to test.
3. Local file system access to save and open the HTML file.
4. No special privileges or network access beyond internet connectivity to the target.

## Defense

Defensive measures and detection strategies:

- Implement the X-Frame-Options HTTP header (e.g., DENY or SAMEORIGIN) on all responses to prevent framing.
- Use Content-Security-Policy with frame-ancestors directive to restrict allowable framing sources.
- Monitor for unusual iframe embeddings in client-side logs or web application firewalls (WAFs).
- Educate users on phishing awareness to recognize suspicious overlays.

## Objectives

1. Verify if the target application can be loaded in an iframe from an external site.
2. Identify lack of framing protections for remediation.
3. Demonstrate potential for user interaction hijacking in a controlled test.
4. Expected outcome: Confirmation of vulnerability if the iframe loads successfully without errors.

## Instructions

### Step 1: Create the Clickjacking Test HTML File

**Context**: This step involves generating a basic HTML file that embeds the target application in an iframe. The purpose is to simulate a malicious page attempting to frame the target, checking for any blocking mechanisms.

Use the provided code snippet [[codes/Clickjacking-Test-HTML]] to create the file. Save it as `clickjacking-test.html` and replace the placeholder URL with the actual target application URL.

**Expected Output**: A valid HTML file saved locally, ready to open in a browser.

> Save the file and confirm it opens without syntax errors in a text editor.

### Step 2: Load the HTML File in a Browser

**Context**: Opening the file tests whether the browser can render the iframe with the target content. If the target loads, the application is vulnerable to clickjacking; if blocked, protections are in place.

Open `clickjacking-test.html` in your web browser by double-clicking the file or using the browser's file-open dialog.

Observe the page: The target application should appear within the iframe if vulnerable. Look for console errors related to framing (e.g., 'Refused to display in a frame').

**Expected Output**: The target webpage loads inside the iframe without restrictions, or an error message indicating framing is blocked.

> If the iframe is blank or shows a refusal message, the test confirms protection against clickjacking.

### Step 3: Verify and Document Results

**Context**: This step ensures the test outcome is validated and any vulnerability is noted for reporting.

Check the browser's developer tools (F12) for network requests and console logs. Confirm if the iframe src request succeeds (200 OK) or fails due to headers.

Document the results: Note the target URL, browser used, and whether the iframe loaded.

**Expected Output**: Screenshots or logs showing successful embedding or blocking, confirming the vulnerability status.

> Success is indicated by the target content visibly loading in the iframe, highlighting the need for defensive headers.
