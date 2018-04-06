"""Employee data object."""


class Employee:
    """Employee class."""

    def __init__(self, first_name, last_name):
        """Inistantiate employee object."""
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self):
        """Convert object to json."""
        return {
            "Employees": {
                'first_name': self.first_name,
                'last_name': self.last_name
            }
        }
