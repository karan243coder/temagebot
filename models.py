from dotenv import load_dotenv
import os

load_dotenv()

models = os.getenv("MODELS")

MODELS = [
    "hakurei/waifu-diffusion-v1-3",

]

if models:
    models_list = models.split(",")
    MODELS.extend(models_list)
