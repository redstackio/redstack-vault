---
tags:
  - idor
  - graphql
  - interception
  - deletion
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Data Manipulation]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Stored Data Manipulation]]'
id: fa946f68-2416-4651-8355-349e19a185fd
created_at: '2025-12-11T03:47:56.649Z'
updated_at: '2025-12-11T03:47:56.649Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0040]]'
mitre_techniques:
  - '[[T1565]]'
---
# Intercept and Modify GraphQL Delete Request

## Summary

This procedure exploits an Insecure Direct Object Reference (IDOR) vulnerability in Snapchat's Spotlight feature by intercepting and modifying a GraphQL delete request to remove any user's content without authorization.

## Description

The attack involves logging into Snapchat, using Burp Suite to capture a legitimate delete request for the attacker's own post, and then altering the 'ids' parameter to target a victim's Spotlight ID. This lacks proper ownership checks, allowing unauthorized deletions that can impact content visibility and payments. The procedure targets web-based GraphQL APIs and requires an authenticated session.

## Requirements

1. Valid Snapchat account credentials
2. Burp Suite installed and configured as a proxy
3. Target's Spotlight ID from public share URLs
4. Network access to Snapchat's API endpoints

## Defense

Defensive measures and detection strategies:

- Implement proper authorization checks for object references in API requests
- Monitor for anomalous delete requests in GraphQL logs, such as IDs not matching the user's owned content
- Use rate limiting and anomaly detection on mutation requests

## Objectives

1. Delete unauthorized Spotlight content
2. Demonstrate IDOR vulnerability
3. Assess impact on content availability and payments

## Instructions

### Step 1: Navigate to Posts and Log In

**Context**: Access the personal posts page to view and select content for deletion.

Access https://my.snapchat.com/myposts and log in with valid credentials.

> This sets up the authenticated session needed for request generation.

### Step 2: Enable Burp Suite Interception

**Context**: Configure Burp Suite to intercept outgoing requests.

Turn on the intercept feature in Burp Suite's Proxy tab.

> Ensure your browser is configured to use Burp as the proxy.

### Step 3: Initiate Deletion on Own Post

**Context**: Trigger the delete action to generate the request.

Select one of your own posts and click the delete option.

> This sends the GraphQL mutation request which will be captured.

### Step 4: Capture the Request

**Context**: Intercept the specific GraphQL request.

In Burp Suite, capture the DeleteStorySnaps mutation request.

> Look for the POST request containing the 'ids' parameter.

### Step 5: Modify the 'ids' Parameter

**Context**: Alter the request to target the victim.

Replace the 'ids' array with the victim's Spotlight ID (e.g., from https://story.snapchat.com/spotlight/█████).

> Ensure the payload remains valid JSON for GraphQL.

### Step 6: Forward the Request

**Context**: Send the modified request to execute the deletion.

Forward the altered request in Burp Suite.

> Verify the response indicates successful deletion.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Data Manipulation]]

### Sub-Techniques

- [[Stored Data Manipulation]]

## Commands Used



## Tools Used

- [[tools/Burp-Suite]]

## Tags

- #idor
- #graphql
