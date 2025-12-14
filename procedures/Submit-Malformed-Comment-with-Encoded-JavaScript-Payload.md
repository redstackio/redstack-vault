---
id: proc-submit-xss-comment
tags:
  - xss
  - stored-xss
  - wordpress
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:19.133Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Malformed-Comment-with-Encoded-JavaScript-Payload

## Summary

This procedure injects a stored XSS payload into WordPress comments using an encoded javascript: URL in an anchor tag, which evades initial esc_url() sanitization.

## Description

In a pre-authentication context, submit a comment on a WordPress post containing a hyperlink with a javascript\x3aalert(1) scheme. The encoding (\x3a for ':') prevents immediate detection by wp_parse_url() checks that enforce http/https schemes. The payload remains dormant until processed later during admin editing, where stripcslashes() in shortcode_parse_atts() decodes it. This targets WordPress sites with comments enabled, leading to potential JS execution in admin or viewer contexts.

## Requirements

1. Access to a public WordPress post with comments enabled
2. No authentication needed
3. Web browser for form submission

## Defense

Defensive measures and detection strategies:

- Disable comments or moderate them strictly
- Update WordPress to patch versions addressing URL sanitization
- Implement Content Security Policy (CSP) to block inline JS execution
- Monitor admin edit logs for unusual comment modifications

## Objectives

1. Store a latent XSS payload in comments without triggering sanitization
2. Set up for payload activation via admin interaction
3. Prepare for arbitrary JS execution upon decoding

## Instructions

### Step 1: Navigate to Target Post

**Context**: Locate a blog post where comments can be submitted anonymously.

Open the WordPress site in a browser and go to a post URL, e.g., http://target.com/post-title/.

### Step 2: Craft and Submit Comment

**Context**: Compose the comment with the encoded payload to appear legitimate while hiding the malicious href.

Enter the following comment text in the comment form:

```
Hi! I really enjoy your work. We've also written a blog post about it here: http://dummysite.com/awesome-blogpost. Feel free to check it out! <a href="javascript\x3aalert(1);">Visit my web page</a>
```

Submit the comment.

> The payload uses \x3a to encode the colon, bypassing initial esc_url() validation. Expected output: Comment posts successfully, visible on the page but href appears as javascript\x3aalert(1) in source.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[wordpress]]
