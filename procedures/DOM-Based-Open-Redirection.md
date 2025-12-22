---
id: d489492e-1a45-4547-82fa-f5c5312de3a6
name: DOM-Based-Open-Redirection
type: procedure
verified: true
submitted: true
created_at: '2020-08-06T17:11:33.744195+00:00'
updated_at: '2023-05-26T18:29:40.266104+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Drive-by Compromise]]'
sub_techniques: []
tags:
  - '[[tags/DOM Based Open Redirection]]'
  - '[[tags/Open Redirection]]'
  - '[[tags/Web Applications]]'
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
---

# DOM-Based-Open-Redirection

## Summary

This procedure demonstrates how to exploit a DOM-based open redirection vulnerability in a web application by manipulating client-side JavaScript to redirect users to an attacker-controlled domain. It targets unvalidated URL parameters that are used in location-based sinks like location.href, allowing cross-domain navigation without server-side checks.

## Description

DOM-based open redirection occurs when client-side code, typically JavaScript, processes user-supplied input (e.g., a URL parameter) and uses it to set the browser's location without proper validation. This can trick users into visiting malicious sites, facilitating phishing, bypass of security controls, or session hijacking. The technique is common in single-page applications or legacy web apps where query parameters directly influence navigation sinks such as location.href, location.hostname, or location.search. In this scenario, an attacker inspects the page source to identify vulnerable sinks, crafts a malicious URL with an external redirect target, loads it in the browser, and triggers the redirection via a link or action on the page. Success relies on the absence of validation for external domains, often evading server-side detection. This maps to MITRE ATT&CK technique T1189 (Drive-by Compromise) under Initial Access, as it enables malicious redirects via exploited public-facing web apps.

## Requirements

1. Access to a vulnerable web application with a DOM-based redirection flaw (e.g., a blog post page with a 'back to blog' link).
2. Modern web browser like Chrome or Firefox for inspection and testing.
3. Basic knowledge of JavaScript and browser developer tools.
4. Network access to load the target application and external domains.

## Defense

Defensive measures and detection strategies:

- Implement client-side validation to whitelist allowed domains or use URL parsing libraries to check for external redirects.
- Use Content Security Policy (CSP) with strict navigation directives to block unauthorized redirects.
- Monitor browser console for suspicious location assignments and log client-side errors.
- Server-side logging of unusual query parameters and referrer headers to detect anomalous navigation patterns.

## Objectives

1. Identify vulnerable JavaScript sinks that handle user input for redirection.
2. Craft and deliver a malicious URL to trigger cross-domain navigation.
3. Verify the redirection to an external attacker-controlled site.
4. Demonstrate potential for phishing or further exploitation.

## Instructions

### Step 1: Inspect the Vulnerable Page for Sinks

**Context**: Examine the client-side code to locate unvalidated location sinks that process URL parameters, confirming the vulnerability exists.

Navigate to the target page (e.g., a blog post) and scroll to the bottom where a 'back to blog' link is present. Right-click the link and select 'Inspect' in the browser's developer tools (e.g., Chrome DevTools). Search for JavaScript code handling the link click, focusing on location assignments.

Observe that the code uses a sink like `location.href = decodeURIComponent(url)` without domain validation. Common vulnerable sinks include:
- `location`
- `location.host`
- `location.hostname`
- `location.href`
- `location.pathname`
- `location.search`

This step verifies the lack of checks, allowing arbitrary redirects.

### Step 2: Craft the Malicious Redirect URL

**Context**: Construct a URL that injects an external domain into the vulnerable parameter, bypassing any implicit validation by appending a fragment (#) to neutralize path checks.

Build the URL by appending the target post ID and a malicious redirect parameter. For example, if the vulnerable parameter is 'url', set it to an external site like 'https://www.blackhat.com' followed by '# ' to prevent further parsing issues.

Example malicious URL:
```
https://ac331f0d1eed796680651b22000b0008.web-security-academy.net/post?postId=4&url=https://www.blackhat.com/#
```

This URL loads the legitimate post but sets the 'url' parameter to the attacker's domain.

### Step 3: Load the URL and Trigger Redirection

**Context**: Deliver the crafted URL to the victim (e.g., via phishing) and trigger the vulnerable link to execute the redirect.

Paste the malicious URL from Step 2 into the browser and load the page. Once loaded, scroll to the bottom where the 'back to blog' link appears. Click the link, which should now redirect to the external domain specified in the 'url' parameter (e.g., www.blackhat.com) instead of the application's home page.

Verify the redirect in the browser's address bar or network tab in DevTools, confirming cross-domain navigation.

### Step 4: Validate Exploitation Success

**Context**: Confirm the redirect works as intended and assess potential impact.

After clicking the link, check that the browser navigates to the attacker-specified URL without errors. In a real attack, this could load a phishing page mimicking the legitimate site. Test variations by changing the external domain to ensure no whitelisting blocks it.

If the redirect fails (e.g., due to partial validation), adjust the payload by URL-encoding special characters or using alternative sinks.
