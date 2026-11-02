# Support Case Analyzer

## Project overview

Support Case Analyzer is a **fictional SaaS portfolio project using sample data**. It models part of a support investigation workflow: a support agent looks up a ticket, reviews logs for that ticket's customer, checks whether those logs match known problems, and prepares a readable report.

The project is an educational example; it is not connected to a real support platform or customer data.

## Features

- Create and manage support tickets, including ticket status.
- Filter customer logs by customer, level, keyword, and time range.
- Match log messages against known-problem keywords.
- Generate a report with a ticket summary, customer logs, and possible known-problem matches.
- Summarize tickets by status and logs by level.

## Requirements

- Python 3
- Python standard library only; no third-party packages are required.

## Running the demo

From the project directory, run:

```bash
python test_case_analyzer.py
```

The script creates sample tickets, logs, and known problems, then prints a report and ticket and log summaries.

## Running tests

Run the unit tests from the project directory with:

```bash
python -m unittest discover -p "test_*_unit.py"
```

This discovers the unit-test modules whose filenames end in `_unit.py`.

## Limitations

- Tickets, logs, and known problems are stored in memory and are not saved after the program exits.
- Known-problem matching uses keyword substring checks, not more advanced text analysis.
- Investigations consider all stored logs for the ticket's customer, regardless of when the logs were created.
- A match only suggests a possible cause; it does not confirm a diagnosis.
- The project uses fictional sample data and is not intended for production support work.

## Learning goals

This project is a way to practice Python classes, input validation, dictionaries, composition, and automated testing.