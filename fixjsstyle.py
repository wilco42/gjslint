#!/usr/bin/python
from closure_linter import fixjsstyle
import exclusions

if __name__ == '__main__':
    exclusions.InjectErrorReporter()
    fixjsstyle.main()

