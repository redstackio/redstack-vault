---
id: 4dbd112f-2d56-4a0d-b2b5-500f1bdc604b
name: Angular-DomSanitizer-Bypass-Example
type: code
language: TypeScript
verified: true
created_at: '2023-04-06T03:56:43.795878+00:00'
updated_at: '2023-04-10T20:24:52.287178+00:00'
platforms:
  - Web
tags:
  - xss
  - angular
  - sanitization-bypass
validated: true
---

# Angular-DomSanitizer-Bypass-Example

## Code

```typescript
import { Component, OnInit } from '@angular/core';
import { DomSanitizer } from '@angular/platform-browser';

@Component({
  selector: 'my-app',
  template: `
    <h4>An untrusted URL:</h4>
    <p><a class="e2e-dangerous-url" [href]="dangerousUrl">Click me</a></p>
    <h4>A trusted URL:</h4>
    <p><a class="e2e-trusted-url" [href]="trustedUrl">Click me</a></p>
  `,
})
export class App implements OnInit {
  dangerousUrl: string;
  trustedUrl: any;

  constructor(private sanitizer: DomSanitizer) {}

  ngOnInit() {
    this.dangerousUrl = 'javascript:alert("Hi there")';
    this.trustedUrl = this.sanitizer.bypassSecurityTrustUrl(this.dangerousUrl);
  }
}
```

## Description

This TypeScript code snippet illustrates a vulnerable Angular component that uses DomSanitizer.bypassSecurityTrustUrl to trust a dangerous javascript: URL, enabling XSS when bound to an <a> tag's [href]. In an offensive context, attackers target applications with similar patterns to inject payloads via user inputs, executing code in the browser.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| dangerousUrl | The untrusted input string, often user-controlled | 'javascript:alert(document.cookie)' |
| trustedUrl | Output of bypassSecurityTrustUrl, bound to template | SafeUrl object |
| sanitizer | Injected DomSanitizer service | Angular service instance |

## Usage

Embed this pattern in a test application or exploit by injecting payloads into vulnerable inputs. Use browser dev tools to modify dangerousUrl dynamically. In red teaming, deliver via reflected/stored XSS vectors targeting Angular apps.

## Detection

- Browser console logs for javascript: URL bindings or sanitizer bypass calls.
- CSP violations if 'unsafe-inline' is blocked.
- Anomalous network requests from javascript: payloads or DOM manipulations via script execution.

## Related

- [[procedures/Bypass-Angular-DomSanitizer-for-XSS-Injection]]
- [[commands/angular-bypass-security-trust-url]]
