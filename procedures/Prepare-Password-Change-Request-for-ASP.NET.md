---
tags:
  - asp-net
  - password-reset
  - request-preparation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-prepare-password-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:12.218Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 6e309b18-6be5-4c4e-8273-e533fe95abb7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Prepare-Password-Change-Request-for-ASP.NET

## Summary

This procedure involves constructing or capturing the HTTP POST request structure for a password change in an ASP.NET application, focusing on form parameters like __VIEWSTATE to enable subsequent exploitation without authentication.

## Description

In ASP.NET web applications, password changes are typically handled via POST requests to endpoints like /Login.aspx, including hidden fields for view state management. This procedure prepares such a request by identifying and templating all necessary fields, such as txtEMail, txtNewPassword, __EVENTTARGET, __EVENTARGUMENT, txtMail, reqEMailE_ClientState, revEMailE_ClientState, and btnNewPassword=Submit. It targets scenarios where the server processes these requests without verifying user authentication or email ownership, allowing arbitrary resets. Prerequisites include access to the target URL and basic knowledge of HTTP form submissions.

## Requirements

1. Network access to the target ASP.NET application (e.g., https://example.mil/Login.aspx)
2. Victim's email address
3. Burp Suite or similar proxy tool for request inspection
4. Basic understanding of ASP.NET ViewState mechanics

## Defense

Defensive measures and detection strategies:

- Implement server-side authentication checks before processing password changes
- Require email verification tokens or CAPTCHA for reset requests
- Monitor for anomalous POST requests to /Login.aspx from unauthenticated IPs
- Use Web Application Firewall (WAF) rules to validate __VIEWSTATE integrity

## Objectives

1. Create a reusable template for the password change POST request
2. Ensure inclusion of all ASP.NET-specific form fields
3. Prepare for token extraction in subsequent steps

## Instructions

### Step 1: Identify Form Fields

**Context**: Examine the login or password change form to list all required parameters.

**Command** ([[commands/curl-prepare-password-request]]):
```bash
curl -X GET https://example.mil/Login.aspx -c cookies.txt
```

> This fetches the login page and saves cookies, allowing inspection of the HTML source for form fields like __VIEWSTATE via browser dev tools or grep on the response.

### Step 2: Construct Request Template

**Context**: Build the POST body template with placeholders.

**Command** ([[commands/curl-prepare-password-request]]):
```bash
curl -X POST https://example.mil/Login.aspx \
  -d "__VIEWSTATE=[PLACEHOLDER]&__EVENTVALIDATION=[PLACEHOLDER]&txtEMail=[VICTIM_EMAIL]&txtNewPassword=[DESIRED_PASSWORD]&btnNewPassword=Submit" \
  -b cookies.txt -v
```

> Prepare the curl command as a template; do not send yet. Replace placeholders later. Expected output: A dry-run verbose response showing the request structure without submission.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-prepare-password-request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[asp-net]]
- [[password-reset]]
