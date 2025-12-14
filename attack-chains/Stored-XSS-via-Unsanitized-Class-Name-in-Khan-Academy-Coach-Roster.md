---
id: ac-khan-xss-roster-001
tags:
  - xss
  - stored-xss
  - web
  - javascript-injection
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Stored-XSS-in-Class-Name-Field]]'
step_count: 4
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:53.281Z'
description: >-
  A multi-step attack exploiting a stored XSS vulnerability in the Khan Academy
  coach roster feature by injecting malicious JavaScript into the class name
  field, leading to persistent script execution for any user viewing the roster.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored XSS via Unsanitized Class Name in Khan Academy Coach Roster

Multi-stage attack chain demonstrating a complete workflow for exploiting a stored cross-site scripting (XSS) vulnerability in the Khan Academy coach roster feature. An attacker injects a malicious JavaScript payload into the class name input, which is stored and rendered unsanitized, executing arbitrary code in the browsers of coaches or users viewing the roster. This can lead to session hijacking, data theft, or further attacks on authenticated users.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~2 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Navigate to Roster] --> B[Initiate Class Addition]
    B --> C[Inject Malicious Payload]
    C --> D[Verify Execution and Persistence]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Khan Academy web application
- Authenticated access as a coach
- No specific services/ports required beyond standard HTTPS (443)

### Initial Access Requirements

- Valid Khan Academy coach account credentials
- Direct network access to https://www.khanacademy.org
- No prior access needed beyond authentication

## Detailed Attack Procedures

### Step 1: Navigate to Coach Roster Page
procedure: [[procedures/Exploit-Stored-XSS-in-Class-Name-Field]]

**Objective**: Access the vulnerable coach roster interface to begin the exploitation process.

**Instructions**: Open a web browser and log in to Khan Academy with coach credentials. Navigate to the coach roster URL.

**Expected Output**: The roster page loads, displaying the list of students or classes.

**Success Indicators**:
- Roster page accessible at https://www.khanacademy.org/coach/roster/?listId=allStudents
- UI elements like 'add class' button visible

### Step 2: Initiate Class Addition
procedure: [[procedures/Exploit-Stored-XSS-in-Class-Name-Field]]

**Objective**: Trigger the class creation form to expose the vulnerable input field.

**Instructions**: On the roster page, locate and click the 'add class' button to open the input form for a new class name.

**Expected Output**: A form or dialog appears with a text input field for the class name.

**Success Indicators**:
- 'Add class' button interaction successful
- Class name input field is editable

### Step 3: Inject Malicious Payload
procedure: [[procedures/Exploit-Stored-XSS-in-Class-Name-Field]]

**Objective**: Submit a JavaScript payload in the class name field to store and persist the XSS.

**Instructions**: In the class name input field, enter the payload `'><img src=x onerror=alert(4)>` and submit the form.

**Expected Output**: The class is added, and the payload is stored in the backend without sanitization.

**Success Indicators**:
- Form submission succeeds without errors
- New class appears in the roster list

### Step 4: Verify Persistence and Execution
procedure: [[procedures/Exploit-Stored-XSS-in-Class-Name-Field]]

**Objective**: Confirm the payload executes JavaScript in the victim's browser context when viewing the roster.

**Instructions**: Refresh or revisit the roster page. The injected class name should render the payload, triggering an alert dialog with '4'.

**Expected Output**: An alert box pops up displaying '4' upon page load or roster view.

**Success Indicators**:
- JavaScript alert executes automatically
- Payload persists across sessions or for other users viewing the roster

## Attack Chain Summary

### Key Achievements

1. Successful injection of unsanitized HTML/JavaScript into the class name field
2. Persistent storage and rendering of the payload on the roster page
3. Arbitrary JavaScript execution in the context of authenticated users, enabling potential session hijacking or data exfiltration

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
