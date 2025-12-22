---
id: p-host-malicious-json
tags:
  - xss
  - payload
  - json
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T03:16:14.707Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Host Malicious JSON on Attacker Domain

## Summary

This procedure sets up a server on an attacker-controlled domain to serve a forged Livefyre JSON response containing malicious JavaScript in the 'bodyHtml' field, enabling XSS execution when loaded by the vulnerable script.

## Description

The JSON mimics a valid Livefyre API response for a content thread, including fields like collectionId, id, authorId, and crucially, bodyHtml with unsanitized HTML/JS. When fetched via the vulnerable parameter, it's inserted directly into the DOM on newsroom.uber.com. Requires a web server capable of serving JSON; example uses a PHP endpoint for dynamic response.

## Requirements

1. Control over a domain (e.g., danylod.com) with DNS pointed to your server
2. Web server software (e.g., Apache with PHP)
3. Knowledge of Livefyre JSON structure from prior analysis

## Defense

Defensive measures and detection strategies:

- Enforce strict CORS policies on API endpoints
- Sanitize all HTML/JS fields in third-party JSON responses
- Log and alert on fetches from untrusted domains

## Objectives

1. Create a realistic JSON payload that evades basic structure checks
2. Embed executable JavaScript for domain-context execution
3. Ensure payload delivery via HTTP GET

## Instructions

### Step 1: Set Up Web Server

**Context**: Configure your server to host the malicious file.

Install and start a web server on your domain, e.g., using XAMPP or a VPS with Apache/PHP. Create a directory for the payload.

**Expected Output**: Server running and accessible at https://your-domain/.

### Step 2: Craft the Malicious JSON

**Context**: Build the JSON to match Livefyre's expected format with injected payload.

Create uber.php with: <?php header('Content-Type: application/json'); echo json_encode([ 'collectionId' => '131560603', 'id' => '307477931', 'authorId' => '123', 'bodyHtml' => '<marquee>XSS</marquee><script>alert("XSS on "+ document.domain)</script>' ]); ?>

**Expected Output**: File serves valid JSON when accessed.

### Step 3: Test Payload Accessibility

**Context**: Verify the endpoint responds correctly.

Visit https://bootstrap.your-domain/uber.php in a browser or use curl to fetch. Check for proper JSON and no syntax errors.

**Expected Output**: JSON loads with bodyHtml containing the script tag.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used

- Web server (Apache/PHP)

## Tags

- [[xss]]
- [[payload]]
- [[json]]
