---
tags:
  - comment-submission
  - expressionengine
  - web-exploit
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: f9093ae3-784e-4439-b028-59152a6b9594
created_at: '2025-12-14T17:24:26.610Z'
updated_at: '2025-12-14T17:24:26.610Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-ExpressionEngine-Comment

## Summary

This procedure involves submitting a comment through the ExpressionEngine CMS comment form to trigger the post-submission redirect process, setting the stage for redirect manipulation.

## Description

In ExpressionEngine, the comment submission feature allows anonymous or authenticated users to post comments on entries like blog posts. Upon successful submission, the system redirects the user back to the entry page or a specified return URL. This procedure focuses on the initial submission step, which is straightforward and requires no special privileges. It is typically used in web vulnerability testing to probe redirect behaviors in CMS platforms. Expected outcomes include successful comment posting and initiation of the redirect flow, with no direct compromise but potential for chaining with redirect exploits.

## Requirements

1. Public access to an ExpressionEngine site with enabled comments
2. A web browser for form interaction
3. Valid comment form inputs (name, email, comment text)

## Defense

Defensive measures and detection strategies:

- Enable CAPTCHA or moderation on comment forms to deter automated submissions
- Log all comment submissions and redirects for anomaly detection (e.g., unusual return URLs)
- Implement rate limiting on comment endpoints to prevent abuse

## Objectives

1. Trigger the comment processing and redirect logic
2. Confirm successful interaction with the vulnerable endpoint
3. Prepare for redirect parameter manipulation

## Instructions

### Step 1: Locate and Access Comment Form

**Context**: Identify a page with an active comment section to begin the submission process.

Navigate to a blog post or entry on the target ExpressionEngine site that has comments enabled. Inspect the page source to confirm the comment form is present (look for form action pointing to a comment submission endpoint like /system/actee).

### Step 2: Fill and Submit Comment

**Context**: Provide minimal valid input to process the comment and invoke the redirect.

Enter arbitrary but valid data into the form fields:
- Name: Test User
- Email: test@example.com
- Comment: Test comment for vulnerability testing

Click the submit button to post the comment. Monitor the network tab in browser developer tools for the POST request to the comment endpoint.

> Upon submission, the server validates and stores the comment, then issues a redirect header (e.g., Location: /entry-url).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[comment-submission]]
- [[expressionengine]]
