# Some header

You can put a description here that describes your app

For an amazing list of snippets you can reference this:
https://jupyterbook.org/en/stable/reference/cheatsheet.html 

```{toctree}
:maxdepth: 2
:caption: Instructions
:glob:
instructions.md
```

```{toctree}
:maxdepth: 2
:caption: Snippets
:glob:
snippets/*
```

```{eval-rst}  
.. autofunction:: test_some_tests.test_two_equals_two
```

