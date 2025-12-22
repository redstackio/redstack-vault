---
id: 19a9d70e-f98e-40b7-b7e9-36c18369b035
name: Host Header Injection
type: procedure
verified: true
submitted: true
created_at: '2020-08-22T13:22:56.651994+00:00'
updated_at: '2023-05-26T01:25:33.308362+00:00'
platforms:
  - Web
tags:
  - '[[tags/Host header Injection]]'
  - '[[tags/Web Applications]]'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
commands:
  - '[[commands/curl-send-custom-host-header]]'
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
---

# Host Header Injection

## Summary

Host header injection is a web vulnerability that arises when a server fails to validate or sanitize the HTTP Host header in incoming requests. This allows attackers to manipulate the header to alter server behavior, such as serving content from arbitrary domains, enabling cache poisoning, bypassing security controls, or facilitating further attacks like XSS or open redirects.

## Description

In a typical web request, the Host header specifies the domain name of the server being requested. If the application trusts this header without validation—often to determine which virtual host to serve or to construct absolute URLs—it can be exploited. For example, an attacker can set the Host header to a malicious or external domain (e.g., bing.com), causing the server to respond with content from that domain or reflect the manipulated value in responses. This procedure demonstrates detection and exploitation using a proxy tool like Burp Suite to intercept and modify requests, confirming the vulnerability by observing reflected changes and loading external content via the manipulated URL. It is commonly used in web penetration testing to identify misconfigurations in load balancers, CDNs, or web servers like Apache/Nginx.

## Requirements

1. A proxy tool like Burp Suite configured to intercept HTTP traffic from your browser.
2. Network access to the target web application (e.g., via a browser or direct HTTP requests).
3. Basic knowledge of HTTP requests and headers.
4. A controlled testing environment to avoid unintended impacts.

## Defense

Defensive measures and detection strategies:

- Validate and sanitize the Host header on the server side, ensuring it matches expected domains.
- Use HTTP Strict Transport Security (HSTS) and secure cookie flags to mitigate related risks.
- Implement web application firewalls (WAFs) to detect anomalous Host headers.
- Monitor server logs for requests with unexpected Host values and enable response header validation.

## Objectives

1. Identify if the target application reflects or acts on unvalidated Host headers.
2. Demonstrate exploitation by loading external content through the vulnerable endpoint.
3. Confirm vulnerability for reporting or further chaining in attack scenarios.
4. Expected outcome: Successful manipulation leading to reflected Host value or external site loading.

## Instructions

### Step 1: Intercept the Target Request

**Context**: Use a proxy to capture an incoming request to the vulnerable endpoint, allowing modification of headers. This step ensures you can observe the original request structure before injection.

**Tool**: Configure [[tools/Burp-Suite]] as a proxy in your browser (e.g., via FoxyProxy extension) and navigate to the target URL to trigger interception.

> No specific command is needed here, as this is a GUI action in Burp Suite. Ensure the Proxy tab is active and the Intercept is toggled on. Forward the request once captured to proceed.

### Step 2: Modify and Send the Request with Custom Host Header

**Context**: In the Burp Repeater, alter the Host header to an external domain (e.g., bing.com) to test if the server processes it without validation. This reveals if the header is reflected in the response or influences server routing.

**Command** ([[commands/curl-send-custom-host-header]]):
```bash
curl -H "Host: $_CUSTOM_HOST" -X GET $_TARGET_URL
```

> This command sends a GET request with a custom Host header. Replace $_CUSTOM_HOST with an external domain like 'bing.com' and $_TARGET_URL with the vulnerable endpoint (e.g., 'http://target.com/page'). In Burp, right-click the intercepted request, send to Repeater, edit the Host line to 'Host: bing.com', and click Send. The purpose is to inject the malicious header and observe the response for reflections or anomalies.

### Step 3: Verify Exploitation by Loading the Manipulated URL

**Context**: Extract the full URL from the manipulated request and load it in a browser to confirm the server serves external content based on the injected Host header, proving the vulnerability's impact.

**Instructions**: In Burp Repeater, right-click the response URL (which now incorporates the custom Host) and copy it to the clipboard. Paste into a new browser tab and observe if the external site (e.g., bing.com) loads instead of the target content. Alternatively, use the curl command from Step 2 with verbose output (-v) to inspect headers.

> If using curl for verification: Add -v flag to see full request/response headers. Success is indicated if the response body contains content from the custom host or if the browser loads the external site.

## Expected Output

- Step 2: Response headers or body reflecting the injected Host value (e.g., links or redirects pointing to bing.com).
- Step 3: Browser loads the external domain's homepage, confirming the server used the manipulated Host for resolution or content serving.

Sample curl output for success:
```
< HTTP/1.1 200 OK
< Server: nginx
< Content-Type: text/html
... (HTML from bing.com)
```
