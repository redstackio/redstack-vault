---
tags:
  - initial-access
  - web-app
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
updated_at: '2025-12-14T17:26:12.081Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 4683b215-db6d-4eac-9d45-e7327973008f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Instacart-Store-List

## Summary

This procedure outlines the steps to create a new shopping list associated with a specific store in the Instacart web application, setting the stage for testing image upload features.

## Description

In the context of vulnerability assessment, creating a store list provides access to customization options, including background image uploads. This is a prerequisite for triggering the image manipulation process in Instacart's Ruby on Rails backend. The procedure assumes a standard user account and targets the web interface, with no special privileges required. Expected outcome is a functional list ready for further interaction.

## Requirements

1. Valid Instacart user account with login credentials
2. Web browser with JavaScript enabled for the Instacart app
3. Internet access to app.instacart.com

## Defense

Defensive measures and detection strategies:

- Rate limiting on list creation to prevent abuse
- CAPTCHA on frequent account actions
- Logging of user sessions for anomalous list creation patterns

## Objectives

1. Gain access to list customization interface
2. Associate list with a store for targeted feature testing
3. Prepare environment for upload vulnerability exploitation

## Instructions

### Step 1: Log In to Instacart

**Context**: Authenticate to access personal features like lists.

Navigate to app.instacart.com and enter credentials to log in.

> Successful login redirects to the dashboard.

### Step 2: Navigate to Lists

**Context**: Access the lists management section.

Click on the 'Lists' tab in the navigation menu.

> Displays existing lists or option to create new.

### Step 3: Create New List

**Context**: Initiate list creation and link to a store.

Select 'Create List', enter a name, choose a store from the dropdown, and save.

> List is created and editable, with customization options available.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web]]
- [[initial-access]]
