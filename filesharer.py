from filestack import Client

class FileSharer:

    def __init__(self, filepath, api_key="AeHe316uQaahI9VDtw8naz"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        # Ahora crearemos el link tras subir el archivo:
        new_filelink = client.upload(filepath=self.filepath)
        # Ahora nos devolvera la .url
        return new_filelink.url