import os
import io
import markdown
from bs4 import BeautifulSoup

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

from dotenv import load_dotenv
load_dotenv()

# Set API key and endpoint from .env file 
api_key = os.getenv('AZURE_COGNITIVE_SERVICES_KEY')
api_endpoint = os.getenv('AZURE_COGNITIVE_SERVICES_ENDPOINT')

# Authenticate Computer Vision client
credential = CognitiveServicesCredentials(api_key)
client = ComputerVisionClient(api_endpoint, credential)


# Parse the Markdown file and identify any inline images that are missing alt text
def find_missing_alt_text(markdown_text):
    missing_alt_text = []

    md = markdown.Markdown(extensions=['meta'])
    html = md.convert(markdown_text)
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.findAll("img")
    for x in images:
        if x.get('alt') == "":
            missing_alt_text.append(x.get('src'))

    return missing_alt_text


# Analyze the images and suggest alt text
def suggest_alt_text(image_urls):
    alt_text_suggestions = []

    for image_url in image_urls:
        with open("." + image_url, "rb") as image_file:
            image_data = image_file.read()

        stream = io.BytesIO(image_data)
        analysis = client.analyze_image_in_stream(stream, [VisualFeatureTypes.description])
        caption = analysis.description.captions[0].text

        alt_text_suggestions.append((image_url, caption))

    return alt_text_suggestions



if __name__ == '__main__':
    with open('README.md') as f:
        markdown_text = f.read()

    missing_alt_text = find_missing_alt_text(markdown_text)
    if missing_alt_text != []:
        print("\nImages with missing alt text:", missing_alt_text, "\n")

        alt_text_suggestions = suggest_alt_text(missing_alt_text)

        for image_url, alt_text in alt_text_suggestions:
            print(f"Suggested alt text for '{image_url}' : {alt_text}")
        print("\n")
