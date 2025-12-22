---
id: 8c236b92-127a-4847-95f2-52644eb7959f
name: Clobbering-DOM-Attributes-To-Bypass-HTML-Filters
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T04:39:00.100464+00:00'
updated_at: '2023-05-26T01:29:06.260372+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - DOM XSS
  - injection
  - owasp
  - owasp top 10
  - Web Applications
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Clobbering-DOM-Attributes-To-Bypass-HTML-Filters

## Summary

This procedure demonstrates DOM clobbering, a technique to manipulate the Document Object Model (DOM) by injecting HTML elements that override or redefine DOM properties and attributes. It is used to bypass HTML filters in web applications, enabling DOM-based XSS (Cross-Site Scripting) attacks, such as executing JavaScript to steal cookies or perform other malicious actions.

## Description

DOM clobbering involves injecting HTML like forms or elements with specific IDs that conflict with existing JavaScript variables or DOM attributes, effectively 'clobbering' them to alter application behavior. This is particularly effective against applications that sanitize input for standard XSS but fail to account for attribute redefinition. In this scenario, the target is a web application with a comment section that allows limited HTML input. The injected payload redefines DOM elements to trigger an onfocus event, leading to JavaScript execution. The technique requires a delay to ensure the injected content loads before focusing the element, often achieved via an iframe. This maps to JavaScript execution in web contexts and is common in OWASP Top 10 injection vulnerabilities.

## Requirements

1. Access to a web application with an injectable input field (e.g., comment section) that permits basic HTML tags like <form> and <input> but filters script tags.
2. A browser environment where the attacker can control an external page (e.g., local HTML file) to load the target.
3. Knowledge of the target's URL structure, including post IDs for loading specific pages.
4. No special tools required beyond a standard web browser and text editor.

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to restrict inline scripts and eval() usage.
- Sanitize and validate all user inputs, including HTML attributes, using libraries like DOMPurify.
- Avoid using element IDs that match global objects or sensitive properties (e.g., avoid 'x' if used in JS).
- Monitor for unusual DOM manipulations via client-side logging or anomaly detection in web traffic.
- Use HttpOnly flags on cookies to prevent theft via XSS.

## Objectives

1. Inject HTML payload to clobber DOM attributes and bypass HTML filters.
2. Trigger JavaScript execution (e.g., alert(document.cookie)) via focus event.
3. Demonstrate successful XSS in a filtered comment section.

## Instructions

### Step 1: Inject the Clobbering Payload

**Context**: This step introduces HTML elements that redefine DOM properties, setting up the clobbering effect. The payload uses a form with an ID that overrides a target attribute, combined with an input to focus and execute code.

Paste the following payload into the application's comment or input section:

```html
<form id=x tabindex=0 onfocus=alert(document.cookie)><input id=attributes>
```

Submit the comment to persist the payload on the page.

### Step 2: Load the Target Page with Delay

**Context**: To ensure the injected payload is parsed into the DOM before triggering, load the page containing the comment in an iframe with a timed redirect to activate the fragment identifier (#x), which focuses the clobbered element.

Use the code snippet [[codes/Iframe-Delayed-Load-For-DOM-Clobbering]]:

Save the code as an HTML file (e.g., clobber.html) and open it in a browser. The iframe will load the target post after a 500ms delay, appending #x to the URL to focus the form and execute the alert.

### Step 3: Verify Execution

**Context**: Confirm the clobbering worked by observing the JavaScript execution. The onfocus event should fire, displaying the cookie alert if successful.

After loading, inspect the page source or browser console for the injected elements. If the alert pops up with cookie data, the bypass succeeded. If not, check for filter interference and adjust the payload (e.g., encode attributes).
