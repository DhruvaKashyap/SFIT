class HEAD:
    def __init__(self, path: str) -> None:
        self.path = path

    def get_ref(self) -> str:
        with open(self.path, 'r') as file:
            ref: str = file.readline().strip()
            if ref.startswith('refs/heads/'):
                # Return the file name in reference to refs/heads
                return ref[len('refs/heads/'):]
            else:
                # Return the reference as is (when HEAD is 'detached')
                return ref

    def set_ref(self, ref: str) -> None:
        with open(self.path, 'w') as file:
            if ref.startswith('refs/'):
                # For branch references, provide complete reference
                file.write(ref)
            else:
                # Relative reference
                file.write('refs/heads/' + ref)

    def show_ref(self) -> str:
        # Useful for other CLI commands like log, status, so can be directly imported
        return self.get_ref()
