---
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:40Z'
updated_at: '2023-04-06T03:56:40Z'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - '[[techniques/Phishing|T1566 - Phishing]]'
sub_techniques: []
tags:
  - '[[tags/phishing]]'
  - '[[tags/tabnabbing]]'
  - '[[tags/detection]]'
  - '[[tags/link-analysis]]'
commands:
  - '[[commands/grep-search-html-target-blank-links]]'
platforms:
  - Web
tools: []
validated: true
---

# Hunt-for-Tabnabbing-Enabling-Links

## Summary

This procedure identifies potentially malicious HTML links that use the `target="_blank"` attribute without accompanying security measures like `rel="noopener noreferrer"`. Such links can enable Tabnabbing attacks, where an attacker manipulates a background tab to display phishing content when the user switches back, potentially leading to credential theft or session hijacking.

## Description

Tabnabbing is a phishing technique that exploits users leaving multiple tabs open in their browser. When the user switches tabs, JavaScript in the inactive tab can detect the blur event and replace the page content with a fake login form or malicious site. Links with `target="_blank"` are risky because the new tab can access the `window.opener` property of the original page, allowing potential manipulation or data exfiltration. This procedure focuses on hunting for these insecure link formats in web source code, server logs, or captured traffic to detect and mitigate phishing setups. It is particularly useful for security teams reviewing web applications, emails, or third-party content for vulnerabilities. By flagging these links, organizations can prevent social engineering attacks that bypass traditional filters.

## Requirements

1. Access to HTML source code, web server logs, or network traffic captures (e.g., via browser dev tools, wget, or proxy like Burp Suite).
2. Basic knowledge of HTML and regular expressions for pattern matching.
3. Tools like grep (available on Linux/macOS) or equivalent search functionality in Windows PowerShell.
4. Permission to inspect web content without violating privacy policies.

## Defense

- Educate users on phishing risks and encourage verifying URLs before entering credentials.
- Enforce browser policies or extensions (e.g., uBlock Origin, NoScript) to block or warn on suspicious JavaScript behaviors.
- Implement Content Security Policy (CSP) headers to restrict script execution and frame navigation.
- Use web application firewalls (WAFs) to scan for and block insecure link patterns in outgoing content.
- Enable multi-factor authentication (MFA) to limit damage from stolen sessions.

## Objectives

1. Locate HTML anchors (`<a>`) tags using `target="_blank"` in web content.
2. Verify absence of protective `rel` attributes like `noopener noreferrer` to identify high-risk links.
3. Document and remediate suspicious links to prevent Tabnabbing exploitation.

## Instructions

### Step 1: Acquire Web Content for Analysis

**Context**: Obtain the HTML source or log files containing potential links. This could be from viewing page source in a browser, downloading a page with curl/wget, or extracting from proxy logs. Focus on user-facing content like emails, web apps, or ads where phishing might occur.

Save the content to a file, e.g., `page.html` or `logs.txt`, for searching.

### Step 2: Search for Links with Target Blank Attribute

**Context**: Use pattern matching to find all `<a>` tags with `target="_blank"`, as these open links in new tabs/windows and are a hallmark of Tabnabbing setups. This step identifies candidates for further inspection.

**Command** ([[commands/grep-search-html-target-blank-links]]):
```bash
grep -i -o '<a[^>]*target=["'']_blank["''][^>]*>' file.html
```

> This command searches case-insensitively for opening `<a>` tags containing `target="_blank"` or `target='_blank'`, outputting the matching lines. It helps isolate links without pulling in closing tags or unrelated content. Run it on the acquired file to list potential risky links.

### Step 3: Inspect for Missing Security Attributes

**Context**: For each identified link, manually or programmatically check if the `rel` attribute includes `noopener noreferrer`. Missing these allows the new page to reference and manipulate the opener window, enabling Tabnabbing. Use the example code below to understand suspicious formats.

Review the output from Step 2. If `rel` is absent or incomplete (e.g., empty or only `nofollow`), flag the link. For automation, pipe the grep output to another grep excluding safe patterns:
```bash
grep -i -o '<a[^>]*target=["'']_blank["''][^>]*>' file.html | grep -v 'rel=["'']noopener\( noreferrer\)?["'']'
```

> This filters to show only links without the protective `rel`. Expected: Lines with insecure `<a>` tags. If no output, the content is likely secure.

**Code** ([[codes/html-anchor-target-blank-examples]]):

The following examples illustrate common insecure link formats used in Tabnabbing:

```html
<a href="..." target="_blank" rel="" />
or
<a href="..." target="_blank" />
```

> These show a link with an empty `rel` and one without `rel` at all. In a real hunt, replace `...` with actual URLs from your output and test in a safe environment (e.g., isolated browser) to confirm behavior.

### Step 4: Validate and Remediate

**Context**: Test flagged links in a controlled browser to observe if switching tabs triggers content changes (indicating JavaScript for Tabnabbing). Report findings and recommend fixes like adding `rel="noopener noreferrer"` to all `target="_blank"` links.

Expected: Confirmation of insecure behavior or safe patterns. Document links with their context (e.g., page URL, source).
