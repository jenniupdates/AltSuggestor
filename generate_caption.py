import os
import io
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from dotenv import load_dotenv
load_dotenv()

# Set your API key and endpoint
api_key = os.getenv('AZURE_COGNITIVE_SERVICES_KEY')
api_endpoint = os.getenv('AZURE_COGNITIVE_SERVICES_ENDPOINT')

# Set up the Computer Vision client
credential = CognitiveServicesCredentials(api_key) 
client = ComputerVisionClient(api_endpoint, credential)

# Set the path to the image file
image_path = "./images/ip.png"

# Open the image file and get the image data
with open(image_path, "rb") as image_file:
    image_data = image_file.read()

# Create an in-memory stream from the image data
stream = io.BytesIO(image_data)

# Analyze the image and get the caption
analysis = client.analyze_image_in_stream(stream, [VisualFeatureTypes.description])
caption = analysis.description.captions[0].text

# Print the caption
print("Caption: {} (confidence: {:.2f}%)".format(analysis.description.captions[0].text, analysis.description.captions[0].confidence * 100))
