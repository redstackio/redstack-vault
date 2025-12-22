---
id: 1ff5bbcd-8cbd-4d90-99d7-d3ca22367222
name: DOM-XSS-in-jQuery-href-Attribute-Using-location-search
type: procedure
verified: true
submitted: true
created_at: '2020-08-24T08:03:29.774174+00:00'
updated_at: '2023-05-26T18:30:06.186140+00:00'
platforms:
  - Web
tags:
  - '[[tags/DOM XSS]]'
  - '[[tags/injection]]'
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/Web Applications]]'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
commands: []
tools: []
validated: true
---

# DOM-XSS-in-jQuery-href-Attribute-Using-location-search

## Summary

This procedure exploits a DOM-based Cross-Site Scripting (XSS) vulnerability in a web application where jQuery dynamically sets an anchor element's href attribute using the unsanitized location.search value, specifically the returnPath query parameter. By injecting a javascript: URI scheme into returnPath, arbitrary JavaScript code can be executed in the victim's browser context, such as displaying document cookies via an alert, potentially leading to session theft or further attacks.

## Description

The vulnerability occurs in the application's feedback submission or search functionality, which relies on jQuery to select an anchor element and assign location.search (or a derived value like returnPath) directly to its href attribute without validation or encoding. This allows attackers to craft malicious URLs that, when loaded or interacted with, execute embedded JavaScript. The attack targets client-side code execution without server-side reflection, making it stealthy and dependent on user navigation. It is commonly found in legacy jQuery implementations (pre-3.5) lacking proper URL sanitization. Success enables cookie exfiltration or DOM manipulation in the authenticated session.

## Requirements

1. Valid access to the web application's home page and feedback submission endpoint.
2. A modern web browser (e.g., Chrome, Firefox) with developer tools enabled for inspection.
3. Network access to the target application without blocking (no CSP or strict browser policies).
4. Optional: An intercepting proxy like [[tools/Burp-Suite]] for URL manipulation and request inspection, though manual browser URL editing suffices for basic testing.

## Defense

Defensive measures and detection strategies:

- Implement input validation and sanitization on client-side: Parse and escape query parameters before assigning to href attributes, rejecting javascript:, data:, or vbscript: schemes.
- Upgrade to modern jQuery versions (3.5+) with built-in protections against prototype pollution and unsanitized assignments.
- Enforce Content Security Policy (CSP) headers to block inline script execution and unsafe-inline directives.
- Use URL-safe encoding (e.g., encodeURIComponent) for query parameters and avoid direct DOM insertion of user-controlled data.
- Monitor for anomalous JavaScript execution via browser logging or endpoint protection tools detecting alert() or cookie access patterns.

## Objectives

1. Navigate to the vulnerable feedback submission page and identify the jQuery href manipulation.
2. Inject a javascript: payload into the returnPath query parameter to execute arbitrary code.
3. Verify payload execution through element inspection and alert observation, confirming DOM XSS success.
4. Demonstrate potential impact, such as cookie disclosure, to assess session hijacking risk.

## Instructions

### Step 1: Navigate to Submit Feedback Page

**Context**: Access the page where the vulnerable jQuery code runs, typically the feedback submission form, to set up the environment for query parameter manipulation. This step establishes the initial page state without triggering the vulnerability yet.

From the application's home page, click or navigate to the "Submit Feedback" link or endpoint (e.g., /submit-feedback).

Observe the page load; no payload is injected at this stage.

### Step 2: Modify returnPath Query Parameter

**Context**: Introduce the malicious payload by altering the URL's query string. The returnPath parameter is directly used by jQuery to set the anchor's href, so prefixing it with javascript: allows code execution upon href activation.

Edit the browser's address bar to append or replace the returnPath parameter: ?returnPath=javascript:alert(document.cookie).

Reload the page with the modified URL.

This injects the payload into location.search, which jQuery assigns to the href without sanitization.

### Step 3: Inspect the Anchor Element

**Context**: Confirm reflection of the payload in the DOM to validate the vulnerability. Inspection reveals if the href attribute contains the unsanitized input, proving the jQuery assignment flaw.

Right-click on the relevant anchor element (e.g., a "Back" or navigation link) and select "Inspect Element" or "Inspect" from the browser's developer tools (F12).

Examine the href attribute of the <a> tag; it should now contain the full javascript:alert(document.cookie) value.

If the payload appears unescaped, the vulnerability is confirmed.

### Step 4: Trigger Payload Execution

**Context**: Activate the malicious href to execute the JavaScript in the current context. This simulates victim interaction, such as clicking a back button, leading to code execution like cookie alerting.

Click the browser's back button or interact with the anchor element (e.g., hover or click if applicable) to trigger the href navigation.

Observe the alert popup displaying the document cookies, confirming successful XSS execution.

If no alert appears, check for CSP blocks or retry with a simpler payload like javascript:alert(1).

### Step 5: Verify and Document Impact

**Context**: Assess the attack's success and potential for escalation. This step ensures the payload ran in the authenticated context and captures evidence for reporting.

After the alert, inspect the browser console (Developer Tools > Console) for any errors or additional output.

Document the cookies revealed, noting sensitive data like session tokens, to evaluate risks such as account takeover.

Test variations, like javascript:fetch('/api/user') for data exfiltration, to gauge full impact.
