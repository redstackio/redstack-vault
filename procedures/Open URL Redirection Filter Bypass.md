---
id: 9f1da970-5d4f-4d6f-8200-032310364348
name: Open URL Redirection Filter Bypass
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:31.801592+00:00'
updated_at: '2023-04-10T20:23:05.927883+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Subvert Trust Controls|T1553 - Subvert Trust Controls]]'
sub_techniques:
- '[[Code Signing|T1553.002 - Code Signing]]'
- '[[Install Root Certificate|T1553.004 - Install Root Certificate]]'
- '[[SIP and Trust Provider Hijacking|T1553.003 - SIP and Trust Provider Hijacking]]'
tags:
- '[[Filter Bypass]]'
- '[[Open URL Redirection]]'
---

# Open URL Redirection Filter Bypass

## Summary

Open URL Redirection is a web application vulnerability that allows attackers to redirect users to malicious websites. Attackers can bypass filters and security mechanisms in place by using various techniques such as whitelisted domain or keyword redirect, URL bypass command, Unicode character redi

## Description

# Description

Open URL Redirection is a web application vulnerability that allows attackers to redirect users to malicious websites. Attackers can bypass filters and security mechanisms in place by using various techniques such as whitelisted domain or keyword redirect, URL bypass command, Unicode character redirection, parameter pollution attack, and others. This vulnerability can be used to steal user credentials, deliver malware, or perform other malicious activities. 

From a technical standpoint, open URL redirection occurs when a web application takes a parameter and redirects the user to the value of that parameter without validating it. This can be exploited by an attacker by crafting a malicious URL that looks legitimate and redirecting the user to a malicious website. 

The business value of this vulnerability is that it can be used as part of a larger attack chain to gain access to sensitive data or systems. By redirecting users to a phishing website, attackers can steal user credentials and gain access to corporate networks. This vulnerability can also be used to deliver malware to unsuspecting users.

 

## Requirements

1. Access to a vulnerable web application

1. Knowledge of open URL redirection vulnerability

1. Ability to craft a malicious URL

 

## Defense

1. Validate all user input and sanitize any data that will be used in a redirect

1. Implement a whitelist of allowed domains or keywords for redirection

1. Use HTTP Strict Transport Security (HSTS) to prevent HTTP to HTTPS downgrade attacks

 

## Objectives

1. Bypass URL filters and security mechanisms

1. Redirect users to malicious websites

1. Steal user credentials or deliver malware

 

# Instructions

1. To redirect a whitelisted domain or keyword to a malicious website, use the following command:

Redirect-WhitelistedDomain -Domain www.whitelisted.com.evil.com -RedirectTo evil.com

This command will redirect any requests to www.whitelisted.com.evil.com to the malicious website evil.com.

 



**Code**: [[www.whitelisted.com.evil.com redirect to evil.com]]



> The Redirect-WhitelistedDomain command allows an attacker to redirect traffic from a whitelisted domain or keyword to a malicious website. This can be useful in bypassing security measures that allow traffic from whitelisted domains or keywords to bypass security checks. The -Domain parameter specifies the domain or keyword to be redirected, while the -RedirectTo parameter specifies the URL of the malicious website to redirect traffic to.

2. The JavaScript Alert command is used to display a pop-up message box with a specified message. The command can be executed in various programming languages, including PowerShell. To execute the command, simply replace the message in the code with the desired text and run the script.

 



**Code**: [[java%0d%0ascript%0d%0a:alert(0)]]



> The 'java%0d%0ascript%0d%0a' portion of the code is used to bypass the 'javascript' blacklisted keyword. The '%0d%0a' characters represent the carriage return and line feed characters, respectively. By using these characters, the 'javascript' keyword is split into two separate strings, which bypasses the blacklist. The 'alert(0)' portion of the code is the actual JavaScript code that displays the pop-up message box. The '0' can be replaced with any desired message.

3. To use this command, simply insert the desired URL after the "//" or "////" characters. This command can be used to bypass blacklisted keywords, such as "http".

 



