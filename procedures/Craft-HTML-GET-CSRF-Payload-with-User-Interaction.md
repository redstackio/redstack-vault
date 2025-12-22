---
type: procedure
description: >-
  A procedure to create and deliver an HTML-based CSRF payload using a GET
  request that requires user interaction to execute unauthorized actions on a
  target website.
verified: true
submitted: false
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - '[[techniques/Drive-by Compromise|T1189 - Drive-by Compromise]]'
sub_techniques: []
tags:
  - csrf
  - cross-site-request-forgery
  - web-attack
  - user-interaction
  - payloads
commands:
  - '[[commands/curl-test-csrf-endpoint]]'
platforms:
  - Web
tools: []
validated: true
---

# Craft-HTML-GET-CSRF-Payload-with-User-Interaction

## Summary

This procedure outlines how to craft and deploy an HTML GET-based Cross-Site Request Forgery (CSRF) payload that tricks an authenticated user into performing an unintended action on a target website, such as changing account settings or transferring funds, by clicking a malicious link. It requires user interaction and exploits sites vulnerable to CSRF without proper token validation on GET requests.

## Description

CSRF attacks leverage the browser's automatic inclusion of authentication cookies to perform actions on behalf of the victim. In this GET-based variant, the attacker embeds a malicious hyperlink in an email, social media post, or website that, when clicked by an authenticated user, sends a GET request to the target site's vulnerable endpoint. This can lead to unauthorized actions like password resets, data modifications, or credential theft if the endpoint processes the request without additional validation. The procedure is effective against legacy web applications using GET for state-changing operations and assumes the attacker knows the target's session behavior. Success depends on social engineering to induce the click and the absence of CSRF defenses.

## Requirements

1. Knowledge of the target website's vulnerable GET endpoint (e.g., an API that modifies user data without CSRF tokens).
2. Ability to communicate with the victim (e.g., via email or a controlled website) to deliver the payload.
3. Victim must be authenticated to the target site when clicking the link.
4. Basic HTML knowledge and a way to host or embed the malicious link.

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all forms and validate them server-side for state-changing requests.
- Use HTTP POST for sensitive actions instead of GET to prevent link-based exploitation.
- Enforce multi-factor authentication (MFA) and same-site cookie attributes (e.g., 'SameSite=Strict').
- Monitor for anomalous requests from unusual referers or user-agents, and educate users on phishing links.

## Objectives

1. Identify a vulnerable GET endpoint on the target site that performs state changes without CSRF protection.
2. Craft a deceptive HTML link that embeds the malicious GET request parameters.
3. Deliver the payload to induce user interaction and execute the unauthorized action.
4. Verify the action's success through observable changes on the target site.

## Instructions

### Step 1: Identify Vulnerable GET Endpoint

**Context**: Determine an endpoint on the target site that uses GET for sensitive operations, such as updating user profiles or settings, without CSRF token validation. This step ensures the payload targets a real vulnerability.

Inspect the site's API documentation or use browser developer tools to find endpoints like `/api/setusername`. Test if it processes requests without additional auth checks beyond cookies.

**Command** ([[commands/curl-test-csrf-endpoint]]):
```bash
curl -X GET "http://target.com/api/setusername?username=test" -H "Cookie: session=abc123"
```

> This command simulates the GET request with a session cookie to confirm if the endpoint accepts and processes the parameter without tokens. If it returns a success message or updates the data, the endpoint is vulnerable.

### Step 2: Craft the Malicious HTML Payload

**Context**: Create an HTML anchor tag that disguises the malicious GET request as a legitimate link, tricking the user into clicking it while authenticated to the target site.

Replace the example URL and parameters with the actual vulnerable endpoint and desired action (e.g., setting username to attacker-controlled value). Embed this in an email template or webpage.

```html
<a href="http://www.target.com/api/setusername?username=attacker_controlled_value">Click here to update your profile!</a>
```

> The link appears benign but sends the GET request to the target upon click, executing the action using the victim's session.

### Step 3: Deliver the Payload to the Victim

**Context**: Use social engineering to get the victim to click the link while logged into the target site, ensuring their browser sends authenticated cookies.

Embed the HTML link in a phishing email (e.g., "Confirm your account update") or host it on a malicious site and lure the victim via messaging. If delivering via email, use HTML email format to preserve the link.

No specific command needed; use email clients or web hosting to send. Track clicks if possible via URL shorteners or logging on your hosted page.

### Step 4: Verify Execution and Impact

**Context**: Confirm the CSRF succeeded by checking for the intended change on the target site, such as altered user data or performed action.

Log into the target site with an observer account or monitor public changes. Re-run the test command from Step 1 with the malicious parameter to simulate verification.

**Expected Output**: For Step 1 command, a 200 OK response with confirmation like "Username updated successfully" indicates vulnerability and potential success.
