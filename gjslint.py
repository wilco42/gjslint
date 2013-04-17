#!/usr/bin/python
from closure_linter import gjslint
import exclusions

if __name__ == '__main__':
    exclusions.InjectErrorReporter()
    gjslint.main()
