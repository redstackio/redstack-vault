---
tags:
  - clickjacking
  - iframe
  - html-creation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/create-clickjacking-test-html]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:12.324Z'
sub_techniques: []
id: 92a2eca3-ffc5-4ab3-b53e-209aa22849a7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-HTML-File-for-Clickjacking-Test

## Summary

This procedure creates a simple HTML file that embeds a target URL in an iframe using the sandbox attribute to allow scripts and forms, simulating a clickjacking setup to test for missing frame protections like X-Frame-Options.

## Description

In a clickjacking attack, an attacker embeds a vulnerable page in an iframe on a malicious site to overlay invisible elements, tricking users into clicking unintended actions. This procedure focuses on generating the test HTML for the Legal Robot email verification page (https://app.legalrobot-uat.com/pending-verification), which lacks X-Frame-Options, allowing embedding from external domains. The sandbox attribute permits necessary interactions while isolating the iframe. Prerequisites include a local environment with bash access; expected outcome is a verifiable HTML file ready for browser testing.

## Requirements

1. Bash shell access on Linux/macOS or compatible environment (e.g., Git Bash on Windows)
2. Write permissions in the current directory
3. Knowledge of the target URL for iframe src

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN in HTTP headers to prevent framing
- Use Content-Security-Policy (CSP) with frame-ancestors directive to restrict embedding domains
- Monitor for anomalous iframe requests or unusual referrer headers in server logs

## Objectives

1. Generate a test artifact for clickjacking validation
2. Prepare for browser-based verification of framing vulnerability
3. Document the setup for reproducibility in reporting

## Instructions

### Step 1: Create the HTML File

**Context**: Use a heredoc in bash to write the iframe-containing HTML to a file, ensuring the sandbox allows scripts and forms for realistic testing.

**Command** ([[commands/create-clickjacking-test-html]]):
```bash
cat > index.html << EOF
<!DOCTYPE html>
<html>
<body>
<iframe sandbox="allow-scripts allow-forms" src="https://app.legalrobot-uat.com/pending-verification" width="1000" height="600"></iframe>
</body>
</html>
EOF
```

> This command outputs the HTML structure to `index.html`. Verify creation with `ls index.html` or `cat index.html`. Successful execution creates the file without syntax errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/create-clickjacking-test-html]]

## Tools Used


## Tags

- [[clickjacking]]
- [[iframe-embedding]]
