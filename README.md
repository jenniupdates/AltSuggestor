# AltSuggestor
 Markdown alt text suggestor - GitHub Action that can be enabled by maintainers to scan markdown documents looking for inline images missing alt text and suggesting them. 

# Submission for Microsoft Code; Without Barriers Hackathon 2023

## Assumptions
1. The standard markdown format for inline images and alt text is as follows:

`
![alt_text](relative_or_absolute_path "description")
`

[x] ! to indicate an inline image
[x] [] for alternate text, brackets must exist, but its contents can be empty
[x] (path) is required, description is optional


## Image gallery

### Here are some inline images without alt text

![](/images/hoyoung.png "A screenshot of Hoyoung")
![](/images/phantom.png "A screenshot of Phantom")

### Here are some inline images with alt text
![Kain](/images/kain.png "A screenshot of Kain" )
![Ice Light](/images/icelight.png "A screenshot of Ice Lightning" )
