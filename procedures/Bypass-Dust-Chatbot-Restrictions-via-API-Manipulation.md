---
tags:
  - auth-bypass
  - api-manipulation
  - chatbot
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:27.209Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 363b8e44-fce0-4682-b603-8461557028b8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# Bypass-Dust-Chatbot-Restrictions-via-API-Manipulation

## Summary

This procedure exploits an authorization bypass vulnerability in the Dust chatbot system, allowing non-admin member users to access disabled or restricted AI agents like Gemini by intercepting and modifying HTTP API requests to inject unauthorized agent mentions and configuration IDs.

## Description

In the Dust platform, admins can disable or restrict access to certain AI chatbots, such as Google's Gemini agent, via the admin dashboard. However, the server-side API lacks proper validation of user permissions for agent configuration IDs in message edit requests. An attacker with a member account can use a proxy like Burp Suite to capture a legitimate chat initiation request, modify the JSON payload to reference the restricted 'gemini-pro' agent, and forward it to receive responses from the unauthorized agent. This bypasses admin controls, enabling unauthorized use of premium features and potential abuse. The vulnerability is present in endpoints like POST /api/w/{workspace}/assistant/conversations/{conversation}/messages/{message}/edit, where the 'mentions' array and content fields are manipulated.

## Requirements

1. Valid admin account to verify and set agent restrictions
2. Valid member (non-admin) account for exploitation
3. Burp Suite or similar HTTP proxy tool configured to intercept browser traffic
4. Access to the Dust web application over the network
5. Basic knowledge of JSON payload editing and HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement server-side authorization checks for all agent configuration IDs in API requests, validating user permissions against admin settings
- Use input sanitization and whitelist allowed agents per user role in the 'mentions' and 'configurationId' fields
- Monitor API logs for anomalous requests to conversation/message edit endpoints, flagging injections of disabled agent IDs
- Enforce Content Security Policy (CSP) and rate limiting on chat APIs to hinder proxy-based manipulations

## Objectives

1. Gain unauthorized access to restricted AI chatbots like Gemini
2. Interact with disabled premium features without admin privileges
3. Demonstrate violation of access control policies in the Dust system

## Instructions

### Step 1: Verify Agent Restrictions as Admin

**Context**: Log in as admin to confirm the Gemini agent is disabled, setting up the restricted environment.

Access the admin dashboard and navigate to 'Manage Agents' to check the status of 'gemini-pro'.

> Ensure the agent is marked as disabled or restricted for member users.

### Step 2: Initiate Chat as Member

**Context**: Switch to member account to start a legitimate chat, preparing for interception.

Log in with member credentials, create a new conversation, and select an available agent via the UI.

> This generates a capturable API request without triggering the restricted agent.

### Step 3: Intercept Request with Burp Suite

**Context**: Capture the POST request during chat message submission or edit.

Configure Burp Suite as a proxy, then perform the chat action to intercept the request to the /api/.../edit endpoint.

> The request body will contain JSON with 'content' and 'mentions' fields for a permitted agent.

### Step 4: Edit Payload to Inject Unauthorized Agent

**Context**: Modify the JSON to reference the restricted Gemini agent, bypassing checks.

In Burp Suite Repeater or Proxy, alter the body:
- Set 'content' to ':mention[gemini-pro]{sId=gemini-pro} how are you?'
- Update 'mentions' array to [{'type':'agent','configurationId':'gemini-pro'}]

> Example modified JSON payload:
```json
{
  "content": ":mention[gemini-pro]{sId=gemini-pro} how are you?",
  "mentions": [{"type":"agent","configurationId":"gemini-pro"}]
}
```

### Step 5: Forward Request and Verify Access

**Context**: Send the tampered request to confirm the bypass and interact with the agent.

Forward the request in Burp Suite and check the response for Gemini's output.

> Successful bypass shows a response from the restricted agent, allowing further messaging.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- auth-bypass
- api-manipulation
- chatbot
- gemini
- dust