**Code**: [[//google.com
////google.com]]



> The "//" and "////" characters are used to bypass blacklisted keywords in URLs. By using these characters, the URL is interpreted as a relative URL, rather than an absolute URL. This can be useful in situations where certain keywords are blacklisted, but the URL itself is not harmful. By using this command, you can access the desired URL without triggering any blacklisted keyword filters.

4. To bypass the blacklisted keyword "//" using HTTPS, simply prefix the URL with "https:" instead of "http:".

 



**Code**: [[https:google.com]]



> When a URL contains the "//" characters, some firewalls or security software may block the request as it can be used to execute malicious code. However, by using the secure HTTPS protocol instead of HTTP, the request can bypass this restriction and still be sent to the server. This is because HTTPS encrypts the traffic, making it harder for attackers to exploit the "//" characters.

5. This command can be used to redirect a URL to a different website. The command uses a Unicode character "%E3%80%82" instead of the blacklisted character "." to bypass security measures. The command takes the following arguments:
1. URL: The URL to be redirected.
2. Redirect URL: The URL to redirect to.

 



**Code**: [[/?redir=google。com
//google%E3%80%82com]]



> The command works by using the Unicode character "%E3%80%82" instead of the blacklisted character "." in the URL. This allows the URL to bypass any security measures that may be in place to prevent redirection. The command can be used in situations where the blacklisted character is not allowed, but the Unicode character is allowed. However, it is important to note that this method may not work in all situations and may be detected by more advanced security measures.

6. To bypass a blacklist filter using null byte, follow these steps:
1. Identify the URL you want to access that is being blocked by a blacklist filter.
2. Append "%00" to the end of the URL.
3. Use the modified URL to bypass the blacklist filter and access the desired content.

 



**Code**: [[//google%00.com]]



> Blacklist filters are commonly used to block access to certain URLs or websites. However, these filters can be bypassed by appending a null byte "%00" to the end of a blocked URL. This works because the null byte effectively terminates the string, causing the blacklist filter to see a different URL than what is actually being accessed. This technique can be used to bypass a wide range of blacklist filters and gain access to blocked content.

7. The 'Parameter Pollution' attack involves manipulating the parameters passed to a web application in order to bypass security measures or gain unauthorized access. In this example, the attacker is attempting to redirect the user to two different websites by adding multiple 'next' parameters. This can be prevented by properly validating and sanitizing user input.

 



**Code**: [[?next=whitelisted.com&next=google.com]]



> The 'data' field contains the manipulated parameters used in the attack. The 'lang' field specifies the programming language used to execute the attack. The 'text' field provides a brief description of the attack. The 'instruction' field provides details on how the attack works and how to prevent it. The 'name' field provides a descriptive name for the attack.

8. To redirect to a specific webpage using the @ character, simply add the desired website after the @ symbol in the URL.

 



**Code**: [[http://www.theirsite.com@yoursite.com/]]



> This command can be useful for redirecting users to a specific page or for masking the actual URL of a webpage. However, it should be used with caution as it may cause confusion for users and may also be seen as a security risk.

9. To create folders for multiple domains, follow these steps:
1. Open PowerShell.
2. Navigate to the directory where you want to create the folders.
3. Use the following command to create folders for multiple domains:
   - For individual domains: mkdir domain1.com domain2.com domain3.com
   - For domains with subfolders: mkdir -p domain1.com/subfolder domain2.com/subfolder domain3.com/subfolder
4. Press Enter to execute the command.

 



**Code**: [[http://www.yoursite.com/http://www.theirsite.com/
]]



> This command allows you to create folders for multiple domains at once. The 'mkdir' command is used to create new directories (folders) and the '-p' option is used to create parent directories as needed. By specifying the domain names as arguments, you can create folders for multiple domains simultaneously. The command also supports creating subfolders within each domain folder by specifying the subfolder name after the domain name separated by a forward slash (/).

10. To pass query string parameters to a web server using a URL, add a "?" character followed by the parameter name and value, separated by an "=" character. Multiple parameters can be separated by an "&" character.

 



**Code**: [[http://www.yoursite.com?http://www.theirsite.com/
]]



> In the provided example, the first URL passes the parameter "http://www.theirsite.com/" to the web server at "http://www.yoursite.com". The second URL passes the parameter "www.folder.com" in the "folder" parameter to the same web server.

11. To prevent homograph attacks, it is recommended to use Unicode normalization. This command converts Unicode characters to their canonical form and splits the URL into its component parts. To host/split a URL using Unicode normalization, use the following command:

Normalize-String -NormalizationForm FormC $url | Split-Path -Leaf | Split-Path -Parent

 



**Code**: [[https://evil.c℀.example.com . ---> https://evil.ca]]



> The 'Normalize-String' command normalizes the Unicode characters in the URL to their canonical form using the FormC normalization form. The '-Leaf' parameter of the 'Split-Path' command returns the last element of the path, which is the domain name. The '-Parent' parameter of the 'Split-Path' command returns the parent directory of the domain name, which is the protocol and subdomains. This splits the URL into its component parts and prevents homograph attacks.

12. To execute this command, simply open the URL containing the vulnerable JavaScript variable, and replace the value of the variable with the payload provided in the 'data' field.

 



**Code**: [[";alert(0);//]]



> This command exploits a cross-site scripting (XSS) vulnerability that occurs when a website includes user input in a JavaScript variable without properly sanitizing it. An attacker can inject malicious code into the variable, which will execute when the variable is used in the website's JavaScript code. In this case, the payload provided in the 'data' field will execute an alert message when the vulnerable variable is used.

13. This command allows an attacker to execute arbitrary JavaScript code in the victim's browser by exploiting a cross-site scripting vulnerability in the data:// wrapper. To exploit this vulnerability, the attacker must first construct a specially crafted URL containing the malicious JavaScript code and then trick the victim into clicking on the link. Once the victim clicks on the link, the JavaScript code will execute in the victim's browser, giving the attacker access to sensitive information or the ability to perform unauthorized actions.

 



**Code**: [[http://www.example.com/redirect.php?url=data:text/]]



> The 'data://' wrapper is used to specify data in a URI. In this case, the attacker is using it to specify a base64-encoded HTML document containing malicious JavaScript code. When the victim clicks on the link, the browser decodes the base64-encoded data and renders the HTML document, executing the embedded JavaScript code. This vulnerability can be prevented by properly validating and sanitizing user input on the server-side and properly encoding output on the client-side.

14. To execute an XSS attack using the javascript:// wrapper, follow these steps:
1. Identify a website that allows user input in a vulnerable field.
2. Construct a URL that includes the javascript:// wrapper followed by the malicious script.
3. Submit the URL as the input in the vulnerable field.
4. When the victim visits the page and interacts with the vulnerable field, the script will execute.

 



**Code**: [[http://www.example.com/redirect.php?url=javascript]]



> The javascript:// wrapper allows the execution of JavaScript code from a URL. This can be used to execute malicious scripts on unsuspecting users. In this example, the URL includes a prompt function that will display a popup box with the message '1'. This is a simple example, but more complex scripts can be executed in the same way.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Subvert Trust Controls|T1553 - Subvert Trust Controls]]

### Sub-Techniques

- [[Code Signing|T1553.002 - Code Signing]]
- [[Install Root Certificate|T1553.004 - Install Root Certificate]]
- [[SIP and Trust Provider Hijacking|T1553.003 - SIP and Trust Provider Hijacking]]

## Tags

- [[Filter Bypass]]
- [[Open URL Redirection]]


