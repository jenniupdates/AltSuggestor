# AltSuggestor
AltSuggestor is a simple yet game-changing and automated Markdown alt text suggestor. With AltSuggestor, you can now enhance both **social inclusiveness and web accessibility** of your project. 

It scans through your project's README.md file, detects inline images that do not contain alt text and suggests them accordingly.

## Description
AltSuggestor consists of a GitHub Action that automates the reading of your project's README.md file, highlights inline images with no alt text and suggests the relevant alt text (alternate text) for the respective images. 

With alt text, a visually impaired user or someone who is otherwise unable to view the images on the page can now read information about the images. Furthermore, alt text provides better image context/description to search engine crawlers, helping them to index and rank an image properly in image search, improving search engine optimisation (SEO). In addition, if an image file is unable to load, alt text will be displayed in its place. 

Hence, alt text is important in allowing your project to achieve higher social inclusivity and web accessbility/visibility.

Altsuggestor is also my submission for the Microsoft Code; Without Barriers Hackathon 2023.
Done by: Lim Yin Shan

## Assumptions / Scope
1. It is believed that the standard markdown format for inline images and alt text is as follow:

    `
    ![alt_text](relative_or_absolute_path "description")
    `

    - ! to indicate an inline image
    - [] for alternate text, brackets must exist, but its contents can be empty
    - (path) is required, description is optional

2. As the solution will detect an image by its img tag in html format (after converting the markdown into html), it assumes that the markdown is accurately written and formatted as above to enable correct markdown-to-html conversion. It will then return whether an image tag contains an empty alt attribute.

3. The GitHub Action's yml file is configured to be **triggered on a pull request event on the "main" branch**. Hence, this would assume proper branch protection rules is in place such that checks cannot be overwritten and pull request will fail if the status checks fail. Should your branch name be different, you can rename the workflow accordingly to work on your branch.

## Pre-requisites
- Azure Cognitive Service resource setup
- Proper branch protection rules

## Running the AltSuggestor in your own repository
1. You will need to have an existing Azure Cognitive Service resource running (for the Computer Vision API).
    - You are required to set this service up. Without it, there will be no alt text suggestions.
2. Create a new branch based on your main branch and **enable branch protection rules**.
    - your main branch
    - "Require a pull request before merging"
    - "Require status checks to pass before merging"
    - "Require conversation resolution before merging"
    - "Do not allow bypassing the above settings"
2. Clone this GitHub repository or download its contents and **place everything** in your project's directory/repository.
    - "github/workflows/main.yml" -- the GitHub Action that will automate AltSuggestor
    - do note that you will need every file except the README.md for the AltSuggestor to be working properly
    - if you have any files with duplicate name, please rename your own files 
    - delete the cloned/downloaded README.md and make sure your own project's README.md is in the same directory as the cloned/downloaded files
    - do not touch any of the other cloned/downloaded files
3. Create two GitHub repository secret so that the GitHub Action can retrieve the keys from:
    - **AZURE_COGNITIVE_SERVICES_ENDPOINT**=<your_azure_cognitive_service_endpoint>
    - **AZURE_COGNITIVE_SERVICES_KEY**=<your_azure_cognitive_service_key> (either one of the two)
4. Push your new commits to the new branch.
5. Create a pull request to merge your new branch with your main branch.
    - after creation, it should run the AltSuggestor Action:
        - if all your README.md's images **have alt text**, it would pass the check and you can proceed to merging the two branches
        - if some of your README.md's images **DO NOT HAVE alt text**, it would fail the status check
            - click "details" to see why the check failed
            - click on the job named "Reading output file", it would tell you which image did not have alt text as well as the suggested image caption
            - edit your README.md accordingly and push the new updates to the branch
            - check back the same pull request, it would automatically call AltSuggestor again

## AltSuggestor Demo
video to be inserted here

## Future Improvements
1. More fine-tuned caption generator

## Credits and Acknowledgements
why alt text suggestor - https://moz.com/learn/seo/alt-text

## Image gallery (for testing AltSuggestor)

Here are some inline images **without** alt text

![](/images/mbs.jpeg "A screenshot of Marina Bay Sands")
![](/images/bigben.jpg "A screenshot of London's Big Ben")
![](/images/macbook.jpg "A picture of a Macbook")
![](/images/milktea.jpg "A picture of a milktea")

Here are some inline images **with** alt text

![Maplestory's Kain Character](/images/kain.png "A screenshot of Kain")
![A happy dog](/images/dog.jpeg "A screenshot of a dog")