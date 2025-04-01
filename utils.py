from tempfile import NamedTemporaryFile

class Utils:
    async def create_temporary_file(self, file):
        with NamedTemporaryFile(delete=False, suffix=".csv") as temporary_file:
            temporary_path = temporary_file.name
            content = await file.read()
            temporary_file.write(content)
        return temporary_path
