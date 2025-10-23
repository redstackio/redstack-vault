---
id: b685b9b7-d8a9-4ac6-9cdf-547c0b525956
name: Server Side Template Injection using PHPlib and HTML_Template_PHPLIB
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.445023+00:00'
updated_at: '2023-04-10T20:23:38.184447+00:00'
tags:
- '[[PHPlib and HTML_Template_PHPLIB]]'
- '[[Server Side Template Injection]]'
commands:
- '[[Display All Authors]]'
- '[[Display Author List using HTML Template PHPLIB]]'
- '[[Display Authors]]'
---

# Server Side Template Injection using PHPlib and HTML_Template_PHPLIB

## Summary

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to inject malicious code into a web application's template, which is then executed on the server-side. This can result in sensitive data being exposed, server-side code execution, or even a complete compromise of the t

## Description

# Description

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to inject malicious code into a web application's template, which is then executed on the server-side. This can result in sensitive data being exposed, server-side code execution, or even a complete compromise of the target system. This procedure utilizes PHPlib and HTML_Template_PHPLIB to perform SSTI attacks. PHPlib is a set of PHP libraries that provide a framework for developing PHP applications, and HTML_Template_PHPLIB is a template engine that allows developers to separate the presentation layer from the logic layer of their web applications. By exploiting vulnerabilities in these libraries, an attacker can inject malicious code into the template and execute it on the server-side. The business value of this procedure is that it allows an attacker to gain access to sensitive data or take control of the target system.

 

## Requirements

1. Access to the web application

1. Knowledge of the target system and its vulnerabilities

1. PHPlib and HTML_Template_PHPLIB libraries installed on the target system

 

## Defense

1. Regularly update and patch the PHPlib and HTML_Template_PHPLIB libraries

1. Implement input validation and output encoding to prevent SSTI attacks

1. Implement strict access controls to limit the impact of SSTI attacks

 

## Objectives

1. Inject malicious code into the web application's template

1. Execute the malicious code on the server-side

1. Gain access to sensitive data or take control of the target system

 

# Instructions

1. To use this template, you can follow these commands:
1. create_author - This command is used to create a new author. It requires the following arguments:
   - name: The name of the author (string)
   - age: The age of the author (integer)
   - nationality: The nationality of the author (string)
2. get_author - This command is used to get the details of an author. It requires the following argument:
   - name: The name of the author (string)
3. update_author - This command is used to update the details of an author. It requires the following arguments:
   - name: The name of the author to update (string)
   - field: The field to update (string)
   - value: The new value for the field (string or integer)
4. delete_author - This command is used to delete an author. It requires the following argument:
   - name: The name of the author to delete (string)

 



**Code**: [[authors.tpl]]



> This JSON object contains the details for an authors template. The 'data' field specifies the path to the template file. The 'instruction' field provides the commands that can be used with this template, along with the arguments required for each command. The 'explain' field provides a brief description of the template and its purpose. The 'name' field has been filled in as 'Authors Template', which provides a clear and concise name for the template.



**Command** ([[Display Authors]]):

```bash
<div>
	<h1>Authors</h1>
	<ul>
		<li>John Doe</li>
		<li>Jane Smith</li>
	</ul>
</div>
```



2. This command generates an HTML table with dynamic content.

 



**Code**: [[<html>
 <head><title>{PAGE_TITLE}</title></head>
 ]]



> The HTML table is generated using the provided HTML code in the 'data' field. The table is populated with data using the following variables:
- {PAGE_TITLE}: The title of the HTML page.
- {NUM_AUTHORS}: The total number of authors.
- {AUTHOR_NAME}: The name of an author.
- {AUTHOR_EMAIL}: The email of an author.
The data for these variables should be provided in the 'text' field as a JSON array of objects. Each object should have the following fields:
- 'page_title': The title of the HTML page.
- 'num_authors': The total number of authors.
- 'authors': An array of objects representing the authors. Each author object should have the following fields:
  - 'name': The name of the author.
  - 'email': The email of the author.

3. To list all authors, make a GET request to 'authors.php'

 



**Code**: [[authors.php]]



> This command retrieves a list of all authors in the system. The endpoint for this command is 'authors.php'. To execute this command, simply make a GET request to the endpoint. No arguments are needed for this command.



**Command** ([[Display All Authors]]):

```bash
<?php

require_once('config.php');

$sql = 'SELECT * FROM authors';
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo 'Name: ' . $row['name'] . ' - Email: ' . $row['email'] . '<br>';
    }
} else {
    echo '0 results';
}

$conn->close();
?>
```



4. Create a PHP script that displays a list of authors using HTML_Template_PHPLIB.

 



**Code**: [[<?php
//we want to display this author list
$autho]]



> This script uses HTML_Template_PHPLIB to display a list of authors. The author list is defined as an associative array, where the keys are the author names and the values are their email addresses. The script first includes the HTML_Template_PHPLIB library and creates a new template object. It then loads the template file 'authors.tpl' and sets a block called 'authorline'. The script sets some variables, such as the number of authors and the page title, and then loops through the author list, setting the variables for each author and parsing the 'authorline' block. Finally, the script finishes and echoes the output of the template.



**Command** ([[Display Author List using HTML Template PHPLIB]]):

```bash
<?php
//we want to display this author list
$authors = array(
    'Christian Weiske'  => 'cweiske@php.net',
    'Bjoern Schotte'     => 'schotte@mayflower.de'
);

require_once 'HTML/Template/PHPLIB.php';
//create template object
$t =& new HTML_Template_PHPLIB(dirname(__FILE__), 'keep');
//load file
$t->setFile('authors', 'authors.tpl');
//set block
$t->setBlock('authors', 'authorline', 'authorline_ref');

//set some variables
$t->setVar('NUM_AUTHORS', count($authors));
$t->setVar('PAGE_TITLE', 'Code authors as of ' . date('Y-m-d'));

//display the authors
foreach ($authors as $name => $email) {
    $t->setVar('AUTHOR_NAME', $name);
    $t->setVar('AUTHOR_EMAIL', $email);
    $t->parse('authorline_ref', 'authorline', true);
}

//finish and echo
echo $t->finish($t->parse('OUT', 'authors'));
?>
```



## Commands Used

- [[Display All Authors]]
- [[Display Author List using HTML Template PHPLIB]]
- [[Display Authors]]

## Tags

- [[PHPlib and HTML_Template_PHPLIB]]
- [[Server Side Template Injection]]


