# AltSuggestor
 Markdown alt text suggestor - GitHub Action that can be enabled by maintainers to scan markdown documents looking for inline images missing alt text and suggesting them. 

# Submission for Microsoft Code; Without Barriers Hackathon 2023

## Assumptions
1. The standard markdown format for inline images and alt text is as follows:

    `
    ![alt_text](relative_or_absolute_path "description")
    `

    - ! to indicate an inline image
    - [] for alternate text, brackets must exist, but its contents can be empty
    - (path) is required, description is optional

2. As the suggestor solution detects an image by its img tag in html form (after converting markdown into html), it assumes that the markdown is correctly written and formatted to enable accurate markdown-to-html conversion. It will then return whether an image tag contains an empty alt attribute.


## Image gallery (for testing AltSuggestor)

Here are some inline images **without** alt text

![](/images/kain.png "A screenshot of Kain")
![](/images/mbs.jpeg "A screenshot of Marina Bay Sands")
![](/images/alt-text.png "A screenshot explaining what is alternate text")

Here are some inline images **with** alt text

![IPv4](/images/ip.png "A screenshot explaining what is an IPv4")
![Dog](/images/dog.jpeg "A screenshot of a dog")


## Running AltSuggestor
1. You need to have a working and running Azure Cognitive Service resource (for Computer Vision API)
2. Clone this GitHub
3. Edit the .env.example file to contain your Azure Cognitive Service resource key and rename the file to .env
4. Install the dependent libraries and modules `pip3 install -r requirements.txt`
5. Add your own inputs following below's section and try merging branches or pushing the new changes to the main branch.


## Trying out with your own image inputs
Here, you can edit this section of the README.md to add your own inputs to test.
This is to test future PR pre-merge checks or just predically checks.
You have to indicate 1. the new markdown text in README.md and 2. insert the respective image into the images folder


## Test Workflow
Here are some inline images **without** alt text

![](/images/bigben.jpg "A screenshot of London's Big Ben")
![](/images/macbook.jpg "A picture of a Macbook")
![](/images/milktea.jpg "A picture of a milktea")