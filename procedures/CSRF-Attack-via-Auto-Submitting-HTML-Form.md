---
id: 5eb898bb-8d30-47c0-bd9f-3258929cd086
name: CSRF-Attack-via-Auto-Submitting-HTML-Form
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:55.445143+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Subvert Trust Controls|T1553 - Subvert Trust Controls]]'
sub_techniques: []
tags:
  - '[[tags/Cross-Site Request Forgery]]'
  - '[[tags/HTML POST - AutoSubmit - No User Interaction]]'
  - '[[tags/Payloads]]'
  - csrf
  - web-attack
commands: []
platforms:
  - Web
tools: []
validated: true
---

# CSRF-Attack-via-Auto-Submitting-HTML-Form

## Summary

This procedure exploits Cross-Site Request Forgery (CSRF) by crafting a malicious HTML form that automatically submits a POST request to a target website when a victim visits the attacker's site. The form includes hidden fields with the malicious payload, allowing unauthorized actions like changing user settings or initiating transactions without the victim's knowledge, assuming they are authenticated to the target site.

## Description

CSRF attacks leverage a victim's authenticated session on a trusted site by tricking them into submitting malicious requests from an attacker-controlled domain. In this technique, an HTML form is created with the target action URL and payload in hidden inputs. JavaScript automatically submits the form upon page load, bypassing user interaction. This is effective against sites lacking CSRF tokens or SameSite cookie protections. The attack requires the victim to visit the malicious page while logged into the target, leading to actions such as account modifications, data changes, or financial transactions. It targets web applications vulnerable to request forgery, commonly in e-commerce, banking, or admin panels.

## Requirements

1. Ability to host a malicious HTML page on an attacker-controlled website or server (e.g., via a phishing link or compromised site).
2. Knowledge of the target website's POST endpoint URL and required form parameters for the unauthorized action.
3. Victim must be authenticated (logged in) to the target website with an active session cookie.
4. No CSRF protections (tokens or SameSite=Strict/Lax) on the target endpoint.

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens: Require unique, unpredictable tokens in forms and validate them server-side to ensure requests originate from the legitimate site.
- Use SameSite cookie attributes: Set cookies to SameSite=Strict or Lax to prevent cross-site submission.
- Educate users: Warn against clicking links or visiting untrusted sites while logged into sensitive accounts; promote use of multi-factor authentication (MFA).
- Content Security Policy (CSP): Enforce strict CSP headers to block inline scripts or form submissions from external domains.
- Monitor for anomalous requests: Log and alert on requests from unexpected referer headers or IP addresses.

## Objectives

1. Execute unauthorized POST actions on the victim's behalf, such as modifying account settings or initiating transfers.
2. Demonstrate or exploit lack of CSRF protections to gain unauthorized access or control over victim accounts.
3. Collect evidence of vulnerability for reporting or further exploitation in a chained attack.

## Instructions

### Step 1: Identify Target Endpoint and Payload

**Context**: Determine the vulnerable POST endpoint on the target site and the exact parameters needed for the malicious action. This requires reconnaissance, such as inspecting the target's legitimate forms via browser developer tools or proxy interception.

Inspect the target site's form (e.g., using browser dev tools) to note the action URL (e.g., http://www.example.com/api/setusername) and required fields (e.g., username). Decide on the payload value that achieves the objective, such as setting a username to a controlled value.

**Expected Output**: Documented endpoint URL, method (POST), and payload parameters (e.g., username=malicious_value).

### Step 2: Craft the Malicious HTML Form

**Context**: Create the HTML payload using the identified endpoint and parameters. Embed it in a full HTML page for hosting.

Use the following code snippet as the basis: [[codes/CSRF-Auto-Submit-HTML-POST-Payload]]. Customize the action URL and hidden input values to match the target. Optionally, add disguising elements like fake content to lure the victim.

**Expected Output**: A complete HTML file ready for hosting, with auto-submit functionality.

### Step 3: Host and Distribute the Malicious Page

**Context**: Deploy the HTML page on an attacker-controlled server and entice the victim to visit it while authenticated to the target.

Host the file on a web server (e.g., Apache, Nginx, or a simple Python HTTP server). Distribute via phishing email, social engineering, or malicious links. Ensure the page loads quickly to submit the form before the victim notices.

**Expected Output**: The page is accessible via a URL (e.g., http://attacker.com/csrf.html), and the form submits silently upon load.

### Step 4: Verify Execution

**Context**: Confirm the attack succeeded by checking the target's response or changes on the victim's account.

After the victim visits, monitor the target site or use a proxy to intercept if possible. Log into the victim account (if compromised) or observe effects like username changes.

**Expected Output**: Successful POST submission reflected in target site changes (e.g., updated username) without user interaction.

### Step 5: Clean Up and Mitigate

**Context**: Remove the hosted page and report the vulnerability if in a testing scenario.

Delete the malicious HTML from the server. If authorized testing, document findings and recommend fixes to the target site owners.

**Expected Output**: No residual malicious content; vulnerability report if applicable.
