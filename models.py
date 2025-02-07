from dotenv import load_dotenv
import os

load_dotenv()

models = os.getenv("MODELS")

MODELS = [
    "CompVis/stable-diffusion-v-1-4-original",
"stabilityai/stable-diffusion-2",
"dreamlike-art/dreamlike-photoreal-2.0",
"Yntec/Dreamshaper8",
"Yntec/epiCPhotoGasm",
"stabilityai/stable-diffusion-xl-base-1.0",

]

if models:
    models_list = models.split(",")
    MODELS.extend(models_list)
