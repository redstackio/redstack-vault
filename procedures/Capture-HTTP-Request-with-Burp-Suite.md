---
id: proc-capture-request-burp
tags:
  - recon
  - http-intercept
  - burp
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:46:26.019Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Capture-HTTP-Request-with-Burp-Suite

## Summary

Intercept and capture the HTTP GET request to the vulnerable RequestAccess.asp endpoint using Burp Suite to analyze and prepare for parameter manipulation in SQL Injection testing.

## Description

Burp Suite acts as a proxy to capture traffic from the authenticated session to /██████mil/AFServices/RequestAccess.asp, including parameters like selMajcom and session cookies. This allows inspection of the request structure before injecting payloads. The target environment is a web application over HTTPS on port 443.

## Requirements

1. Burp Suite installed and running with proxy listener on 127.0.0.1:8080
2. Browser configured to use Burp proxy
3. Active user session from account creation

## Defense

Defensive measures and detection strategies:

- Enable HSTS and monitor for proxy interception via certificate pinning
- Log unusual request patterns or proxy headers

## Objectives

1. Capture the exact request format to the vulnerable endpoint
2. Preserve session authentication in the intercepted request
3. Identify injectable parameters like selMajcom

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp Suite to intercept traffic.

Launch Burp Suite and ensure the proxy tab is active with intercept on.

> Browser traffic will now route through Burp.

### Step 2: Trigger Request

**Context**: Send the request to the endpoint while intercepting.

With authentication, navigate to or submit the form at https://████████mil/AFServices/RequestAccess.asp?selMajcom=MAT\*&selbase=MXRD&Submitted=1&Appid=29&FuncID=23&App=Activity+Database+FMP.

Intercept the GET request in Burp, noting headers like Cookie for session.

> Expected output: Full request displayed in Burp Proxy > Intercept tab, including vulnerable parameters.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[recon]]
- [[http-intercept]]
