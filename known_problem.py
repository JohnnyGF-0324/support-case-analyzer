class KnownProblem:
    def __init__(self, problem_id, title, keywords, workaround):

        # Validate input types and values
        if not isinstance(problem_id, str) or not problem_id.strip():
            raise ValueError("problem_id must be a non-empty string.")
        if not isinstance(title, str) or not title.strip():
            raise ValueError("title must be a non-empty string.")
        if not isinstance(keywords, list):
            raise TypeError("keywords must be a list of strings.")
        if not keywords:
            raise ValueError("keywords list cannot be empty.")
        for keyword in keywords:
            if not isinstance(keyword, str) or not keyword.strip():
                raise ValueError("Each keyword must be a non-empty string.")
        if not isinstance(workaround, str) or not workaround.strip():
            raise ValueError("workaround must be a non-empty string.")

        # Assign validated values to instance variables
        self.problem_id = problem_id
        self.title = title
        self.keywords = keywords.copy()
        self.workaround = workaround

    # Check if the problem matches a given message based on keywords
    def matches(self, message):
        if not isinstance(message, str) or not message.strip():
            raise ValueError("message must be a non-empty string.")
        return all(keyword.lower().strip() in message.lower() for keyword in self.keywords)