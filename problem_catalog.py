from known_problem import KnownProblem
from log_entry import LogEntry

class ProblemCatalog:
    def __init__(self):
        self.problems = {}

    # Add a known problem to the catalog
    def add_problem(self, problem):
        if not isinstance(problem, KnownProblem):
            raise TypeError("problem must be an instance of KnownProblem.")
        if problem.problem_id in self.problems:
            raise ValueError(f"Problem with ID '{problem.problem_id}' already exists.")
        self.problems[problem.problem_id] = problem

    # Find known problems that match a given message
    def find_matches(self, message):
        if not isinstance(message, str) or not message.strip():
            raise ValueError("message must be a non-empty string.")
        matches = []
        for problem in self.problems.values():
            if problem.matches(message):
                matches.append(problem)
        return matches

    # Find known problems that match a list of log entries
    def find_matches_for_logs(self, logs):
        # Validate input type
        if not isinstance(logs, list):
            raise TypeError("logs must be a list of LogEntry instances.")

        # Validate each log entry in the list
        for log in logs:
            if not isinstance(log, LogEntry):
                raise TypeError("Each item must be a LogEntry instance.")

        matches = {}
        # Iterate through each log entry and find matching known problems
        for log in logs:
            for problem in self.find_matches(log.message):
                if problem.problem_id not in matches:
                    matches[problem.problem_id] = []
                matches[problem.problem_id].append(log)
        return matches
    
    