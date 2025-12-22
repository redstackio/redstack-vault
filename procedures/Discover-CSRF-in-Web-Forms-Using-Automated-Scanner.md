---
id: proc-uuid-001
tags:
  - csrf
  - web-scanning
  - vulnerability-discovery
type: procedure
tools:
  - '[[tools/Acunetix]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/http-get-enterprise-form]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:03.139Z'
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
# Discover-CSRF-in-Web-Forms-Using-Automated-Scanner

## Summary

This procedure uses an automated web vulnerability scanner to identify Cross-Site Request Forgery (CSRF) vulnerabilities in HTML forms lacking protection tokens, enabling attackers to forge requests and trick authenticated users into performing unintended actions like submitting contact form data.

## Description

In this attack scenario, a web application at http://try.crashlytics.com/enterprise/ exposes an HTML form using the GET method without CSRF tokens or other countermeasures. The form accepts inputs for name, email, and comment, allowing an attacker to craft malicious external pages that submit data on behalf of the victim. Discovery occurs through automated scanning, revealing the vulnerability. Prerequisites include network access to the target and a vulnerability scanner like Acunetix. Expected outcomes include a report detailing the unprotected form, with potential impacts ranging from data compromise to full application control if an admin is targeted.

## Requirements

1. Network access to the target web application (e.g., http://try.crashlytics.com/enterprise/)
2. Installed web vulnerability scanner such as Acunetix with Aspect module enabled
3. Basic understanding of HTTP requests and web forms

## Defense

Defensive measures and detection strategies:

- Implement CSRF protection tokens in all forms and validate them server-side
- Use SameSite cookie attributes to prevent cross-site requests
- Monitor for anomalous form submissions from unexpected referers using web application firewalls (WAF)

## Objectives

1. Identify web forms vulnerable to CSRF attacks
2. Assess the potential impact on user data and application security
3. Provide evidence for remediation, such as adding token validation

## Instructions

### Step 1: Configure and Launch Vulnerability Scan

**Context**: Set up the scanner to probe the target URL for common web vulnerabilities, including CSRF in forms.

**Command** ([[commands/http-get-enterprise-form]]):
Use Acunetix to initiate the scan, enabling Aspect for advanced querying.

```bash
acunetix-scan --url http://try.crashlytics.com/enterprise/ --aspect-enabled --aspect-password 082119f75623eb7abd7bf357698ff66c --aspect-queries "filelist;aspectalerts"
```

> This command scans the enterprise page, analyzing HTML forms for protection mechanisms. Expected output includes a report flagging the GET form as vulnerable due to missing CSRF tokens, with details on input fields (name: text, email: text, comment: textarea).

### Step 2: Analyze Scan Results for CSRF

**Context**: Review the generated report to confirm the CSRF vulnerability and document the form's location and method.

No specific command; manually inspect the Acunetix report for alerts on unprotected forms.

> Look for indicators like 'HTML form without CSRF protection' and verify the impact description. Successful analysis yields technical details for exploitation, such as forging a request to submit fake contact data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/http-get-enterprise-form]]

## Tools Used

- [[tools/Acunetix]]

## Tags

- [[csrf]]
- [[web-vulnerability]]
