## 2024-03-24 - CLI Accessibility
**Learning:** For CLI tools, using Unicode symbols like ✓ and ✗ improves scannability compared to relying solely on text like PASS/FAIL, especially when ANSI color codes are avoided to minimize dependencies.
**Action:** Use universally supported Unicode symbols for status indicators in CLI output.

## 2024-03-24 - CLI Argument Descriptions
**Learning:** For a CLI tool, adding help text to the `argparse` configuration makes the tool significantly more accessible to users unfamiliar with all the required arguments and subcommands, acting effectively as an application UI element for terminal environments.
**Action:** Always provide descriptive `help` parameters for CLI arguments in `argparse` scripts.
