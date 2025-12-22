---
id: 4e0ea9d3-d7ea-4aa3-ba89-eb3f8d053cbe
name: File-Upload-Double-Extension-Bypass
type: procedure
verified: true
submitted: true
created_at: '2020-08-01T14:21:20.705964+00:00'
updated_at: '2023-05-26T01:09:04.157332+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
sub_techniques: []
tags:
  - File Uploads
  - Web Applications
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# File-Upload-Double-Extension-Bypass

## Summary

This procedure demonstrates how to bypass client-side file upload restrictions in web applications by appending an allowed file extension to a malicious file (e.g., a PHP webshell) and then stripping the extra extension during the upload request using a proxy tool like Burp Suite. This technique exploits weak validation on the client side, allowing the upload of potentially dangerous files that can lead to remote code execution on the server.

## Description

Many web applications implement file upload functionality with client-side checks to restrict file types based on extensions (e.g., allowing only .jpg images). However, these checks can be bypassed by renaming the malicious file to include a double extension, such as Malicious.php.jpg, which passes the initial validation. By intercepting the HTTP POST request containing the upload using a tool like Burp Suite, the attacker can modify the filename in the request to remove the benign extension (.jpg), resulting in the server receiving and storing the file as Malicious.php. This uploaded file can then be accessed and executed if the server interprets it as a script, enabling further exploitation like command execution or backdoor installation. The technique is effective against applications with insufficient server-side validation and is commonly used in penetration testing to assess upload vulnerabilities.

## Requirements

1. Access to a web application with file upload functionality that enforces client-side extension checks (e.g., JavaScript validation).
2. A prepared malicious file, such as a simple PHP webshell (e.g., <?php system($_GET['cmd']); ?> saved as Malicious.php).
3. Burp Suite or similar HTTP proxy tool configured to intercept browser traffic.
4. Browser with proxy settings configured to route through Burp Suite (e.g., Firefox with manual proxy at 127.0.0.1:8080).
5. Knowledge of allowed extensions in the target application (e.g., .jpg, .png).

## Defense

Defensive measures and detection strategies:

- Implement server-side validation of file content using magic bytes or libraries like ClamAV to verify actual file type, not just extension.
- Store uploaded files outside the web root or in non-executable directories with randomized filenames.
- Use web application firewalls (WAFs) to inspect and block suspicious upload requests, including double extensions.
- Enable logging of all file uploads and monitor for anomalies like extension mismatches or proxy-intercepted modifications.
- Scan uploaded files with antivirus/malware detection tools before processing.

## Objectives

1. Bypass client-side file type restrictions to upload a malicious script.
2. Intercept and modify the upload request to ensure the file is stored with the intended executable extension.
3. Verify successful upload by accessing and executing the malicious file on the server.
4. Achieve initial code execution foothold for further exploitation.

## Instructions

### Step 1: Identify File Upload Functionality

**Context**: Locate the file upload feature in the web application to understand the validation rules and allowed extensions. This step ensures you target the correct endpoint and know what extensions pass client-side checks.

Navigate to the application's upload page using your browser. Inspect the page source or use developer tools (F12) to identify any JavaScript that enforces extension validation. Test with benign files (e.g., a real .jpg) to confirm allowed types.

### Step 2: Prepare Malicious File with Double Extension

**Context**: Create or rename the malicious file to append an allowed extension, tricking the client-side validation into accepting it as a safe file type.

Use your file explorer or command line to rename the malicious file. For example, if .jpg is allowed, rename Malicious.php to Malicious.php.jpg. Ensure the malicious file contains executable code, such as a basic PHP webshell.

### Step 3: Initiate File Upload

**Context**: Select and submit the double-extended file through the web application's upload interface, allowing the request to be captured by the proxy.

In the browser, select the renamed file (Malicious.php.jpg) using the upload form and click submit. Ensure Burp Suite is actively intercepting traffic for the target site.

### Step 4: Intercept and Modify Upload Request

**Context**: Capture the HTTP POST request in Burp Suite and alter the filename parameter to strip the benign extension, ensuring the server receives the file as executable.

In Burp Suite's Proxy tab, intercept the upload request. Locate the filename parameter in the multipart/form-data body (e.g., Content-Disposition: form-data; name="file"; filename="Malicious.php.jpg"). Edit it to filename="Malicious.php" and forward the request. Drop any additional validation parameters if present.

### Step 5: Verify Upload and Execution

**Context**: Confirm the file was uploaded successfully and test its executability to validate the bypass.

After forwarding, check the application's response for success messages. Navigate to the upload directory (if known, e.g., /uploads/Malicious.php) and access it via browser (e.g., http://target.com/uploads/Malicious.php?cmd=whoami). If successful, the server should execute the payload and return output.
