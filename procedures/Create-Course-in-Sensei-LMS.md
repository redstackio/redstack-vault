---
tags:
  - wordpress
  - lms
  - setup
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
updated_at: '2025-12-14T17:32:29.195Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: c219d31d-e532-4fb0-8fd6-b6d7def19ed3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Course-in-Sensei-LMS

## Summary

This procedure sets up a new course in the Sensei LMS WordPress plugin, enabling the private contact teacher feature that generates vulnerable sensei-message objects.

## Description

In the context of exploiting the Sensei LMS vulnerability, creating a course is a prerequisite to activate messaging functionality. This step uses the WordPress admin interface to configure a course, which exposes the REST API endpoint for messages. The target environment is a WordPress site running Sensei LMS <= 4.4.3. Expected outcome: A functional course with private messaging enabled, leading to message ID generation.

## Requirements

1. Access to WordPress admin dashboard (admin credentials)
2. Active Sensei LMS plugin installed
3. Basic familiarity with WordPress course creation

## Defense

Defensive measures and detection strategies:

- Restrict admin access with strong authentication and role-based controls
- Monitor plugin installations and updates via WordPress audit logs
- Use web application firewalls (WAF) to detect unusual admin activity

## Objectives

1. Establish the vulnerable messaging environment
2. Generate prerequisites for message creation
3. Prepare for subsequent exploitation steps

## Instructions

### Step 1: Access WordPress Admin

**Context**: Log in to the WordPress backend to initiate course creation.

Navigate to the admin dashboard at /wp-admin and go to Sensei > Courses > Add New.

### Step 2: Configure and Publish Course

**Context**: Set up course details to enable contact features.

Enter course title, description, and enable lessons. Publish the course to make the contact teacher form available on the frontend.

**Expected Output**: Course appears in the frontend LMS interface with a contact option.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[wordpress]]
- [[lms]]
- [[setup]]
