---
id: 11d3770d-51f5-48a4-adab-d74da27d40d3
name: Display Author List using HTML Template PHPLIB
type: command
executor: bash
data: "<?php\n//we want to display this author list\n$authors = array(\n    'Christian\
  \ Weiske'  => 'cweiske@php.net',\n    'Bjoern Schotte'     => 'schotte@mayflower.de'\n\
  );\n\nrequire_once 'HTML/Template/PHPLIB.php';\n//create template object\n$t =&\
  \ new HTML_Template_PHPLIB(dirname(__FILE__), 'keep');\n//load file\n$t->setFile('authors',\
  \ 'authors.tpl');\n//set block\n$t->setBlock('authors', 'authorline', 'authorline_ref');\n\
  \n//set some variables\n$t->setVar('NUM_AUTHORS', count($authors));\n$t->setVar('PAGE_TITLE',\
  \ 'Code authors as of ' . date('Y-m-d'));\n\n//display the authors\nforeach ($authors\
  \ as $name => $email) {\n    $t->setVar('AUTHOR_NAME', $name);\n    $t->setVar('AUTHOR_EMAIL',\
  \ $email);\n    $t->parse('authorline_ref', 'authorline', true);\n}\n\n//finish\
  \ and echo\necho $t->finish($t->parse('OUT', 'authors'));\n?>"
output: null
created_at: '2023-04-06T03:56:40.435733+00:00'
updated_at: '2023-04-10T20:23:38.202907+00:00'
---

# Display Author List using HTML Template PHPLIB

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
