---
tags:
  - xss
  - ruby-on-rails
  - link_to
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:27.085Z'
sub_techniques: []
id: 7ef2b52b-a9b2-4a76-8bc5-4ce8e50c145e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Vulnerable-Rails-View-with-link_to

## Summary

This procedure involves navigating to a Ruby on Rails view that uses the link_to helper with untrusted user parameters, such as params[:back], to set up the conditions for an XSS attack by confirming direct insertion of input into the href attribute.

## Description

In vulnerable Rails applications, developers may pass user-controlled parameters directly to link_to without sanitization, e.g., `<%= link_to 'Back', params[:back] %>`. This allows attackers to inspect and confirm the vulnerability before payload injection. The target environment is a web application running Ruby on Rails, typically on standard HTTP ports. Expected outcomes include rendering a link based on the parameter, enabling further exploitation.

## Requirements

1. Network access to the Rails application
2. Web browser for navigation and source inspection
3. Knowledge of the endpoint using the vulnerable link_to (e.g., from source code review or error messages)

## Defense

Defensive measures and detection strategies:

- Sanitize or validate URL parameters in views using Rails helpers like url_for or safe URL whitelisting
- Implement Content Security Policy (CSP) to block inline JavaScript execution
- Monitor for unusual parameter values in access logs

## Objectives

1. Confirm the presence of unescaped params in link_to href
2. Establish baseline for payload testing
3. Identify the exact view rendering the vulnerable link

## Instructions

### Step 1: Identify the Vulnerable Endpoint

**Context**: Determine the URL path that triggers the view with the link_to helper using params.

Visit a known or guessed endpoint, such as `http://target-app.com/users?back=/profile`, and use browser developer tools to inspect the HTML.

> Look for the generated <a> tag in the source to verify params[:back] is inserted directly.

### Step 2: Validate Parameter Insertion

**Context**: Test with a benign parameter to ensure no filtering occurs.

Append a safe value like `?back=/home` and reload. Inspect the source for `<a href="/home">Back</a>`.

> If the parameter appears unescaped, the view is vulnerable to further manipulation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[ruby-on-rails]]
- [[link_to]]
