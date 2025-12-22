---
id: da094ea0-4025-41f8-862b-c373316efec1
name: DOM-XSS-Cookie-Manipulation
type: procedure
verified: true
submitted: true
created_at: '2020-08-07T15:03:08.156147+00:00'
updated_at: '2023-05-26T01:26:00.287899+00:00'
platforms:
  - Web
tags:
  - cookie manipulation
  - DOM XSS
  - injection
  - owasp
  - owasp top 10
  - Web Applications
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
commands: []
tools: []
validated: true
---

# DOM-XSS-Cookie-Manipulation

## Summary

This procedure exploits a DOM-based Cross-Site Scripting (XSS) vulnerability in a web application where unsanitized input from a URL parameter is written directly to document.cookie. By crafting a malicious URL, an attacker can trick a victim into setting attacker-controlled data in their browser cookies, potentially leading to session hijacking or further exploitation.

## Description

DOM-based XSS occurs when client-side JavaScript processes data from sources like URL parameters without proper sanitization and writes it to sensitive sinks such as document.cookie. In this scenario, targeting an e-commerce application, the 'lastviewedproduct' cookie stores the URL of the last viewed product. An attacker crafts a URL that injects malicious JavaScript via an iframe, which executes to alert or manipulate the cookie contents. Upon clicking, the victim's browser sets the malicious payload in the cookie and redirects to the legitimate site, masking the attack. This technique is effective against applications vulnerable to OWASP Top 10 injection flaws and can be used for credential theft or persistence.

## Requirements

1. Access to a vulnerable web application (e.g., e-commerce site with DOM XSS in product viewing).
2. Browser with developer tools or a cookie editing extension (e.g., Chrome Cookie Editor) to inspect cookies.
3. Ability to deliver the malicious URL to the victim via social engineering (e.g., phishing email or link).
4. Knowledge of the application's base URL and product endpoint structure.

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to restrict inline scripts and iframes.
- Sanitize and validate all URL parameters before writing to document.cookie using libraries like DOMPurify.
- Enable browser protections like XSS Auditor (deprecated but similar in modern browsers) and monitor for anomalous cookie writes via client-side logging.
- Server-side: Log and alert on unusual referral patterns or JavaScript errors indicating XSS attempts.

## Objectives

1. Identify the vulnerable cookie-writing mechanism in the application.
2. Craft and deliver a payload that injects malicious JavaScript to manipulate cookies.
3. Verify successful cookie manipulation and potential data exfiltration (e.g., alerting document.cookie).

## Instructions

### Step 1: Inspect Application Cookies

**Context**: Examine the application's cookie structure to identify the vulnerable 'lastviewedproduct' cookie, which stores unsanitized URL data.

Open the target e-commerce application in a browser and navigate to a product page. Use a browser extension like Cookie Editor to view cookies. Look for the 'lastviewedproduct' cookie, which should contain the URL of the viewed product.

### Step 2: Craft Malicious Payload

**Context**: Create an iframe-based payload that injects a script to execute DOM XSS, alerting the cookie contents while redirecting to mask the attack.

Use the following code snippet as the payload, substituting the base URL with the target's domain:

**Code** ([[codes/DOM-XSS-Cookie-Manipulation-Iframe-Payload]]):

```
<iframe src="https://aca71fbe1fd30d7180c004e800d800e9.web-security-academy.net/product?productId=1&'><script>alert(document.cookie)</script>" onload="if(!window.x)this.src='https://aca71fbe1fd30d7180c004e800d800e9.web-security-academy.net';window.x=1;">
```

Construct the full malicious URL by embedding this payload into the product parameter (e.g., https://target.com/product?productId=<payload>).

### Step 3: Deliver and Verify

**Context**: Send the crafted URL to the victim and confirm the exploit by observing cookie changes or alert execution.

Deliver the URL via social engineering. When the victim clicks it, the browser loads the malicious iframe, executes the script to alert document.cookie, sets the attacker-controlled data in 'lastviewedproduct', and redirects to the homepage. Verify success by checking for the alert (in testing) or modified cookie contents using Cookie Editor.
