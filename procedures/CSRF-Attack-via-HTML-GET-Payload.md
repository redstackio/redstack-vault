---
type: procedure
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/Cross-Site Request Forgery]]'
  - '[[tags/HTML GET - No User Interaction]]'
  - '[[tags/Payloads]]'
commands: []
tools: []
platforms:
  - Web
skill_level: beginner
impact_level: medium
detection_risk: low
verified: true
validated: true
---

# CSRF-Attack-via-HTML-GET-Payload

## Summary

This procedure demonstrates a Cross-Site Request Forgery (CSRF) attack using a simple HTML GET payload embedded in an image tag. The payload tricks the victim's authenticated browser into sending an unauthorized request to a vulnerable web application, such as changing the user's username without their knowledge or consent. This no-interaction attack exploits the trust in the victim's session cookies and is effective against sites lacking CSRF protections like tokens.

## Description

CSRF attacks leverage the browser's automatic inclusion of authentication cookies in requests to the target site. In this scenario, the attacker crafts an HTML snippet that, when loaded in the victim's browser (e.g., via a malicious webpage or email), triggers a GET request to the target's API endpoint. For example, it targets an endpoint like /api/setusername that updates the username without proper validation. The attack requires the victim to be authenticated to the target site and visit the attacker's controlled resource. It is particularly dangerous for state-changing operations accessible via GET, which should be avoided in secure designs. This procedure assumes a public-facing web application vulnerable to CSRF and focuses on payload delivery via HTML.

## Requirements

1. Knowledge of the target's vulnerable endpoint (e.g., a GET-based username change API without CSRF tokens).
2. Ability to deliver HTML content to the victim, such as hosting a malicious webpage or embedding in an email/phishing link.
3. Victim must be authenticated to the target site via an active browser session.
4. No special tools required; a text editor or basic web hosting suffices.

## Defense

- Implement CSRF tokens in all state-changing forms and endpoints to validate request origin.
- Use SameSite=Strict or SameSite=Lax cookies to prevent credential inclusion in cross-site requests.
- Enforce POST for sensitive actions instead of GET to reduce accidental triggers.
- Educate users to log out of sensitive sites and avoid clicking untrusted links.
- Monitor for anomalous requests from unusual referers or user agents.

## Objectives

1. Trick the victim into executing an unauthorized action on the target site without interaction.
2. Demonstrate exploitation of missing CSRF protections in public-facing applications.
3. Achieve account modification, such as username changes, to facilitate further attacks like social engineering.

## Instructions

### Step 1: Identify the Vulnerable Endpoint

**Context**: Determine the exact API or form endpoint that performs the desired action (e.g., username update) via GET without CSRF protection. This can be found through reconnaissance, such as reviewing the site's source code, API documentation, or testing with developer tools.

Inspect the target site's network traffic while performing the action legitimately to capture the request URL and parameters.

### Step 2: Craft the CSRF Payload

**Context**: Create the HTML payload using an image tag to disguise the malicious request as a benign resource load. The src attribute points to the vulnerable endpoint with the attacker's desired parameters.

Use the following code snippet [[codes/HTML-IMG-CSRF-Payload-for-Username-Change]]:

```html
<img src="http://www.example.com/api/setusername?username=CSRFd">
```

Replace the URL with the actual target endpoint and adjust parameters (e.g., username value) to achieve the objective.

### Step 3: Deliver the Payload to the Victim

**Context**: Host the HTML payload on an attacker-controlled site or embed it in a phishing email, forum post, or advertisement that the victim will load in their browser while authenticated to the target.

Create a simple HTML page containing the img tag and host it (e.g., on a free web host). Send the link to the victim via email or social engineering. When the victim visits, the browser automatically fetches the image, triggering the request.

### Step 4: Verify the Attack Success

**Context**: Confirm the action was performed by checking the victim's account on the target site or monitoring for changes.

Access the target site with the victim's credentials (if obtained separately) or observe behavioral changes, such as error messages on login due to the modified username.
