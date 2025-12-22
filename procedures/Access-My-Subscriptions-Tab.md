---
id: proc-uuid-2
tags:
  - recon
  - web
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
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:23.620Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Access-My-Subscriptions-Tab

## Summary

This procedure involves navigating to the 'My Subscriptions' tab in the Zomato user profile to trigger the initial API request, revealing the structure of the vulnerable endpoint for IDOR exploitation.

## Description

As part of the IDOR attack on Zomato's treat subscriptions, this step performs reconnaissance by accessing legitimate user functionality. It triggers a POST request to /php/filter_user_tab_content.php with the authenticated user's own user_id, allowing inspection of request parameters and response format. The target is the Zomato web app; prerequisites include an active session. Expected outcomes: understanding of API behavior and confirmation of endpoint accessibility.

## Requirements

1. Active authenticated session from prior login
2. Access to Zomato user profile section
3. Browser developer tools for network inspection

## Defense

Defensive measures and detection strategies:

- Log and monitor API calls to profile endpoints for anomalies
- Implement client-side checks to prevent easy request inspection
- Use rate limiting on tab loads to detect scripted access

## Objectives

1. Trigger and observe the legitimate API request
2. Identify key parameters (e.g., user_id, tab) for modification
3. Confirm response contains subscription data structure

## Instructions

### Step 1: Navigate to Profile

**Context**: Reach the user profile area where subscriptions are managed.

From the Zomato dashboard, click on the profile icon and select the profile section.

**Expected Output**: User profile page loads.

### Step 2: Select Subscriptions Tab

**Context**: Initiate the API call by accessing the treat subscriptions view.

Click on the 'My Subscriptions' tab, specifically the treat subscriptions subsection.

**Expected Output**: UI displays personal subscriptions; Network tab shows POST request to /php/filter_user_tab_content.php with parameters like user_id=own_id, tab=treat_subscription.

Inspect the request in developer tools to note headers and body.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- reconnaissance
- api-discovery
