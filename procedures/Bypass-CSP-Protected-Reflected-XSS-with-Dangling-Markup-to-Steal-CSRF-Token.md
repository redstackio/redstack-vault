---
type: procedure
verified: true
submitted: true
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - csrf
  - web-applications
  - xss
  - csp-bypass
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Bypass-CSP-Protected-Reflected-XSS-with-Dangling-Markup-to-Steal-CSRF-Token

## Summary

This procedure demonstrates how to bypass Content Security Policy (CSP) protections on a reflected XSS vulnerability using a dangling markup injection technique. By injecting HTML markup that triggers an out-of-band request to a controlled server (Burp Collaborator), an attacker can exfiltrate sensitive data like CSRF tokens from the victim's browser. The stolen token is then used to craft a malicious CSRF proof-of-concept (PoC) that allows unauthorized actions, such as changing a user's email address.

## Description

In scenarios where direct reflected XSS is blocked by CSP, attackers can exploit incomplete HTML parsing by injecting 'dangling' markup, such as an unclosed attribute in a reflected parameter. This causes the browser to interpret subsequent page content as part of the injection, enabling attribute-based exfiltration via background images or similar resources. This technique targets web applications with reflected parameters (e.g., email in a reset form) and weak CSRF protections. The attack requires the victim to interact with a crafted exploit URL, typically delivered via phishing or social engineering. Success results in token theft and subsequent CSRF exploitation, leading to account manipulation. This maps to JavaScript execution for payload delivery and collection of authentication tokens.

## Requirements

1. Valid login credentials to the target web application for initial testing.
2. Burp Suite Professional with Collaborator enabled for out-of-band interaction tracking.
3. Access to an exploit delivery mechanism, such as a controlled server or phishing page.
4. Network access to the target application (typically over HTTPS on port 443).
5. Basic knowledge of HTML injection and Burp Suite interception.

## Defense

Defensive measures and detection strategies:

- Implement strict CSP policies that block inline scripts and unsafe attributes like 'background'.
- Use unique, short-lived CSRF tokens validated server-side with same-site cookies (Lax/Strict).
- Sanitize and encode reflected parameters to prevent attribute injection (e.g., reject quotes and angle brackets).
- Monitor for anomalous out-of-band requests to collaborator-like domains from user agents.
- Enable web application firewall (WAF) rules to detect dangling markup patterns and CSRF PoC generation attempts.

## Objectives

1. Inject dangling markup to bypass CSP and exfiltrate the CSRF token via an OOB request.
2. Intercept and modify an email change request to capture the legitimate flow.
3. Generate a CSRF PoC using the stolen token to perform unauthorized email changes.
4. Deliver the exploit to a victim, resulting in account takeover via email modification.

## Instructions

### Step 1: Login and Prepare Burp Collaborator

**Context**: Authenticate to the target application and set up Burp Collaborator to receive exfiltrated data. This establishes the baseline session and OOB endpoint for token theft.

Launch Burp Suite and configure it as a proxy for your browser. Navigate to the target application's login page and authenticate using valid credentials. In Burp, go to the Collaborator tab, launch a new Collaborator server instance, and copy the unique Collaborator URL (e.g., your-unique-id.burpcollaborator.net) to the clipboard. This URL will be used in the payload to detect interactions from the victim's browser.

### Step 2: Craft and Deliver the Dangling Markup Payload

**Context**: Create an exploit URL that injects dangling markup into a reflected parameter, causing the browser to load a resource from the Collaborator server and exfiltrate the page's CSRF token.

Construct the payload using the following structure, replacing placeholders with the target URL and Collaborator domain:

Use the code snippet [[codes/Dangling-Markup-CSRF-Token-Exfiltration-Payload]] for the exact injection.

Deliver this payload via an exploit server or phishing link targeting the vulnerable endpoint (e.g., /email?email=). When the victim clicks the link, the reflected parameter will break out of its context, appending the page's HTML (including the CSRF token in a form) to the background attribute, triggering a request to Collaborator.

### Step 3: Poll Collaborator for Exfiltrated Token

**Context**: Monitor incoming requests to the Collaborator server to capture the exfiltrated CSRF token from the HTTP response body.

In the Burp Collaborator client, click 'Poll Now' to refresh for new interactions. Review the HTTP GET or POST requests; the response body will contain fragments of the target's HTML, including the CSRF token (typically in a <input name="csrf" value="..."> tag). Extract and copy the token value for use in the next steps.

### Step 4: Intercept and Modify Email Change Request

**Context**: Simulate the email change action while intercepting with Burp to understand the request format and prepare for token substitution.

With Burp's Proxy set to intercept, navigate to the email change functionality in the application (e.g., /my-account). Submit a request to change the email to a random address (e.g., test@example.com). In the intercepted POST request, note the structure, including the csrf parameter and email field. Modify the email parameter to the desired attacker-controlled value (e.g., attacker@evil.com) but do not forward yet—this captures the legitimate flow.

### Step 5: Generate CSRF PoC with Stolen Token

**Context**: Use Burp's built-in tools to create a malicious HTML form that submits the modified request with the stolen CSRF token, enabling automatic execution on the victim side.

In the Burp Repeater or Proxy history, right-click the intercepted email change request and select 'Engagement Tools' > 'Generate CSRF PoC'. In the options, ensure 'Include Auto-Submit Script' is enabled to make the form submit automatically upon page load. Click 'Regenerate' to update the CSRF token placeholder with the stolen value from Step 3. Copy the generated HTML to the clipboard.

### Step 6: Integrate PoC into Exploit and Deliver

**Context**: Embed the CSRF PoC into the original exploit delivery mechanism to chain the token theft with immediate action, completing the attack.

Return to the exploit server or phishing page from Step 2. Replace the initial payload section with the copied CSRF PoC HTML. Ensure the page auto-submits the form upon loading. Deliver the updated exploit to the victim. When interacted with, it will first exfiltrate the token (if needed) and then submit the malicious email change, updating the victim's account to the attacker's email.
