## 2024-03-24 - CLI Accessibility
**Learning:** For CLI tools, using Unicode symbols like ✓ and ✗ improves scannability compared to relying solely on text like PASS/FAIL, especially when ANSI color codes are avoided to minimize dependencies.
**Action:** Use universally supported Unicode symbols for status indicators in CLI output.

## 2024-05-18 - CLI Argument Help and Choices
**Learning:** Adding descriptive `help` texts to CLI arguments using `argparse` improves UX significantly. Explicitly setting `choices` for constrained arguments gives users an immediate list of valid options when an invalid one is supplied, saving them from encountering an execution error down the line.
**Action:** When implementing CLI commands, ensure to set `choices` if possible and use `help` attributes for all defined arguments to improve usability.
