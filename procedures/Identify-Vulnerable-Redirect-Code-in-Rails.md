---
tags:
  - rails
  - recon
  - vulnerability-identification
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-get-endpoint]]'
verified: false
platforms:
  - Web
  - Ruby on Rails
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:27.491Z'
sub_techniques: []
id: 463e5f1c-4796-4f50-80ae-b5b51fcf92cf
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Vulnerable-Redirect-Code-in-Rails

## Summary

This procedure identifies Ruby on Rails controllers using redirect_to or polymorphic_url helpers with untrusted user input, such as params[:some_param], which are susceptible to array parameter manipulation for method invocation and information disclosure.

## Description

In vulnerable Rails applications, unauthenticated routes that redirect based on user-controlled parameters without validation allow attackers to probe for internal routes and methods. The target environment is a web application running Ruby on Rails with Action Pack, accessible over HTTP/HTTPS. Prerequisites include network access to the application and basic knowledge of Rails routing. Expected outcomes include confirmation of vulnerable endpoints through response analysis, enabling further exploitation.

## Requirements

1. Network access to the Rails application
2. Tools for HTTP requests (e.g., curl or browser)
3. Access to application source code if available, or ability to infer from responses

## Defense

Defensive measures and detection strategies:

- Implement input validation and allowlisting for redirect parameters (e.g., case statement checking valid values)
- Use Rails' safe redirect methods or force string conversion with .to_s
- Monitor for unusual 500 errors or redirects with array parameters in logs
- Enable detailed error logging but suppress sensitive details in production

## Objectives

1. Locate endpoints vulnerable to array parameter injection
2. Confirm lack of sanitization in redirect logic
3. Prepare for targeted probing of routes and methods

## Instructions

### Step 1: Enumerate Potential Endpoints

**Context**: Identify unauthenticated routes that may use dynamic redirects by testing common parameter patterns.

**Command** ([[commands/curl-get-endpoint]]):
```bash
curl -v -X GET "http://target.com/login?redirect_url=test" -o response.html
```

> This sends a basic GET request to probe for redirect behavior. Inspect the -v verbose output for Location headers influenced by the parameter, indicating potential vulnerability.

### Step 2: Analyze Application Behavior

**Context**: Review responses or source code for patterns like redirect_to(params[:some_param]) in controllers.

**Command** ([[commands/curl-get-endpoint]]):
```bash
curl -v -X GET "http://target.com/vulnerable?some_param=/admin" -o response.html
```

> If the redirect follows the parameter value without validation, it confirms the endpoint is exploitable. Look for 302 status and dynamic Location.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-get-endpoint]]

## Tools Used


## Tags

- rails
- redirect
- vulnerability-scan
