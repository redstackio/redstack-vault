---
tags:
  - information-disclosure
  - api
  - privacy
  - web
  - traffic-interception
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[T1213.003]]'
  - '[[Network Sniffing]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 08e8eaa3-627d-4130-ac74-5ed4e7161a5f
created_at: '2025-12-14T17:32:39.625Z'
updated_at: '2025-12-14T17:32:39.625Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1213.003]]'
  - '[[Network Sniffing]]'
---
# Intercept-and-Analyze-Bumble-Chat-API-for-Read-Status-Exposure

## Summary

This procedure details how to use an intercepting proxy to capture and analyze HTTP traffic from Bumble's webapp, revealing an information disclosure in the SERVER_OPEN_CHAT API endpoint. The response includes a 'read' boolean for chat messages, exposing read status that the app's UI hides to protect privacy.

## Description

In the context of testing Bumble's web application, this procedure simulates normal user interaction while monitoring backend API calls. By proxying traffic, you can inspect the JSON responses from https://am1.bumble.com/mwebapi.phtml?SERVER_OPEN_CHAT, which returns an array of chat_messages. Each message object (badoo.bma.ChatMessage) contains a 'read' field indicating if the recipient has viewed it. This disclosure allows viewing read status across all chats, breaching privacy as users expect only 'delivered' status. Prerequisites include a valid Bumble account and proxy setup; outcomes confirm the vulnerability without requiring code changes.

## Requirements

1. Valid Bumble login credentials for authenticated access.
2. Installed and configured intercepting proxy tool like Burp Suite.
3. Browser configured to route traffic through the proxy (e.g., FoxyProxy extension).
4. HTTPS interception enabled with CA certificate installation.

## Defense

Defensive measures and detection strategies:

- Filter sensitive fields like 'read' status from API responses before transmission.
- Implement rate limiting on chat API endpoints to detect anomalous traffic patterns.
- Monitor proxy-like tool usage in network logs for unauthorized interception attempts.
- Use UI-only indicators for privacy-sensitive data, ensuring backend does not expose it.

## Objectives

1. Capture and inspect chat API responses to identify unintended data exposure.
2. Verify the presence of 'read' status in JSON, confirming privacy violation.
3. Document the endpoint and response structure for vulnerability reporting.

## Instructions

### Step 1: Authenticate and Configure Proxy

**Context**: Establish a session and prepare for traffic monitoring to ensure all API calls are captured.

Launch Burp Suite and set the proxy listener on localhost:8080. Configure your browser to use this proxy and install the Burp CA certificate for HTTPS decryption.

> Navigate to https://bumble.com, log in with credentials, and confirm traffic appears in Burp's Proxy > HTTP history tab.

### Step 2: Initiate Chat Interaction

**Context**: Trigger the vulnerable API call by loading a chat, generating the POST request for analysis.

In the Bumble webapp, go to the chats section and open an existing conversation.

> Observe in Burp that a POST request to https://am1.bumble.com/mwebapi.phtml?SERVER_OPEN_CHAT is sent with chat ID parameters.

### Step 3: Isolate and Inspect the Request

**Context**: Focus on the specific endpoint to examine its behavior without noise from other traffic.

Filter Burp's history for POST requests containing "SERVER_OPEN_CHAT". Right-click the request and select "Send to Repeater" for closer inspection if needed.

> The request body typically includes JSON with chat identifiers; forward it to view the raw response.

### Step 4: Analyze Response for Disclosure

**Context**: Parse the JSON to locate and validate the exposed 'read' field, confirming the information disclosure.

In Burp's Inspector or Raw view, examine the response JSON. Look for the "chat_messages" array and drill into each message object.

> Expected JSON snippet: {"chat_messages": [{"id": "msg123", "text": "Hello", "read": true}, ...]} – The 'read' boolean is present and unfiltered.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]
- [[Discovery]]

### Techniques

- [[T1213.003]]
- [[Network Sniffing]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[information-disclosure]]
- [[api]]
- [[privacy]]
- [[web]]
- [[traffic-interception]]
