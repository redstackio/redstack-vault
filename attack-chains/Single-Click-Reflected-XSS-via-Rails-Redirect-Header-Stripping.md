---
id: ac-rails-redirect-xss-1955370
tags:
  - xss
  - rails
  - redirect
  - javascript
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Set-Up-Vulnerable-Rails-App]]'
  - '[[procedures/Send-Crafted-Redirect-Request]]'
  - '[[procedures/Trigger-XSS-via-Fallback-HTML]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:27.903Z'
description: >-
  Exploits a vulnerability in Ruby on Rails redirect_to function where control
  characters in user-supplied URLs cause the Location header to be stripped,
  leading to a fallback HTML redirect with a user-controlled href that enables
  reflected XSS on click.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Single-Click Reflected XSS via Rails Redirect Header Stripping

Multi-stage attack chain demonstrating exploitation of a Ruby on Rails vulnerability where control characters like %08 (backspace) in redirect URLs cause Rack to strip the Location header, resulting in a fallback HTML response with a clickable user-controlled href that executes JavaScript payloads for reflected XSS.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Vulnerable App] --> B[Inject Malicious Redirect URL]
    B --> C[Trigger XSS on Click]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard Rails development environment)

### Target Environment

- Ruby on Rails 7.0.4.3 or similar vulnerable version
- Rack web server (e.g., Puma)
- Port 3000 open for local testing
- Network access to the Rails application endpoint

### Initial Access Requirements

- Access to deploy or test a Rails application (developer access)
- No prior credentials needed for the PoC, but in production, requires tricking a victim into visiting the endpoint

## Detailed Attack Procedures

### Step 1: Set Up Vulnerable Rails Application
procedure: [[procedures/Set-Up-Vulnerable-Rails-App]]

**Objective**: Create a Rails controller and route that uses redirect_to with allow_other_host: true on a user-supplied parameter, making it vulnerable to header stripping.

**Instructions**: Generate a new Rails app if needed, then add a controller with a vulnerable action and define the route. Start the server with `rails server`.

**Expected Output**: Server running on http://localhost:3000, with /vuln endpoint accessible.

**Success Indicators**:
- Rails server starts without errors
- GET /vuln returns a redirect or fallback response

### Step 2: Send Crafted Request to Vulnerable Endpoint
procedure: [[procedures/Send-Crafted-Redirect-Request]]

**Objective**: Inject a JavaScript URI payload with a control character (%08) into the redirect_url parameter to trigger Location header removal by Rack linters.

**Instructions**: Use a browser or curl to send the request to the /vuln endpoint with the malicious redirect_url. The %08 backspace causes non-compliance with RFC7230, stripping the header.

Execute [[commands/curl-rails-redirect-poc]]:

```bash
curl -v "http://localhost:3000/vuln?redirect_url=javascript:alert(document.cookie)%08"
```

**Expected Output**: HTTP 302 response without Location header, containing fallback HTML with the href set to the JS payload.

**Success Indicators**:
- No Location header in response headers
- HTML body includes <a href="javascript:alert(document.cookie) ">redirected</a>

### Step 3: Observe Response and Trigger XSS
procedure: [[procedures/Trigger-XSS-via-Fallback-HTML]]

**Objective**: Victim clicks the link in the fallback HTML, executing the JavaScript payload for reflected XSS, such as stealing cookies.

**Instructions**: View the response in a browser; the fallback message prompts a click, executing the JS URI.

**Expected Output**: Alert box showing document.cookie or other malicious action on click.

**Success Indicators**:
- JavaScript executes on link click
- Potential cookie theft or session hijacking

## Attack Chain Summary

### Key Achievements

1. Bypassed redirect mechanism via control character injection
2. Controlled fallback HTML href for XSS delivery
3. Enabled single-click execution of arbitrary JavaScript in a web context

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution
- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
