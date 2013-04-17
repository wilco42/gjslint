Google Closure Linter wrapper
=============================

## Introduction
The Google Closure Linter does not have many options to toggle how strict it is in its enforcement of rules.  This is by their design as they want developers to strictly adhere to their coding guidelines.  If we want to deviate from their ruleset, there's no method to ignore certain rules.

This wrapper will allow one to ignore rules listed in the exclusions.py file from being reported when running gjslint.

## How to use
Instead of invoking gjslint, run the linter via the gjslint.py wrapper instead.
