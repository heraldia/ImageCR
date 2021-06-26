Jason yuchen
刘禹3辰 9年级
s20477.liu@stu.scie.com.cn
git: Jason-Liu813
Josephine [\Claire]
2021_0612_0931 还是3年才上大学，英国体制
    
Windows 10
Lecture Note

# Topic: Image copyright. 网络图片产权保护
Apart from the literature review, project milestones are
1. Web crawling images from Internet. (Javascript)
2. Image comparison algorithm development. (Python, OpenCV)
3. Invent our own novel image fingerprinting algorithm to protect image identity. (Python)
Survey on the status quo will be conducted.

# Topic 3: Image copyright 网络图片产权保护
Myriad of images are extensively uploaded and widely spread on the Internet.
According to the report of "Social Media Statistics 2019: Top Networks By the Numbers • Dustin Stout" (https://dustinstout.com/social-media-statistics/),
we can see
* On average, 95 million photos are uploaded daily on Instagram.
* Since Instagram's creation, more than 40 billion photos have been shared.
* There are approximately 4.2 billion likes per day.

The image copyright is critical to publishers, authors, photographers and organizations. Therefore, intellectual property (IP) protection is significant to this atmosphere.

Image copyright cases draw many attentions globally. Authorities even stream into this area since Aug. 2019.

Please refer to these news
图片作品侵权案件爆发式增长--知识产权--人民网
http://ip.people.com.cn/n1/2019/0430/c179663-31059183.html
涉图片类作品著作权案件爆发式增长的应对--知识产权--人民网
http://ip.people.com.cn/n1/2018/1122/c179663-30415651.html
人民网进军图片版权出大招 视觉中国崩了 知识产权概念继续发威？ _ 东方财富网
http://finance.eastmoney.com/a/201904141096060840.html

We will conduct a cutting-edge research at the forefront of computer science. The requirement is from the real problem today and out research greatly contributes to this area.
Our targets are as follows:
- Complete a comprehensive survey.
- Compare and cluster similar pictures or identical pictures derived from one original picture.
- Append meta data and identification to original photos/pictures.
- Web crawling the similar suspicious pictures that are not approved by the original photographers.
- Using computer vision technique to compare and inspect the similarities between the original protected picture and the un-authorized picture.
- Trace the identified pictures that are shared / modified in the Internet globally.

trace an image internet
The scope of pictures include App icons, product logos, photos taken by photographers, pictures designed by designers, etc.

The technologies involved in this project contains computer vision, image processing, web crawler, big data storage, blockchain (if time permits), web development, etc.

学生技能要求：计算机/电子工程专业，图像识别，computer vision, OpenCV, Python
期望出品：英文会议文章，如IEEE等。
课题当前热度: 3
长期延申扩展性: 5

{
what do you want to share
questinos}

2020_1031_0830 前导 {{{2 {
yuchen
Clarie
https://github.com/heraldia/ImageCR     
} 2}}}

2020_1120_0828 1st {{{2 {
# github
todo register an account, send to phil
   https://github.com/heraldia/ImageCR     
    git client
    vscode 

    put github password in ssh
    git clone

    git push -> remote
    git pull -> local
git配置免密登录_讨厌走开啦-CSDN博客_git 免密 {{{2 { 
https://blog.csdn.net/lqlqlq007/article/details/79065095
} 2}}}

# folder structure
literature review => "report" folder
word, .docx
markdown, text

# documentation structure

# target path
https://github.com/heraldia/rse
1. Reverse Image Search 2007 china, // 2020
2. image collection // web scraper/ crawler
3. image comparison // seek identical images. 
    if website, => (un)authorized.
4. categorize
5. identical 

1. protection, precaution
    hidden information
    todo research => report. 
2. solution =================================== 
    source image
    folder contains 1000 images. 

    categorize (animal ->(cat, dog, toy), others), // milestone
    cat subsection -> high resolution comparison.
    signal processing, image processing () -> 2012 computer vision. opensource (github) application level, api.
3. image trace...

图片自动按人分类软件-图片自动按人分文件夹软件下载-西西软件下载 {{{2 { 
https://www.cr173.com/soft/844960.html
    todo seek more 
} 2}}}

按r g b 色彩比重 大体分类
按图片相似度

~\Downloads\
screenshot ~/Downloads/result
pip install -r requirements.txt
to modification

atmosphere.txt
} 2}}}

2020_1127_0829 2nd {{{2 { 
feature vector, user profile
dispatch.py : appetizer
spyder, pycharm, IDE, python3.
github: code repo
--- writing
[dessant/search-by-image: Browser extension for reverse image search, available on Chrome, Firefox and Opera] { good online image
https://chrome.google.com/webstore/detail/search-by-image/cnojnbdhbhnkbcieeekonklommdnndci
chrome extension
https://github.com/dessant/search-by-image
}

[AInoob/NooBox: A Chrome Extension that contains useful tools] {  
A Chrome Extension that contains useful tools https://ainoob.com/project/noobox
https://chrome.google.com/webstore/detail/noobox/kidibbfcblfbbafhnlanccjjdehoahep
https://github.com/AInoob/NooBox
no underlying algo, wrap other rse.
to learn: wrapper, program design.
}

# target path
https://github.com/heraldia/rse    todo 
1. Reverse Image Search 2007 china, // 2020
2. image collection // web scraper/ crawler
3. image comparison // seek identical images. 
    if website, => (un)authorized.
4. categorize *****************
5. identical  *****************

elcorto/imagecluster: Cluster images based on image content using a pre-trained deep neural network, optional time distance scaling and hierarchical clustering. {{{2 { 
https://github.com/elcorto/imagecluster
todo: clone this repo to your computer and run it. NOTE: 
logic part should be under:
<a>
if __name__ == '__main__':
</a>
example: git: ImageCR\imagecluster\example_api_minimal.py

} 2}}}

literatureReview/IMATAG+WhitePaper+(2).pdf todo 
} 2}}}

2020_1205_0839 3rd {{{2 {
# Related Works.
    - to write

    given images -> differ
        color -> b/w
        no b/w -> different apples, differ color pepper
        b/w, item identification, item classification, 
        3 channels,  

    a mother image -> photoshop -> change color/ hue / grey level. -> similar images.
        b/w 

-1. 基于开源算法实现图片比对进行图片全图和局部 比对 - linbin524 - 博客园 {{{3 { 
https://www.cnblogs.com/linbin524/p/9829394.html
} 3}}}
-2. original paper
-3. www.researchgate.net
https://www.researchgate.net/publication/258848394_FREAK_Fast_retina_keypoint
abstract
-4. citations 

fine-granularity 
coarse
- image comparison 

c:\Users\Yunfei Feng\Pictures folder\Saved Pictures\
r"c:\Users\Yunfei Feng\"
        Pictures\Saved Pictures\

        \t tab 
        \n enter
        \b backspace
        \\t
        \\n

        \\'

# a novel keypoint descriptor

} 2}}}

2020_1225_0820 4th {{{2 {
# python environment setting up

# paper structure
                                     =>   Abstract.  Problem statement +  Proposed Method + Conclusions
    meaning                          =>   I. Introduction
    problem statement                =>      -> Problem statement 
    related works / some methods     =>   II. Related Works
                                     =>   III. Proposed Method
                                             -> subsection. algorithm 
                                             -> novelty 
    implement                        =>   IV. Experiments                     
                                             -> Experiments design
                                             -> Experiments environment, cpu, memory, windows10, python 3.8, keras. a paragraph
                                     =>   V. Discussion.
                                             Pros of algorithm.
                                             Comparison to existing algorithms. Table, graph.
                                             metric, [Related Works]
                                             baseline system, benchmark 
                                     =>   VI. Conclusions

Target1: survey paper

<problem statement>
How to trace origins of photos on the internet (camera, copyright, pictures) - Photography -Digital cameras, SLR, lenses, printing, processing, colors, black-and-white, wedding... - City-Data Forum {{{2 { 
http://www.city-data.com/forum/photography/2089944-how-trace-origins-photos-internet.html
} 2}}}
GUIDE: Where was that photo taken? How to locate (almost) any place on Earth | Africa Check {{{2 { 
https://africacheck.org/factsheets/guide-where-was-that-photo-taken-how-to-locate-almost-any-place-on-earth/
} 2}}}
</problem statement>

Target2: similarity
# 傅里叶水印
[阿里根据截图查到泄露者,用的什么黑科技？(数字盲水印) - _海阔天空 - 博客园] ( https://www.cnblogs.com/zkwarrior/p/5980191.html )

linyacool/blind-watermark: Watermark added to the frequency domain by Fourier transform {{{2 { 
https://github.com/linyacool/blind-watermark
    https://www.youtube.com/watch?v=fj5daANrWws    
} 2}}}
An Efficient Image Watermarking Approach based on Fourier Transform
http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.740.412&rep=rep1&type=pdf
fourier watermark

//Target3: tracing
} 2}}}

2021_0108_0827 5th {{{2 {

# Fourier Transform
y = sin(c.x)+ cos(2x)
frequency: c, 2
y -> Fourier(y) -> frequency
ear, eye -> digital
image -> Fourier(image) -> [c,2] -> [c,2,9] -> Fourier watermarking -> image
y = sin(c.x)+ cos(2x) + sin(9x)
time-domain, frequency-domain
frequency-domain: energy higher == time-domain: louder
(amplitude, time, frequency)
encode 加码
decode 解码/译码

# format idea on paper.

# Python improve
## ide tools
spyder, pycharm, vscode, vi. jupyter.

## logic, algo+data structure.

- logic of algo: 
dfs = depth first search, 
bfs = breadth first search. 
s -> b -> s -> h
       -> t -> h
  -> y -> t -> h
       -> s -> h

- logic of code:
l = [[1,5],[2,3]]
l.sort() 
l.sort(key=lambda x:x[0]) 
l.sort(key=lambda x:x[1]) 
l.sort(key=lambda x:x[1], reverse = True) 
l.sort(key=lambda x:x[0]+x[1], reverse = True) 

while
    while 
    while

Target2: similarity

# international paper download
- 外网的论文得用sci hub下  http://sci-hub.wang/?utm_source=wechat_session&utm_medium=social&utm_oi=1013867099994746880

report => Related Works.

http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.740.412&rep=rep1&type=pdf todo

# Frequency_Domain_Watermarking_An_Overview.pdf todo 
    Important sub-disciplines of information hiding are steganography and watermarking.

# category 
- meta-data 元数据
  imagtag
- watermark
- Fourier watermark

# what algorithm does Tineye, google search images. [2021_0108_0931]
How does reverse image search work? {{{2 {  principle
https://www.researchgate.net/post/How-does-reverse-image-search-work
} 2}}}
Keith Price Bibliography Database Indexing Using Color {{{2 { 
http://www.visionbib.com/bibliography/applicat808.html#TT102839
} 2}}}

[2021_0108_0931] + fourier watermark => identical image.

} 2}}}

2021_0115_0817 6th {{{2 {
下周开始写作。
学生口诉论文提纲。
哪些点不明确。
Abstract - last section to write
# plagiarism category

journal 

proceedings
- reverse image search
-- academia: IEEE, ACM, open access.

-- commercial
    --- tineye, google. chrome extension, noobox
-- open source

# Atmosphere 
=> problem

# Technical obstacles
google, color-based 
+++ big data, 
clustering
identify

    => computation complexity
    storage -> data center
    computation -> algorithm
    architecture
    networking

facebook [Needle in a haystack: efficient storage of billions of photos - Facebook Engineering]{ https://engineering.fb.com/2009/04/30/core-data/needle-in-a-haystack-efficient-storage-of-billions-of-photos/ } 
[Beaver.pdf]{ https://www.usenix.org/legacy/event/osdi10/tech/full_papers/Beaver.pdf } 
flickr
pinterest

# algorithm todo
1 pixel line, or shape - circle R with purple color, encoding
decoding - search the shape in the picture.

hash - 1:1
hash function h()
apple watch   - person_a
android phone - person_b

h(a certain image) = uuid
user scenario: a user is searching a certain unique image.
    color-based => reduce searching scope 
        +
    hash function
https://github.com/heraldia/rse
proposed method:
    similarity 
    ssim
    from skimage.measure import compare_ssim as ssim
    Mean Squared Error

    1. Black and white, grey
    2. channel, photoshop, opencv
    import cv2    
    3 / 4 channels
    3. def _resize(imageA, imageB):    
        without crop
        3072*2048 = 3:2
    [1,2] 
    [2,3]
    mse = sqrt(2) 

    target = [[1,2], [2,3]]
    image1 = [[3,5], [5,5]]
    image2 = [[30,50], [5,5]]
    mse = sqrt() 
    4. hash function

} 2}}}

2021_0205_0837 7th {{{2 {
[todo] share me your github account via email 
word
learn latex
http://www.ctex.org/CTeX

Latex template https://github.com/heraldia/Conference-LaTeX-template

git: cmd, vscode

keep adding more related works in your report.
} 2}}}

2021_0306_0812 8th {{{2 {
https://git-scm.com/
git clone ........git

vs code -> extension -> git history, git lens

} 2}}}

9th 2021_0320_0914 {{{2 {
git clone https://github.com/heraldia/Conference-LaTeX-template
    git setup and learn, conflict
} 2}}}

2021_0403_1019 10th {{{2 {
1. research paper website.
    www.researchgate.net/ *********

    https://ieeexplore.ieee.org/Xplore/home.jsp ****
    https://www.acm.org/
    open access
        https://www.elsevier.com/open-access
        https://www.mdpi.com/journal/sensors/history

2. gist extraction

} 2}}}

2021_0612_0930 11th {{{2 {
find no more academic paper

details on any point
读得不明白

I add some documents in the reading folder.
Note: Always "git pull" before editing.

# Examples:
Object Detection in 20 Years: A Survey
Zhengxia Zou (1), Zhenwei Shi (2), Yuhong Guo (3 and 4), Jieping Ye (1 and 4) ((1) University of Michigan, (2) Beihang University, (3) Carleton University, (4) DiDi Chuxing)
https://arxiv.org/abs/1905.05055

Object Tracking: A Survey - CiteSeerX
http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.112.8588&rep=rep1&type=pdf

[ADD] 7. FUTURE DIRECTIONS

draw a timeline history of the progress
nft - latest technique

# Vsp: A Digital Watermark Method For Motion Picture Copyright Protection | IEEE Conference Publication | IEEE Xplore { https://ieeexplore.ieee.org/document/678376
motion picture // -> NFT
    /*
       */
pixel:
MPEG: 
}/

watermark
    - fourier
    - for motion pic

graphviz tool

} 2}}}

2021_0626_0930 12th {{{2 {
timeline history.txt

more reading, presentation or categorization_tree.
image copyright
# ResearchGate { https://www.researchgate.net/search.Search.html?type=publication&query=image%20copyright

} #

# (PDF) Application of Robust Digital Watermarking Technology in Image Copyright Disputes { https://www.researchgate.net/publication/351139707_Application_of_Robust_Digital_Watermarking_Technology_in_Image_Copyright_Disputes
2021_04
good sentences: introduction, related, conclusions.
abstract, conclusions, 
tech1: 1998, DWT, SIFT
tech2: 
// there are also great hidden dangers, such as information replication, forwarding, and even tampering.
Many critical issues related with image copyright in the internet.
duplicated
sharing
edited.

paraphrase
paragraph 
} #
# (PDF) Digital Watermarking: An Overview { https://www.researchgate.net/publication/2262644_Digital_Watermarking_An_Overview
1998_05
} #
# (PDF) Efficient and Effective Image Copyright Enforcement { https://www.researchgate.net/publication/221255899_Efficient_and_Effective_Image_Copyright_Enforcement
good introduction
2005_10
} #
# (PDF) A robust hybrid watermarking scheme based on DCT and SVD for copyright protection of stereo images { https://www.researchgate.net/publication/321114563_A_robust_hybrid_watermarking_scheme_based_on_DCT_and_SVD_for_copyright_protection_of_stereo_images

} #

# (PDF) A Watermarking Framework for Copyright protection of Digital images { https://www.researchgate.net/publication/2628898_A_Watermarking_Framework_for_Copyright_protection_of_Digital_images

} #

叙述故事类型的文章
阐述技术类型的文章

trial1. how to write an essay. 5 papers (including 1 abstract, conclusion, references)
    1. original sentences in others paper, 5 paper. draft
    2. trim draft
    3. 

trial2. orally tell me a story.

trial3. https://github.com/heraldia/rse

} 2}}}

# todo -------------------------------------------------

josephcz.vscode-markdown-mindmap-preview extension
other algo: ho, 横竖在图片里的位置。
to search

# how to speed up encoding, decoding, comparing 
if there is related researches?
approach


