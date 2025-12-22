---
tags:
  - xss
  - stored-xss
  - concrete-cms
  - injection
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:37.325Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: c810ea8e-d28c-4ccb-8015-599c72f9c799
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-in-SEO-Name-Field

## Summary

This procedure exploits a stored XSS vulnerability in the Name field of the Pages SEO dialog in Concrete CMS 8.1.0 by injecting JavaScript event handlers via HTML attributes, which bypass strip_tags sanitization. The payload persists in the database and executes when admins view the SEO dialog or Page Search, allowing potential session hijacking or unauthorized actions on behalf of higher-privileged users.

## Description

The vulnerability stems from insufficient sanitization in the Page::update() method, where Text::sanitize() removes full HTML tags but not attributes like onmouseover or onfocus. A low-privileged user can inject payloads such as 'Page Name" onmouseover="alert('XSS')"' into the cName parameter during form submission. When an admin interacts with the affected page in the admin interface, the payload executes in their browser context. This can be used for social engineering attacks to steal admin sessions, redirect to phishing sites, or perform actions like adding backdoors. The target environment is Concrete CMS 8.1.0 on PHP 5.6.30 with Apache and MySQL. Prerequisites include authenticated access as a low-priv user and admin interaction for triggering.

## Requirements

1. Valid low-privileged credentials for Concrete CMS login
2. Web browser access to the instance (e.g., http://target.com/dashboard)
3. Knowledge of the target page to modify via sitemap
4. Optional: Developer tools to inspect form POST requests for payload refinement

## Defense

Defensive measures and detection strategies:

- Implement comprehensive input sanitization using HTMLPurifier or similar to strip/encode attributes in addition to tags
- Enforce Content Security Policy (CSP) headers to restrict inline JavaScript execution
- Monitor database for suspicious entries in page metadata tables (e.g., via SQL queries for script patterns)
- Use Web Application Firewall (WAF) rules to detect event handler injections in POST data
- Regularly audit admin interfaces for reflected/stored content with tools like OWASP ZAP

## Objectives

1. Inject and store a JavaScript payload in the SEO Name field to bypass sanitization
2. Trigger execution in an admin's browser to steal session data or escalate privileges
3. Demonstrate potential for persistent attacks via social engineering

## Instructions

### Step 1: Authenticate and Navigate to Sitemap

**Context**: Establish a session and reach the interface for page selection to access the vulnerable SEO form.

Navigate to the login page, authenticate with low-priv credentials, then go to Dashboard > Full Sitemap (/dashboard/sitemap/full). Select a page to open its options popup and choose SEO.

> This loads the form with the editable cName field. Expected: SEO dialog opens without errors.

### Step 2: Craft and Inject Payload

**Context**: Modify the Name field to include an event handler that executes JavaScript, appending to the existing name to avoid detection.

In the Name field, enter: ExistingName" onmouseover="alert('Stored XSS')" autofocus=". For auto-execution, use onfocus with autofocus attribute. Submit the POST request to the update endpoint.

> The payload bypasses strip_tags as it uses attributes, not full tags. Expected: Form submits; no immediate errors.

### Step 3: Persist and Verify Injection

**Context**: Save the changes to store the payload in the database via Page::update(), then verify persistence.

Click "Save changes". Optionally, inspect the database (e.g., CollectionName table) for the injected string or reopen the dialog to confirm the payload is present.

> Payload is now stored persistently. Expected: Save confirmation; payload visible on reload.

### Step 4: Trigger and Exploit

**Context**: Induce execution by simulating or social-engineering admin view of the affected interface.

Reopen the SEO dialog or go to Page Search (/dashboard/sitemap/search). Hover over the Name field or load with autofocus to execute. In exploitation, replace alert with code to exfiltrate document.cookie to an attacker server.

> JavaScript runs in admin context. Expected: Alert or network request to attacker endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- stored-xss
- concrete-cms
- injection
- session-hijacking
