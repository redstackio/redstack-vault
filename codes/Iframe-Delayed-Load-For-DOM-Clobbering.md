---
id: 4d93dc12-7dcb-43df-8e6d-4f1fd20758a9
type: code
language: html
verified: true
created_at: '2020-08-31T04:39:00.084310+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
tags:
  - DOM XSS
  - injection
  - payload
platforms:
  - Web
validated: true
---

# Iframe-Delayed-Load-For-DOM-Clobbering

## Code

```html
<iframe src=https://ac301f571f57bb498033200f00cb000c.web-security-academy.net/post?postId=5 onload="setTimeout(someArgument=>this.src=this.src+'#x',500)">
```

## Description

This HTML code snippet creates an iframe that loads a target web page (a specific post) and, after a 500ms delay, appends a fragment identifier (#x) to the URL. The delay ensures the page's DOM, including any injected clobbering payloads, is fully loaded before the fragment triggers focus on the clobbered element, executing associated JavaScript like an onfocus event.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_TARGET_URL | The base URL of the vulnerable post page | https://example.com/post |
| $_POST_ID | The ID of the post containing the injected payload | 5 |
| $_FRAGMENT_ID | The fragment to append for focusing the clobbered element | #x |

## Usage

Embed this snippet in a local HTML file and open it in a browser during a DOM clobbering attack. It is used after injecting a payload like a form with id='x' into the target's comment section. The iframe simulates loading the vulnerable page externally, triggering the clobbered event. Related to procedures like [[procedures/Clobbering-DOM-Attributes-To-Bypass-HTML-Filters]].

## Detection

- Inspect for iframes with onload handlers using setTimeout and URL manipulation.
- Monitor browser developer tools for unexpected fragment navigation or focus events on injected elements.
- Web application firewalls (WAFs) can flag suspicious iframe src attributes pointing to the same domain with delays.
- Client-side CSP violations or anomalous alert() calls in logs.
