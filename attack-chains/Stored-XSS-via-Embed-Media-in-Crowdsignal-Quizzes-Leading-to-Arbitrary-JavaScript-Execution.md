---
id: ac-stored-xss-crowdsignal-embed-media
tags:
  - xss
  - stored-xss
  - javascript
  - crowdsignal
  - wordpress
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Stored-XSS-in-Crowdsignal-Embed-Media]]'
step_count: 13
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:37.756Z'
description: >-
  A multi-step attack exploiting a stored XSS vulnerability in the Embed Media
  feature of Crowdsignal quizzes, allowing injection of malicious JavaScript
  payloads that execute when users view the quiz on app.crowdsignal.com and
  survey.fm subdomains.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Stored XSS via Embed Media in Crowdsignal Quizzes Leading to Arbitrary JavaScript Execution

Multi-stage attack chain demonstrating exploitation of a stored XSS vulnerability in the Crowdsignal platform's quiz creation feature, specifically the Embed Media option, to inject and persist malicious JavaScript that executes in the context of app.crowdsignal.com and shared survey.fm subdomains.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 13 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Create Quiz] --> B[Payload Injection: Modify Embed Media]
    B --> C[Persistence: Save and Trigger XSS]
    C --> D[Impact: JavaScript Execution on Viewers]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform: app.crowdsignal.com (Crowdsignal quizzes)
- Required services/ports: HTTPS (443)
- Network access requirements: Internet access to the target domain; authenticated session to the dashboard

### Initial Access Requirements

- Valid user account on Crowdsignal (no special privileges needed)
- Burp Suite configured as a proxy for request interception
- No prior access beyond standard user login

## Detailed Attack Procedures

### Step 1: Navigate to the Dashboard
procedure: [[procedures/Exploit-Stored-XSS-in-Crowdsignal-Embed-Media]]

**Objective**: Gain initial access to the quiz creation interface.

**Instructions**: Open a web browser and log in to your Crowdsignal account. Access the dashboard to begin the quiz creation process.

**Technical Details**: Visit `https://app.crowdsignal.com/dashboard`.

**Expected Output**: Dashboard loads, showing options to create new quizzes.

**Success Indicators**:
- Successful login and dashboard access
- Quiz creation option visible

### Step 2: Create a New Quiz
procedure: [[procedures/Exploit-Stored-XSS-in-Crowdsignal-Embed-Media]]

**Objective**: Initiate the quiz setup to reach the question editor.

**Instructions**: Click on the "Create Quiz" button or equivalent to start building a new quiz.

**Technical Details**: This triggers the quiz creation workflow on the platform.

**Expected Output**: Quiz editor interface appears.

**Success Indicators**:
- New quiz initiated
- Editor ready for question addition

### Step 3: Go to the Quiz Question Editor
procedure: [[procedures/Exploit-Stored-XSS-in-Crowdsignal-Embed-Media]]

**Objective**: Access the specific page where questions and media can be added.

**Instructions**: Navigate to the question editing section for the newly created quiz.

**Technical Details**: URL: `https://app.crowdsignal.com/quizzes/{your-quiz-id}/question`.

**Expected Output**: Question editor loads.

**Success Indicators**:
- Question editor page accessible
- Options to add question types visible

### Step 4: Add a Multiple Choice Question
procedure: [[procedures/Exploit-Stored-XSS-in-Crowdsignal-Embed-Media]]

**Objective**: Set up a question type that supports media embedding.

**Instructions**: Select "Multiple Choice" as the question type and add it to the quiz.

**Technical Details**: Choose Multiple Choice from the available question types.

**Expected Output**: Multiple choice question added to the quiz.

**Success Indicators**:
- Question type selected and added
- Answer fields available

### Step 5: Name the First Answer
procedure: [[procedures/Exploit-Stored-XSS-in-Crowdsignal-Embed-Media]]

**Objective**: Prepare the answer field for media injection.

**Instructions**: Enter a name or label for the first answer option.

**Technical Details**: Fill in the text field for answer 1.

**Expected Output**: Answer named and ready for further configuration.

**Success Indicators**:
- Answer text entered
- Media addition option available

### Step 6: Click Add Media Button
procedure: [[procedures/Exploit-Stored-XSS-in-Crowdsignal-Embed-Media]]

**Objective**: Initiate the media embedding process to reach the vulnerable input.

