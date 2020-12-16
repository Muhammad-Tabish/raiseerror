class RuntimeError(TypeError):
    """
    EXception raised when a specific error code is needed
    """
    def __init__(self, message, code):
        super().__init__(f'Error code {code} : {message }')
        self.code = code

raise  RuntimeError('OUCH An error happend', 500)
