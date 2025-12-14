---
id: proc-slack-team-creation-4561
tags:
  - slack
  - onboarding
  - profile-completion
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:31.239Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Slack-Team-to-Trigger-Profile-Completion

## Summary

This procedure initiates the Slack team creation process to activate Slackbot's automated profile completion workflow, setting the stage for injecting malicious inputs during onboarding.

## Description

During new team creation in Slack, the platform prompts users via Slackbot direct messages to complete profile details like first name, last name, and Skype account. This step leverages the standard onboarding flow to receive these prompts without raising suspicion, as it mimics legitimate user setup. The target environment is the Slack web application, and success enables subsequent payload injection. Expected outcomes include receiving editable DM prompts that store user responses unsafely.

## Requirements

1. Active Slack account with permissions to create workspaces
2. Web browser access to slack.com
3. Internet connectivity

## Defense

Defensive measures and detection strategies:

- Monitor for unusual team creation patterns or rapid workspace deletions
- Implement rate limiting on new team onboarding flows
- Log Slackbot interactions for anomalous input patterns

## Objectives

1. Trigger Slackbot's profile completion DMs
2. Establish a context for storing user inputs in team messages
3. Prepare for XSS payload delivery without authentication barriers

## Instructions

### Step 1: Log In and Initiate Team Creation

**Context**: Access Slack and start the process to create a new workspace, which activates the onboarding bot.

No specific command; perform via UI:

- Navigate to slack.com and sign in.
- Click 'Create a workspace' or equivalent.
- Follow prompts to set up basic team details (name, purpose).

> This redirects to the new team's interface where Slackbot begins messaging.

### Step 2: Observe Profile Completion Prompts

**Context**: Wait for Slackbot to send DMs requesting profile information, confirming the trigger.

No command; monitor the sidebar for new direct messages from Slackbot.

> Successful output: DMs appear with questions like "What's your first name?" and fields for input.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[slack]]
- [[onboarding]]
