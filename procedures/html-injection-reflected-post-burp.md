---
id: 9ec46650-c34d-40a2-878f-304754bf8a94
name: html-injection-reflected-post-burp
type: procedure
verified: true
submitted: true
created_at: '2020-07-26T17:10:02.088152+00:00'
updated_at: '2023-05-26T01:29:44.851910+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - html-injection
  - injection
  - owasp-top-10
  - web-applications
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# HTML Injection Reflected POST (Burp)

## Summary

This procedure demonstrates how to identify and exploit reflected HTML injection vulnerabilities in web applications by intercepting and modifying POST requests using Burp Suite. By injecting HTML tags into unvalidated input fields like first name and last name, the injected content is reflected in the response, allowing rendering of arbitrary HTML elements such as headings and hyperlinks, which can lead to phishing or further attacks if escalated to XSS.

## Description

HTML injection occurs when a web application fails to properly sanitize or encode user input, allowing attackers to inject HTML tags that are then reflected back in the server's response and rendered by the client's browser. This procedure focuses on POST requests, where form data (e.g., name fields) is sent to the server. Using Burp Suite as a proxy, the attacker intercepts the request, modifies the input with HTML tags like <h1>, <a>, and <h2>, and forwards it. Upon receiving the response, the browser parses and displays the injected HTML, potentially creating clickable links or altering page layout. This technique is common in legacy applications or those with weak input validation and can serve as a precursor to more severe vulnerabilities like cross-site scripting (XSS). It targets web forms that echo user input without escaping, typically in registration or contact pages.

## Requirements

1. Access to a web application with a vulnerable POST form (e.g., first name and last name fields that reflect input unsanitized).
2. Burp Suite installed and configured as a proxy (browser traffic routed through Burp).
3. Basic knowledge of HTTP requests and browser developer tools for verification.
4. Target environment: Any web application over HTTP/HTTPS; no special credentials needed for public forms.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization using libraries like OWASP ESAPI or DOMPurify to escape HTML characters (< becomes &lt;).
- Use Content Security Policy (CSP) headers to restrict inline HTML and script execution.
- Employ Web Application Firewalls (WAFs) like ModSecurity to detect and block anomalous HTML in requests.
- Enable logging of all POST requests and monitor for patterns of HTML tags in input fields.
- Conduct regular security testing with tools like Burp Suite or OWASP ZAP to identify reflection points.

## Objectives

1. Intercept and modify a POST request containing user input to inject HTML tags.
2. Verify that the injected HTML is reflected and rendered in the response page.
3. Demonstrate potential impact, such as creating functional hyperlinks that redirect users.
4. Expected outcome: Successful rendering of injected HTML, confirming the vulnerability.

## Instructions

### Step 1: Prepare and Submit Initial Form

**Context**: Begin by submitting normal form data to establish a baseline request that can be intercepted. This step identifies the structure of the POST request and ensures the form reflects input in the response.

Navigate to the target web form (e.g., a registration or contact page with first name and last name fields). Enter benign text such as "TestUser" in the First Name field and "TestLast" in the Last Name field. Submit the form while ensuring your browser is proxied through Burp Suite to capture the traffic.

> No specific command is used here; this is a manual browser interaction. Use Burp's Proxy tab to monitor incoming requests.

### Step 2: Intercept the POST Request

**Context**: Capture the outgoing POST request to inspect its payload. This allows observation of how user input is parameterized in the request body, typically in form-urlencoded format.

In Burp Suite, go to the Proxy > Intercept tab and ensure interception is enabled for POST requests. Submit the form from Step 1. The request will pause in Burp, showing the HTTP POST method, headers, and body with parameters like firstname=TestUser&lastname=TestLast.

> Inspect the request in Burp's UI. Look for the raw request body to confirm input fields are present and unencoded.

### Step 3: Inject HTML Tags into the Request

**Context**: Modify the request parameters to include HTML tags, exploiting the lack of sanitization. This tests whether the server reflects the input as raw HTML in the response.

In Burp's Proxy > Intercept or Repeater tab, edit the request body. Replace the firstname value with <h1>Follow Me</h1> and lastname with <a href="https://redstack.io">redstack.io</a><h2>Injected Content</h2>. Ensure the request remains valid (e.g., preserve parameter names and encoding). Forward the modified request to the server.

> Use Burp's text editor in the request pane. Common tags for testing include <h1> for headings, <a href="URL"> for links, and <h2> for subheadings. Avoid script tags unless escalating to XSS.

### Step 4: Observe and Verify the Response

**Context**: Analyze the server's response to confirm reflection and rendering of the injected HTML. This validates the vulnerability and demonstrates impact.

After forwarding, view the response in Burp's Inspector or your browser. The response body should contain the injected tags unescaped, and when rendered in the browser, it displays as a heading "Follow Me", a clickable link to redstack.io, and additional heading "Injected Content".

> Check the HTML source in the browser (right-click > View Page Source) to see raw tags. Click the link to verify functionality.

### Step 5: Test for Escalation and Report

**Context**: Attempt to escalate the injection if possible (e.g., to include JavaScript) and document findings for remediation.

If the basic injection works, try injecting <script>alert('XSS')</script> in a field to check for XSS. If successful, note it as a higher-severity issue. Capture screenshots of requests, responses, and rendered output for reporting.

> This step includes decision points: If HTML renders but JS does not, it's HTML injection only (lower risk). If JS executes, reclassify as reflected XSS.
