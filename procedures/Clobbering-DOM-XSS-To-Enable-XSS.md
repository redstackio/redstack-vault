---
id: 2d8dc443-815f-451e-a186-b840e1a34ad1
name: Clobbering-DOM-XSS-To-Enable-XSS
type: procedure
verified: true
submitted: false
created_at: '2020-08-31T14:10:17.130395+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
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
validated: true
---

# Clobbering-DOM-XSS-To-Enable-XSS

## Summary

This procedure exploits DOM-based Cross-Site Scripting (XSS) by using DOM clobbering to override JavaScript object properties through injected HTML elements, enabling arbitrary JavaScript execution in a vulnerable web application comment section.

## Description

DOM clobbering is a technique where an attacker injects HTML elements with IDs or names that shadow existing JavaScript variables or object properties, altering the DOM in a way that affects script behavior. In this scenario, the target application loads comments dynamically via a JavaScript file (e.g., loadCommentsWithDomClobbering.js) that uses a fallback for a defaultAvatar object with a logical OR operator: `let defaultAvatar = window.defaultAvatar || {avatar: '/resources/images/avatarDefault.svg'}`. By injecting anchor tags with duplicate IDs and a name attribute matching the property ("avatar"), the attacker clobbers the avatar property to point to a malicious href containing an onerror handler. When subsequent comments are loaded, the clobbered property triggers the JavaScript execution, such as an alert. This targets web applications with insufficient input sanitization on user-generated content like comments, allowing control over HTML structure without direct script injection.

## Requirements

1. Access to a vulnerable web application with a comment posting feature that renders user input as HTML without proper escaping.
2. A modern web browser (e.g., Chrome, Firefox) with developer tools enabled.
3. Network access to the target application (no special credentials required for public comment sections).
4. Basic knowledge of HTML, JavaScript, and browser DOM inspection.

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to restrict inline scripts and eval-like behaviors.
- Sanitize user input to prevent HTML tag injection, using libraries like DOMPurify.
- Avoid relying on global objects for fallbacks; use local variables or strict mode.
- Monitor for duplicate IDs or unusual anchor tags in rendered HTML via client-side validation or server-side logging.
- Enable browser security features like XSS Auditor (deprecated but similar in modern browsers) and log JavaScript errors.

## Objectives

1. Identify vulnerable JavaScript code relying on global object properties.
2. Inject HTML to clobber the target property and embed a malicious event handler.
3. Trigger execution by interacting with the application to reload affected elements.
4. Verify XSS execution through popup or console output.

## Instructions

### Step 1: Navigate to the Vulnerable Page and Inspect the Application

**Context**: Access the target blog post or page with the comment section to understand the structure and locate the JavaScript responsible for loading comments.

Open the target web application in your browser and navigate to the "view post" page where comments can be posted. This establishes the context for the vulnerability.

### Step 2: Inspect Network Requests and JavaScript Source

**Context**: Use browser developer tools to monitor network activity and examine the JavaScript file that handles comment loading, identifying the clobberable object.

Right-click on the page and select "Inspect" or "Developer Tools". Switch to the "Network" tab. Reload the page or interact with comments to capture requests. Look for and double-click on the file named `loadCommentsWithDomClobbering.js` to view its source code. Observe the line: `let defaultAvatar = window.defaultAvatar || {avatar: '/resources/images/avatarDefault.svg'}`. This fallback is vulnerable to clobbering because it references a global property.

### Step 3: Inject the Clobbering Payload

**Context**: Submit HTML input that creates duplicate anchor elements to shadow the `defaultAvatar` object and override its `avatar` property with a malicious href containing an onerror handler.

In the comment input field, enter the following payload:

[[codes/DOM-Clobbering-Anchor-Payload-for-XSS]]

```html
<a id=defaultAvatar><a id=defaultAvatar name=avatar href="cid:&quot;onerror=alert(1)//">
```

Post the comment. This injects the anchors into the DOM, grouping them by ID and setting the `name` attribute to clobber the `avatar` property with the `href` value.

### Step 4: Trigger the Payload Execution

**Context**: Post an additional comment to force the application to reload or re-evaluate the clobbered DOM elements, activating the onerror handler.

Return to the comment section and post a neutral comment (e.g., "Test comment"). This action causes the JavaScript to access the clobbered `defaultAvatar.avatar`, attempting to load the malicious `href`, which fails and triggers the `onerror=alert(1)` execution.

### Step 5: Verify Execution

**Context**: Confirm the XSS by observing the alert popup or checking the browser console for execution traces.

Upon successful triggering, an alert box with "1" should appear, indicating JavaScript execution. If no popup, inspect the console for errors or use more advanced payloads (e.g., replace `alert(1)` with data exfiltration).

## Expected Output

- Successful payload injection: Comment posts without errors, visible in the DOM via inspector.
- Clobbering effect: In developer tools Elements tab, verify duplicate `<a id="defaultAvatar">` elements and the `name="avatar"` attribute.
- Execution: Alert popup or console log confirming `alert(1)` ran.

Success is indicated by the alert firing, demonstrating full XSS control for further payloads like keylogging or credential theft.
