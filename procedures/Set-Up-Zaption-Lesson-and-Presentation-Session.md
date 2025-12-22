---
id: proc-zaption-setup-session
tags:
  - setup
  - web
  - presentation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:16:14.323Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Set-Up-Zaption-Lesson-and-Presentation-Session

## Summary

This procedure outlines the creation and initiation of a Zaption lesson and presentation session to simulate a multi-user environment, enabling testing of interactive features like 'Quick question' from both presenter and viewer perspectives.

## Description

Zaption is an online platform for creating interactive lessons and presentations. To exploit vulnerabilities in its presentation mode, an attacker first needs to establish a legitimate session. This involves logging in with valid credentials, building a simple lesson, publishing it, and starting a presentation. A second browser window simulates a viewer joining the session, mimicking a real-time classroom or webinar scenario. This setup is crucial for observing how injected content propagates to multiple users.

## Requirements

1. Valid Zaption account credentials with lesson creation permissions
2. Modern web browser (e.g., Chrome) for multi-instance testing
3. Stable internet connection to Zaption's web application

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls to limit lesson creation to verified users
- Monitor for unusual multi-browser sessions or rapid lesson publications
- Use client-side CSP headers to restrict script execution in presentation iframes

## Objectives

1. Establish a functional presentation environment for vulnerability testing
2. Simulate multi-user interaction to assess cross-context impacts
3. Prepare for payload injection without triggering account restrictions

## Instructions

### Step 1: Log In and Create a Lesson

**Context**: Access the Zaption dashboard and build a basic lesson to serve as the foundation for the presentation.

Navigate to the Zaption login page and sign in with your credentials. Once logged in, select 'Create New Lesson' and add minimal content, such as a slide or video, to make it publishable.

### Step 2: Publish the Lesson and Start Presentation

**Context**: Make the lesson available and initiate the live presentation mode.

Click 'Publish' on the lesson, then select 'Present' to start the session. Note the join link or code for viewers.

### Step 3: Simulate Viewer Role

**Context**: Join the presentation in a separate browser to observe participant-side rendering.

Open an incognito window or second browser instance, navigate to Zaption, and join the presentation using the viewer link.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[web]]
- [[presentation]]
