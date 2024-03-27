class HttpConflictError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "Conflict"
        self.status_code = 409
