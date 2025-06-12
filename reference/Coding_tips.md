# Tips for scientific coding

Scientific coding differs in important ways from programming for other applications. These tips are neither exhaustive nor universal. Apply any tips that help, ignore any that don't, and experiment with your own approach.

## Preparation and writing style

- Be clear on what your code should do before you even open an editor
- Use a "Documentation First" workflow
- Use a consistent documentation style
- Use automated testing and test-driven design
- Use an informative naming convention for variables and functions
- Use comments to describe the _intent_, not the _steps_
- Use comments to document any tricky edge cases or unusual patterns


## Generation

- Build out a skeleton of function definitions before working on the code within the functions (use placeholder code like `pass`)
- Favor functions that do just one thing, and do it well
- Use interactive interfaces to work out code blocks and test them by themselves before packing inside functions
- Run your code after every significant change to make sure it still works, and restart kernels often
- Use selective commenting and/or string blocks and/or if-then blocks to isolate bits of code during inspection
- Experiment! If you're not sure how a choice of code will affect the outcome, try it in a sandbox and see
- Test a wide range of situations (e.g. possible user input or data files), not just the ideal cases

## Checking, troubleshooting, and getting help

- Make your code _brittle_: if anything seems off, the code should fail and require human intervention, as small discrepancies often hide bigger problems within the data or the logic
- Actually read error messages, focussing on the line(s) that set off the error
- Cut and paste error messages when getting help online or from AI; include context like neighboring code and the values of key variables
- For tricky errors, try to construct a minimal reproducible example for study
- Produce lots of diagnostic outputs (e.g. using `print`) when developing new code
- A good AI prompt is *very* specific: take the energy you would have invested in writing the code itself and use it to maximize the precision of your description of what you need
- Never take AI at its word; review and test


## Higher level

- Save often
- Use version control with informative commit messages
- Always keep a working "sane state" version you can revert to before making changes
- Do exploratory work in notebooks, then package the most reusable code in modules
- Keep large projects organized with a sensible subdirectory structure
- If a block of code takes a long time to run, consider checkpointing (writing the block's output to a file, and bypassing the time-consuming block and loading the file instead if it already exists)
