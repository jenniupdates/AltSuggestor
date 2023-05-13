# AltSuggestor
Markdown alt text suggestor - GitHub Action that can be enabled by maintainers to scan markdown documents looking for inline images missing alt text and suggesting them. 

# Submission for Microsoft Code; Without Barriers Hackathon 2023
Done by: Lim Yin Shan, ysimptstuff@gmail.com

## Assumptions
1. The standard markdown format for inline images and alt text is as follows:

    `
    ![alt_text](relative_or_absolute_path "description")
    `

    - ! to indicate an inline image
    - [] for alternate text, brackets must exist, but its contents can be empty
    - (path) is required, description is optional

2. As the solution detects an image by its <img> tag in html form (after converting markdown into html), it assumes that the markdown is accurately written and formatted to enable correct markdown-to-html conversion. It will then return whether an image tag contains an empty alt attribute.


## Running the AltSuggestor in your own repository
1. You need to have an existing Azure Cognitive Service resource working and running (for the Computer Vision API)
    - You are required to set this service up, without it there will be no alt text suggestions
2. Clone this GitHub or download its contents and place it in your repository. There are 2 versions:
    - If you want GitHub Actions to run using main.py directly, you need both main.py and requirements.txt    - If you want GitHub Actions to run using the docker version, you just need the AltSuggestor.yml in the workflow (note that docker version is not fully working yet, )
3. You need certain secrets for the workflow to run smoothly. They are:
    - AZURE_COGNITIVE_SERVICES_KEY (your own azure service, for both versions)
    - AZURE_COGNITIVE_SERVICES_ENDPOINT (your own azure service, for both versions)
    - DOCKER_USERNAME (your docker username, if you are using docker version)
    - DOCKER_PASSWORD (your docker password, if you are using docker version)
3. Edit your repository's README.md with inline images having no alt text. By the next push/pull request, you should see the AltSuggestor's effect taking place in GitHub Actions!
<!-- 3. Edit the .env.example file to contain your Azure Cognitive Service resource key and rename the file to .env
4. Install the dependent libraries and modules `pip3 install -r requirements.txt` -->
<!-- 5. Add your own inputs following below's section and try merging branches or pushing the new changes to the main branch. -->


## Trying out with your own image inputs
Here, you can edit this section of the README.md to add your own inputs to test.
This is to test future PR pre-merge checks or just predically checks.

You have to: 
1. add in the new markdown text in README.md containing the image and 
2. insert the respective image into the images folder (or if you're linking to an external image)


## Future Improvements
1. More fine-tuned caption generator (using OpenAI's DALL·E 2)


<!-- ## Image gallery (for testing AltSuggestor)

Here are some inline images **without** alt text

![](/images/kain.png "A screenshot of Kain")
![](/images/mbs.jpeg "A screenshot of Marina Bay Sands")
![](/images/bigben.jpg "A screenshot of London's Big Ben")
![](/images/macbook.jpg "A picture of a Macbook")
![](/images/milktea.jpg "A picture of a milktea")
![](/images/alt-text.png "A screenshot explaining what is alternate text")

Here are some inline images **with** alt text

![IPv4](/images/ip.png "A screenshot explaining what is an IPv4")
![Dog](/images/dog.jpeg "A screenshot of a dog") -->


## Credits and Acknowledgements

