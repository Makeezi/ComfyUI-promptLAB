import requests

class PromptLAB:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "host": ("STRING", {"default": "http://127.0.0.1:"}),
                "port": ("INT", {"default": 5000}),
                "id": ("INT", {"default": 0}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive", "negative")
    FUNCTION = "prompt_lab"
    OUTPUT_NODE = False

    CATEGORY = "utils"

    def prompt_lab(self, host, port, id):
        url = f"{host}{port}/input/{id}"
        response = requests.get(url)
        data = response.json()
        return (data[0], data[1])


