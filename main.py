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

# Set the API key and endpoint from GitHub Secrets
# api_key = os.environ['AZURE_COGNITIVE_SERVICES_KEY']
# api_endpoint = os.environ['AZURE_COGNITIVE_SERVICES_ENDPOINT']

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



# for further analytics
def AnalyzeImage(image_file):
    print('Analyzing', image_file)

    # Specify features to be retrieved
    features = [VisualFeatureTypes.description,
                VisualFeatureTypes.tags,
                VisualFeatureTypes.categories,
                VisualFeatureTypes.brands,
                VisualFeatureTypes.objects,
                VisualFeatureTypes.adult]
    
    
    # Get image analysis
    with open("." + image_file, mode="rb") as image_data:
        analysis = client.analyze_image_in_stream(image_data, features)

    # Get image description
    for caption in analysis.description.captions:
        print("Description: '{}' (confidence: {:.2f}%)".format(caption.text, caption.confidence * 100))

    # Get image tags
    if (len(analysis.tags) > 0):
        print("Tags: ")
        for tag in analysis.tags:
            print(" -'{}' (confidence: {:.2f}%)".format(tag.name, tag.confidence * 100))

    # Get image categories
    if (len(analysis.categories) > 0):
        print("Categories:")
        landmarks = []
        for category in analysis.categories:
            # Print the category
            print(" -'{}' (confidence: {:.2f}%)".format(category.name, category.score * 100))

    # Get brands in the image
    if (len(analysis.brands) > 0):
        print("Brands: ")
        for brand in analysis.brands:
            print(" -'{}' (confidence: {:.2f}%)".format(brand.name, brand.confidence * 100))

    # Get objects in the image
    if len(analysis.objects) > 0:
        print("Objects in image:")

        # Prepare image for drawing
        fig = plt.figure(figsize=(8, 8))
        plt.axis('off')
        image = Image.open(image_file)
        draw = ImageDraw.Draw(image)
        color = 'cyan'
        for detected_object in analysis.objects:
            # Print object name
            print(" -{} (confidence: {:.2f}%)".format(detected_object.object_property, detected_object.confidence * 100))
            
            # Draw object bounding box
            r = detected_object.rectangle
            bounding_box = ((r.x, r.y), (r.x + r.w, r.y + r.h))
            draw.rectangle(bounding_box, outline=color, width=3)
            plt.annotate(detected_object.object_property,(r.x, r.y), backgroundcolor=color)

        # Save annotated image
        plt.imshow(image)
        outputfile = 'objects.jpg'
        fig.savefig(outputfile)
        print('  Results saved in', outputfile)

    # Get moderation ratings
    ratings = 'Ratings:\n -Adult: {}\n -Racy: {}\n -Gore: {}'.format(analysis.adult.is_adult_content,
                                                                        analysis.adult.is_racy_content,
                                                                        analysis.adult.is_gory_content)
    print(ratings)



if __name__ == '__main__':
    with open('README.md') as f:
        markdown_text = f.read()

    missing_alt_text = find_missing_alt_text(markdown_text)
    print("images with missing alt text:", missing_alt_text, "\n")

    alt_text_suggestions = suggest_alt_text(missing_alt_text)

    for image_url, alt_text in alt_text_suggestions:
        print(f"Suggested alt text for '{image_url}' : {alt_text}")
