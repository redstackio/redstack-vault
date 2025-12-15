---
id: proc-uuid-001
name: Monitor Websocket Traffic for Sensitive Data
tags:
  - information-disclosure
  - websocket
  - reconnaissance
  - discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Sniffing]]'
updated_at: '2025-12-14T17:24:56.015Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Sniffing]]'
---
# Monitor Websocket Traffic for Sensitive Data

## Summary

This procedure involves using browser developer tools to intercept and analyze websocket communications in a web application, identifying potential information disclosure of user account details such as IDs and names in JSON payloads. It is useful for reconnaissance in web security testing to uncover client-side data exposures.

## Description

In web applications leveraging websockets for real-time updates, sensitive data like user IDs and names may be inadvertently sent to the client without proper sanitization or encryption. By monitoring network traffic during normal usage, testers can observe these payloads and assess if the disclosure poses a risk, such as enabling unauthorized enumeration of user details if intercepted by malicious actors. This technique was applied to discover such exposure in an e-commerce platform, where user information appeared in websocket messages related to cart operations. Prerequisites include a valid user session and access to a browser with network inspection capabilities. Expected outcomes include captured JSON structures revealing account data, though the impact may be mitigated if the data is intended for client rendering.

## Requirements

1. Valid credentials to authenticate into the target web application
2. Modern web browser (e.g., Chrome, Firefox) with developer tools enabled
3. Active internet connection to the application
4. Basic understanding of JSON and network protocols

## Defense

Defensive measures and detection strategies:

- Implement payload sanitization in websocket servers to exclude unnecessary sensitive fields like user IDs
- Use WebSocket Secure (WSS) to encrypt traffic and prevent interception
- Monitor for anomalous network inspection tools or traffic patterns indicative of sniffing
- Apply client-side data access controls to limit what is rendered or logged

## Objectives

1. Capture websocket messages during application interactions
2. Parse JSON payloads for user account information
3. Evaluate the exposure risk and report findings

## Instructions

### Step 1: Set Up Monitoring

**Context**: Prepare the browser environment to capture websocket traffic without external tools.

Open the target web application in your browser and authenticate with valid credentials. Ensure you are on a page that uses websockets, such as a real-time dashboard or shopping cart.

1. Press F12 (or right-click and select Inspect) to open Developer Tools.
2. Navigate to the Network tab.
3. In the filter bar, select "WS" to show only websocket connections.
4. Clear any existing logs by clicking the clear button.

**Expected Output**: A list of websocket connections appears as you interact with the app.

### Step 2: Trigger and Capture Traffic

**Context**: Generate websocket messages by performing normal user actions to reveal payloads.

Interact with the application features that likely use websockets, such as updating a cart, refreshing a page, or viewing user-related data.

1. Perform actions like adding items to a cart or navigating user profiles.
2. Observe new frames or messages appearing in the Network tab under the websocket connection.
3. Click on a message frame to view its details, including the JSON payload in the "Message" or "Response" section.

**Expected Output**: Raw JSON data in payloads, e.g., {"t":"d","d":{"r":8,"a":"p","b":{"p":"/carts/3671079_xjdJHqx88J435eDW5zxN/users/-KRbGN8R6uIjy6_OPx_j","d":{"id":25390626,"name":"Username"}}}}.

### Step 3: Analyze for Disclosure

**Context**: Inspect the captured data for sensitive information and assess exposure.

Review the JSON structure for fields like "id" and "name" under user-related paths.

1. Copy the JSON payload and parse it manually or using a JSON viewer.
2. Note any user account details (e.g., ID: 25390626, name: "Username").
3. Document the location (e.g., 'd' field in websocket message) and potential impact.

**Expected Output**: Identification of disclosed user information without server restrictions.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Network Sniffing]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- information-disclosure
- websocket
- reconnaissance
- discovery
