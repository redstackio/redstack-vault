---
id: proc-idor-bruteforce-burp
tags:
  - idor
  - brute-force
  - web
  - burp-suite
  - dod
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Brute Force]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:23.430Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Brute Force]]'
  - '[[Account Discovery]]'
---
# Brute-Force-IDOR-in-Appointment-Lookup-with-Burp-Suite

## Summary

This procedure exploits an Insecure Direct Object Reference (IDOR) vulnerability in a web-based appointment lookup form by using Burp Suite's Intruder to brute-force predictable 8-character hexadecimal confirmation numbers. It allows unauthorized access to other users' appointments, enabling data leakage (names, phones, emails) and cancellation of processes on a DoD .mil website without rate limiting or protections.

## Description

The target is an ASP.NET application at https://█████████/appointment/lookup.aspx?a=f, where the TbPin parameter accepts 8-hex confirmation numbers without validation against the submitting user's session. By intercepting POST requests and fuzzing TbPin with a hex wordlist, valid numbers can be guessed (e.g., 16^8 = 4.29 billion possibilities, but practical with targeted fuzzing or partial knowledge). Successful hits reveal appointment details and allow actions like cancellation via https://█████████/appointment/lookup.aspx?a=c. Prerequisites include Burp Suite setup and browser proxy configuration. Expected outcomes: Access to PII and demonstration of impact.

## Requirements

1. Burp Suite Professional or Community edition installed
2. Browser configured for proxy interception (e.g., Firefox with manual proxy settings)
3. Wordlist of 8-character hex strings (can be generated via tools like Crunch or custom scripts)
4. Public access to the target .mil website

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on lookup attempts (e.g., IP-based throttling)
- Use CAPTCHA or multi-factor challenges after failed attempts
- Normalize error responses to avoid length-based oracle
- Enforce session-bound references (e.g., UUIDs tied to user sessions)
- Monitor for anomalous request volumes via WAF logs

## Objectives

1. Gain unauthorized access to appointment records via IDOR
2. Exfiltrate personal identifiable information (PII)
3. Demonstrate potential for disrupting services (e.g., cancellations)

## Instructions

### Step 1: Setup Burp Proxy and Browser

**Context**: Establish interception to capture form submissions.

Launch Burp Suite, go to Proxy > Options, and ensure a listener on 127.0.0.1:8080. In browser settings, set proxy to 127.0.0.1:8080 and install Burp CA cert for HTTPS.

> No command; GUI action. Expected: Traffic routed through Burp.

### Step 2: Access and Interact with Target Form

**Context**: Identify the vulnerable endpoint and capture a sample request.

Navigate to https://█████████/appointment/lookup.aspx?a=f. Enter 'Smith' as last name and random hex (e.g., '00000000') in TbPin, submit via 'Next>>', and intercept in Burp.

> No command; browser action. Expected: POST request intercepted with params like __VIEWSTATE, TbPin=00000000.

### Step 3: Send to Intruder and Configure Positions

**Context**: Prepare for payload injection on the vulnerable parameter.

Right-click intercepted request > Send to Intruder. In Positions tab, clear defaults, select TbPin value, Add § (e.g., TbPin=§00000000§). Set Attack type to Sniper.

> No command; GUI. Expected: Payload position marked.

### Step 4: Configure and Launch Payload Attack

**Context**: Brute-force TbPin with hex payloads to find valid references.

In Payloads tab, load 8-char hex wordlist (e.g., all combos of 0-9A-F). In Options, set Grep - Extract to match success strings (e.g., 'appointment found'). Start Attack.

> No command; GUI. Expected: Results table; valid responses have longer lengths or specific content (e.g., user data).

### Step 5: Analyze Results and Follow-Up

**Context**: Identify hits and access leaked data.

Sort results by response length. For valid TbPin, forward request to Repeater to view details or modify for cancellation (a=c).

> No command; GUI. Expected: PII exposure (names, phones, emails); cancellation possible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Brute Force]] Brute Force
- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- idor
- brute-force
- web
- burp-suite