**Instructions**: Click the "Add Media" button associated with the answer.

**Technical Details**: This opens the media selection interface.

**Expected Output**: Media addition dialog appears.

**Success Indicators**:
- Media button clicked
- Embed options displayed

### Step 7: Select Embed Media
procedure: [[procedures/Exploit-Stored-XSS-in-Crowdsignal-Embed-Media]]

**Objective**: Choose the embed option to access the shortcode input field.

**Instructions**: From the media options, select "Embed Media".

**Technical Details**: This allows pasting custom embed shortcodes.

**Expected Output**: Embed field input box visible.

**Success Indicators**:
- Embed Media selected
- Input field for shortcode ready

### Step 8: Paste Initial Shortcode
procedure: [[procedures/Exploit-Stored-XSS-in-Crowdsignal-Embed-Media]]

**Objective**: Provide a benign initial payload to set up for interception.

**Instructions**: Paste a valid WordPress video shortcode into the embed field, such as `[wpvideo w0MiG12E]`.

**Technical Details**: Use a legitimate shortcode to avoid immediate errors.

**Expected Output**: Shortcode entered in the field.

**Success Indicators**:
- Shortcode pasted
- No validation errors yet

### Step 9: Insert the Media
procedure: [[procedures/Exploit-Stored-XSS-in-Crowdsignal-Embed-Media]]

**Objective**: Commit the initial media to prepare for saving.

**Instructions**: Click the insert or add button to embed the media into the answer.

**Technical Details**: This associates the shortcode with the answer.

**Expected Output**: Media preview or confirmation in the answer.

**Success Indicators**:
- Media inserted
- Answer updated with embed

### Step 10: Open Burp Suite and Click Save
procedure: [[procedures/Exploit-Stored-XSS-in-Crowdsignal-Embed-Media]]

**Objective**: Intercept the save request for modification.

**Instructions**: Ensure Burp Suite is proxying your browser traffic, then click the Save button on the quiz.

**Technical Details**: Configure Burp to intercept POST requests to the quiz save endpoint.

**Expected Output**: Request intercepted in Burp Suite.

**Success Indicators**:
- Save button clicked
- Request captured in Burp

### Step 11: Modify the Media Parameter in Burp Suite
procedure: [[procedures/Exploit-Stored-XSS-in-Crowdsignal-Embed-Media]]

**Objective**: Inject the XSS payload into the request.

**Instructions**: In the intercepted request, locate the media parameter (e.g., `media[23168664]`) and modify it to include the payload: `[wpvideo%20w0MiG12Exx1"><svg/onload=prompt(document.domain)>]`.

**Technical Details**: URL-decode and encode as needed; the payload closes the shortcode and injects an SVG with onload JavaScript.

**Expected Output**: Modified request ready to forward.

**Success Indicators**:
- Parameter updated with payload
- No syntax errors in request

### Step 12: Forward the Modified Request and Refresh the Page
procedure: [[procedures/Exploit-Stored-XSS-in-Crowdsignal-Embed-Media]]

**Objective**: Persist the payload and trigger initial execution.

**Instructions**: Forward the request in Burp Suite, then refresh the quiz editor page to observe the XSS alert.

**Technical Details**: The stored payload executes on page load due to insufficient sanitization.

**Expected Output**: Alert box with `app.crowdsignal.com` domain prompted.

**Success Indicators**:
- Request forwarded successfully
- XSS alert triggers on refresh

### Step 13: Check the Shared Survey Link
procedure: [[procedures/Exploit-Stored-XSS-in-Crowdsignal-Embed-Media]]

**Objective**: Verify persistence and execution on shared views.

**Instructions**: Go to the sharing page at `https://app.crowdsignal.com/sharing/quiz/{your-quiz-id}/`, copy the survey.fm link, and visit it in a new browser or incognito window.

**Technical Details**: The XSS executes for any viewer of the quiz on survey.fm subdomains.

**Expected Output**: XSS alert triggers on the shared page.

**Success Indicators**:
- Shared link accessed
- JavaScript payload executes, showing alert

## Attack Chain Summary

### Key Achievements

1. Successful injection and storage of XSS payload in quiz media embed
2. Arbitrary JavaScript execution on app.crowdsignal.com and survey.fm domains
3. Potential for cookie theft or other client-side attacks, though limited by lack of sensitive cookies

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
