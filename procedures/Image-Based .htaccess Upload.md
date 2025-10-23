---
id: ea981257-414f-41e0-95d2-d6f842e85c76
name: Image-Based .htaccess Upload
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.899972+00:00'
updated_at: '2023-04-06T03:56:40.919483+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Dynamic Resolution|T1568 - Dynamic Resolution]]'
- '[[File Permissions Modification|T1222 - File Permissions Modification]]'
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
- '[[Windows Remote Management|T1028 - Windows Remote Management]]'
tags:
- '[[.htaccess upload as image]]'
commands:
- '[[Check image type]]'
- '[[Image Protection]]'
---

# Image-Based .htaccess Upload

## Summary

Image-Based .htaccess Upload is a technique used by attackers to bypass web application security measures and upload a malicious .htaccess file. Attackers use image files to hide the .htaccess file, which is then uploaded to the web server. The .htaccess file can be used to redirect users to a mali

## Description

# Description

Image-Based .htaccess Upload is a technique used by attackers to bypass web application security measures and upload a malicious .htaccess file. Attackers use image files to hide the .htaccess file, which is then uploaded to the web server. The .htaccess file can be used to redirect users to a malicious website or to steal sensitive information. This technique can be used to achieve persistence on the target system. The attacker can modify the .htaccess file to maintain access to the system even if the original vulnerability used to upload the file is patched.

Technical Explanation: Attackers use image files to hide the .htaccess file. The image file is then uploaded to the web server. The server interprets the image file as an image and stores it in the web directory. The attacker can then access the .htaccess file by making a request to the image file. The .htaccess file can be used to redirect users to a malicious website or to steal sensitive information.

Business Value: This technique can be used by attackers to bypass web application security measures and gain access to sensitive information. It can also be used to maintain access to the target system even if the original vulnerability used to upload the file is patched.

 

## Requirements

1. Access to the target web server

1. Ability to upload files to the web server

1. Knowledge of image-based .htaccess upload techniques

 

## Defense

1. Implement strict file upload controls and image validation checks on the web application

1. Regularly monitor the web server for suspicious activity, such as unexpected file uploads or changes to the .htaccess file

1. Implement access controls and permissions to restrict access to sensitive files and directories

 

## Objectives

1. Upload a malicious .htaccess file to the target system

1. Maintain access to the target system even if the original vulnerability used to upload the file is patched

1. Redirect users to a malicious website or steal sensitive information

 

# Instructions

1. exif_imagetype() function is used, it returns the type of the given image file. The returned value is an integer representing one of the IMAGETYPE_XXX constants.

 



**Code**: [[exif_imagetype]]



> The exif_imagetype() function is used to determine the type of a given image file. This function returns one of the IMAGETYPE_XXX constants defined in the PHP GD library. These constants represent the type of the image file, such as JPEG, PNG, GIF, etc. The function takes one argument, which is the filename of the image file. If the file is not found or is not a valid image file, the function returns the value FALSE.



**Command** ([[Check image type]]):

```bash
path/to/image.jpg
```



2. Use the following commands to detect and create the image type:

 



**Code**: [[.htaccess/image]]



> The 'Image Type Detection and Creation' function can be achieved using the following commands:
1. getImageType() - This command is used to detect the type of image file. It takes the image file path as an argument.
2. createImage() - This command is used to create an image file. It takes the image file path and image type as arguments.

Example:
getImageType('/path/to/image.jpg');
createImage('/path/to/newimage', 'png');

3. To configure access control with .htaccess, you can use the following commands:

 



**Code**: [[.htaccess]]



> 1. AuthType: Specifies the authentication type to be used.
2. AuthName: Specifies the name of the authentication realm.
3. AuthUserFile: Specifies the path to the password file.
4. Require: Specifies the access requirements for a particular resource.

4. grep -v '^\<character\>' file.txt

 



**Code**: [[\x00]]



> This command allows you to ignore lines in a file that start with a specific character. Replace 'character' in the instruction with the character you want to ignore. The command uses grep with the -v option to invert the match and only show lines that do not begin with the specified character. The caret (^) symbol indicates the beginning of a line and the angle brackets (\< and \>) indicate a word boundary, ensuring that only lines that start with the specified character are matched.

5. The Concatenation Command is used to join two or more strings together.

 



**Code**: [[#]]



> The command takes two or more arguments, which can be either strings or variables that contain strings. The strings are joined together in the order they are given, with the 'and' text string used as a separator. The resulting string is returned as output. For example, if the command is given the arguments 'Hello', 'World', and '!', the output would be the string 'Hello and World and !'.

6. To generate a valid .htaccess image script, follow these steps:
1. Open a text editor and create a new file.
2. Copy and paste the following code into the file:

<IfModule mod_rewrite.c>
RewriteEngine On
RewriteRule ^image.jpg$ /path/to/image.jpg [L]
</IfModule>

Note: Replace '/path/to/image.jpg' with the actual path to your image file.
3. Save the file as '.htaccess' in the same directory as your image file.
4. Upload the '.htaccess' file and your image file to your web server.

Once you have completed these steps, the '.htaccess' file will redirect requests for 'image.jpg' to the actual image file, ensuring that the image is displayed correctly on your website.

 



**Code**: [[.htaccess/image]]



> The '.htaccess' file is a configuration file used by the Apache web server to control various aspects of website functionality. One of the most common uses of the '.htaccess' file is to create redirects, which allow you to redirect requests for one URL to another URL. In the case of images, a redirect can be used to ensure that the image is displayed correctly on your website, even if the image file is located in a different directory than the web page that displays it. The script provided in this JSON object is a sample '.htaccess' file that can be used to create a redirect for an image file called 'image.jpg'. By following the instructions provided, you can generate a valid '.htaccess' file and upload it to your web server to ensure that your images are displayed correctly.



**Command** ([[Image Protection]]):

```bash
.htaccess/image
```



7. To create a valid .htaccess/xbm image, follow these steps:
1. Set the desired width and height of the image.
2. Define the payload that you want to include in the image.
3. Open the .htaccess file and write the width, height, and payload to it using the 'write' function.

Example:

width = 50
height = 50
payload = '# .htaccess file'

with open('.htaccess', 'w') as htaccess:
    htaccess.write('#define test_width %d\n' % (width, ))
    htaccess.write('#define test_height %d\n' % (height, ))
    htaccess.write(payload)

 



**Code**: [[# create valid .htaccess/xbm image

width = 50
hei]]



> The 'width' and 'height' variables are used to define the dimensions of the image. The 'payload' variable is used to define the content of the image. The 'open' function is used to open the .htaccess file in write mode. The 'write' function is used to write the width, height, and payload to the .htaccess file. The resulting file can be used as a valid .htaccess/xbm image.

8. Use this command to create a valid .htaccess/wbmp image.

 



**Code**: [[# create valid .htaccess/wbmp image

type_header =]]



> The command creates a valid .htaccess/wbmp image by setting the required headers and dimensions. The resulting image will have a width and height of 50 pixels each and will contain the text '# .htaccess file'. The image will be saved as '.htaccess' in the current directory.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Dynamic Resolution|T1568 - Dynamic Resolution]]
- [[File Permissions Modification|T1222 - File Permissions Modification]]
- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]
- [[Windows Remote Management|T1028 - Windows Remote Management]]

## Commands Used

- [[Check image type]]
- [[Image Protection]]

## Tags

- [[.htaccess upload as image]]


