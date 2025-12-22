---
id: 112160e0-9d3e-401d-8f82-71205b3d927d
type: procedure
verified: true
submitted: true
created_at: '2020-08-24T06:41:04.772306+00:00'
updated_at: '2023-05-26T01:11:38.990936+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - dom-xss
  - injection
  - owasp
  - owasp-top-10
  - web-applications
commands: []
platforms:
  - Web
tools:
  - '[[tools/web-browser-developer-tools]]'
skill_level: beginner
impact_level: medium
detection_risk: low
validated: true
---

# DOM XSS via location.search in Select Element

## Summary

This procedure exploits a DOM-based Cross-Site Scripting (XSS) vulnerability where the application unsafely uses the `location.search` parameter (specifically `storeId`) to populate options in a `<select>` element, allowing an attacker to inject arbitrary HTML and JavaScript by breaking out of the tag structure. The technique demonstrates how client-side reflection of URL parameters without proper encoding leads to executable code injection, typically resulting in JavaScript alerts or more severe actions like data theft.

## Description

DOM-based XSS occurs when client-side JavaScript processes untrusted data (here, from `location.search`) and inserts it into the DOM without sanitization. In this case, the vulnerable code likely uses something like `document.write` or `innerHTML` to insert the `storeId` value into a `<select>` dropdown for store selection during a stock check. An attacker can manipulate the URL parameter to close the `<select>` and `<option>` tags prematurely, then inject malicious HTML attributes (e.g., `onerror` in an `<img>` tag) to execute JavaScript. This is common in legacy web apps or those mishandling query strings. The procedure assumes access to a vulnerable product page and uses browser developer tools for inspection and testing. Success is confirmed by executing an alert popup, proving arbitrary JS execution in the victim's context.

## Requirements

1. Direct access to the vulnerable web application via a browser (e.g., HTTP/HTTPS endpoint like `/product?productId=1`).
2. A modern web browser with developer tools enabled (e.g., Chrome, Firefox).
3. No special privileges required, but the site must reflect `location.search` parameters client-side without server validation.
4. Basic knowledge of HTML, JavaScript, and URL encoding.

## Defense

Defensive measures and detection strategies:

- Sanitize and encode all user inputs from `location.search` using methods like `textContent` instead of `innerHTML`, or libraries like DOMPurify.
- Implement Content Security Policy (CSP) to restrict inline script execution and `on*` event handlers.
- Use URL parsing libraries to extract and validate parameters before DOM insertion.
- Monitor browser console for unexpected JS errors or network requests triggered by injected code.
- Enable client-side logging or use tools like OWASP ZAP to scan for DOM XSS sinks.

## Objectives

1. Identify the reflection point where `storeId` from `location.search` populates a `<select>` element.
2. Confirm parameter control and lack of sanitization with benign input.
3. Inject a payload to break out of the HTML structure and execute JavaScript.
4. Verify exploitation by triggering a proof-of-concept alert.

## Instructions

### Step 1: Access the Product Page and Trigger Stock Check

**Context**: Navigate to the vulnerable product page and activate the functionality that processes the `storeId` parameter, setting up the DOM for potential injection.

Open the web application in your browser and go to the product details page, such as `https://vulnerable-site.com/product?productId=1`. Click the "Check Stock" button to load the store selection interface, which triggers the client-side code using `location.search`.

### Step 2: Inspect the Page HTML Structure

**Context**: Use browser developer tools to examine the rendered DOM and identify the `<select>` element where the parameter is inserted, understanding the injection sink.

Right-click on the page (near the stock check area) and select "Inspect Element" (or press F12). In the Elements panel, locate the `<select>` dropdown for stores. Note any `<option>` tags and check the associated JavaScript for how `location.search` is parsed (e.g., via `new URLSearchParams` or manual splitting).

### Step 3: Locate the Hidden storeId Parameter

**Context**: Identify the `storeId` parameter in the URL or DOM attributes, confirming it's user-controllable and reflected without escaping.

In the developer tools, use the search function (Ctrl+F in Elements panel) to find "storeId". Hover over elements related to the stock check to reveal any hidden inputs or URL parameters. Observe that `storeId` is not visibly present but can be appended to the query string.

### Step 4: Test Reflection with Benign Input

**Context**: Inject a harmless alphanumeric string to verify that the parameter is reflected into the `<select>` element, often with improper closing (e.g., appended ">).

Modify the browser's address bar to append `&storeId=test123` to the URL (full: `https://vulnerable-site.com/product?productId=1&storeId=test123`) and press Enter to reload. Re-inspect the `<select>` element to confirm "test123" appears inside an `<option>` tag, typically malformed like `<option value="test123">`.

### Step 5: Inject and Execute the XSS Payload

**Context**: Craft a payload to close the `<select>` and `<option>` tags, then inject an executable element to trigger JavaScript, exploiting the lack of HTML entity encoding.

Update the URL to: `https://vulnerable-site.com/product?productId=1&storeId="></select><img%20src=1%20onerror=alert(1)>` (URL-encoded spaces as %20). Load the page and observe the alert dialog popping up, confirming JavaScript execution. The payload breaks out by closing tags and adds an `<img>` with a non-existent `src` to fire the `onerror` event.

**Expected Output**: A browser alert box displays "1", indicating successful JS execution in the context of the page.

**Success Indicators**:
- The benign string appears unescaped in the DOM during Step 4.
- No encoding errors; the payload triggers the alert without URL decoding issues.
- Console shows no CSP violations blocking the script.
