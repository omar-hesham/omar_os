## 2024-03-24 - CLI Accessibility
**Learning:** For CLI tools, using Unicode symbols like ✓ and ✗ improves scannability compared to relying solely on text like PASS/FAIL, especially when ANSI color codes are avoided to minimize dependencies.
**Action:** Use universally supported Unicode symbols for status indicators in CLI output.

## 2024-03-24 - Argparse Usage Scannability
**Learning:** For Python CLI tools using `argparse`, when positional arguments have a long list of `choices` (like lifecycle stages) or there are multiple `subparsers`, the auto-generated `usage` string becomes extremely cluttered and difficult to read (e.g. `usage: command {choice1,choice2,choice3...}`).
**Action:** Use the `metavar` argument (e.g. `metavar="STAGE"`) when defining arguments with long choices, and `metavar="COMMAND"` with a `title` when adding subparsers to significantly improve the scannability of the help menu.
