from bs4 import BeautifulSoup
import urllib.request

html = '<div data-test="carousel-viewer-wrap" radius="0" class="css-114r11c"><div class="css-q4ks6l" data-test="carousel"><div data-test="carousel-wrapper" spacing="0" class="css-11mzas3"><div data-test="carousel-inner-wrapper" spacing="0" class="css-6txkg3"><div data-test="carousel-item-0" class="css-15xv5ui"><div data-test="slide-item-wrap" spacing="0" width="491px" height="491px" class="css-1i8w078"><button type="button" class="assetWrapper css-nyt3ir" tabindex="-1" data-index="0" data-test="0" width="491" height="491" aria-label="Gallery asset 1 of 13"><div data-test="image-wrap" class="css-1bgzf1l" data-ready="true"><div relative="true" data-test="img-zoom-wrap" class="css-1bn8s1b"><img itemprop="image" draggable="false" src="https://res.garmin.com/transform/image/upload/b_rgb:FFFFFF,c_pad,dpr_1.0,f_auto,h_500,q_auto,w_500/c_pad,h_500,w_500/v1/Product_Images/en/products/010-02582-21/v/cf-xl-cc59b8c4-e2e8-4b10-9331-71f936c87ffc?pgw=1" class="css-fwsz2x" alt="Gallery asset 1 of 13" width="491" height="491"><div data-test="zoom-wrap" class="css-14btltm"><div data-test="zoom-trigger" style="cursor: zoom-in;" class="css-qpv74m"></div></div></div></div></button></div></div><div data-test="carousel-item-1" class="css-15xv5ui"><div data-test="slide-item-wrap" spacing="0" width="491px" height="491px" class="css-1i8w078"><button type="button" class="assetWrapper css-nyt3ir" tabindex="-1" data-index="0" data-test="0" width="491" height="491" aria-label="Gallery asset 2 of 13"><div data-test="image-wrap" class="css-1bgzf1l" data-ready="true"><div relative="true" data-test="img-zoom-wrap" class="css-1bn8s1b"><img itemprop="image" draggable="false" src="https://res.garmin.com/transform/image/upload/b_rgb:FFFFFF,c_pad,dpr_1.0,f_auto,h_500,q_auto,w_500/c_pad,h_500,w_500/v1/Product_Images/en/products/010-02582-21/v/pd-01-xl-29d700d2-7b1c-46b1-8931-3dd11a6c701f?pgw=1" class="css-fwsz2x" alt="Gallery asset 2 of 13" width="491" height="491"></div></div></button></div></div><div data-test="carousel-item-2" class="css-15xv5ui"><div data-test="slide-item-wrap" spacing="0" width="491px" height="491px" class="css-1i8w078"><button type="button" class="assetWrapper css-nyt3ir" tabindex="-1" data-index="0" data-test="0" width="491" height="491" aria-label="Gallery asset 3 of 13"><div data-test="image-wrap" class="css-1bgzf1l" data-ready="true"><div relative="true" data-test="img-zoom-wrap" class="css-1bn8s1b"><img itemprop="image" draggable="false" src="https://res.garmin.com/transform/image/upload/b_rgb:FFFFFF,c_pad,dpr_1.0,f_auto,h_500,q_auto,w_500/c_pad,h_500,w_500/v1/Product_Images/en/products/010-02582-21/v/pd-02-xl-39c7e083-522d-4c31-aa8b-bdb2c107c788?pgw=1" class="css-fwsz2x" alt="Gallery asset 3 of 13" width="491" height="491"></div></div></button></div></div><div data-test="carousel-item-3" class="css-15xv5ui"><div data-test="slide-item-wrap" spacing="0" width="491px" height="491px" class="css-1i8w078"><button type="button" class="assetWrapper css-nyt3ir" tabindex="-1" data-index="0" data-test="0" width="491" height="491" aria-label="Gallery asset 4 of 13"><div data-test="image-wrap" class="css-1bgzf1l" data-ready="true"><div relative="true" data-test="img-zoom-wrap" class="css-1bn8s1b"><img itemprop="image" draggable="false" src="https://res.garmin.com/transform/image/upload/b_rgb:FFFFFF,c_pad,dpr_1.0,f_auto,h_500,q_auto,w_500/c_pad,h_500,w_500/v1/Product_Images/en/products/010-02582-21/v/pd-03-xl-1a996b5d-40b1-4f65-b062-07e0465c33c3?pgw=1" class="css-fwsz2x" alt="Gallery asset 4 of 13" width="491" height="491"></div></div></button></div></div><div data-test="carousel-item-4" class="css-15xv5ui"><div data-test="slide-item-wrap" spacing="0" width="491px" height="491px" class="css-1i8w078"><button type="button" class="assetWrapper css-nyt3ir" tabindex="-1" data-index="0" data-test="0" width="491" height="491" aria-label="Gallery asset 5 of 13"><div data-test="image-wrap" class="css-1bgzf1l" data-ready="true"><div relative="true" data-test="img-zoom-wrap" class="css-1bn8s1b"><img itemprop="image" draggable="false" src="https://res.garmin.com/transform/image/upload/b_rgb:FFFFFF,c_pad,dpr_1.0,f_auto,h_500,q_auto,w_500/c_pad,h_500,w_500/v1/Product_Images/en/products/010-02582-21/v/pd-04-xl-0ab7e16b-1abf-44d7-8f6d-1704b01f7e7c?pgw=1" class="css-fwsz2x" alt="Gallery asset 5 of 13" width="491" height="491"></div></div></button></div></div><div data-test="carousel-item-5" class="css-15xv5ui"><div data-test="slide-item-wrap" spacing="0" width="491px" height="491px" class="css-1i8w078"><button type="button" class="assetWrapper css-nyt3ir" tabindex="-1" data-index="0" data-test="0" width="491" height="491" aria-label="Gallery asset 6 of 13"><div data-test="image-wrap" class="css-1bgzf1l" data-ready="true"><div relative="true" data-test="img-zoom-wrap" class="css-1bn8s1b"><img itemprop="image" draggable="false" src="https://res.garmin.com/transform/image/upload/b_rgb:FFFFFF,c_pad,dpr_1.0,f_auto,h_500,q_auto,w_500/c_pad,h_500,w_500/v1/Product_Images/en/products/010-02582-21/v/pd-05-xl-c5ecbe75-c760-4507-939e-6d498b5304ee?pgw=1" class="css-fwsz2x" alt="Gallery asset 6 of 13" width="491" height="491"></div></div></button></div></div><div data-test="carousel-item-6" class="css-15xv5ui"><div data-test="slide-item-wrap" spacing="0" width="491px" height="491px" class="css-1i8w078"><button type="button" class="assetWrapper css-nyt3ir" tabindex="-1" data-index="0" data-test="0" width="491" height="491" aria-label="Gallery asset 7 of 13"><div data-test="image-wrap" class="css-1bgzf1l" data-ready="true"><div relative="true" data-test="img-zoom-wrap" class="css-1bn8s1b"><img itemprop="image" draggable="false" src="https://res.garmin.com/transform/image/upload/b_rgb:FFFFFF,c_pad,dpr_1.0,f_auto,h_500,q_auto,w_500/c_pad,h_500,w_500/v1/Product_Images/en/products/010-02582-21/v/sc-01-xl-fa220418-7527-4ac1-8649-3113a5f7ac11?pgw=1" class="css-fwsz2x" alt="Gallery asset 7 of 13" width="491" height="491"></div></div></button></div></div><div data-test="carousel-item-7" class="css-15xv5ui"><div data-test="slide-item-wrap" spacing="0" width="491px" height="491px" class="css-1i8w078"><button type="button" class="assetWrapper css-nyt3ir" tabindex="-1" data-index="0" data-test="0" width="491" height="491" aria-label="Gallery asset 8 of 13"><div data-test="image-wrap" class="css-1bgzf1l" data-ready="true"><div relative="true" data-test="img-zoom-wrap" class="css-1bn8s1b"><img itemprop="image" draggable="false" src="https://res.garmin.com/transform/image/upload/b_rgb:FFFFFF,c_pad,dpr_1.0,f_auto,h_500,q_auto,w_500/c_pad,h_500,w_500/v1/Product_Images/en/products/010-02582-21/v/sc-02-xl-142b88df-aaa7-4cb3-b48e-f927af1255c5?pgw=1" class="css-fwsz2x" alt="Gallery asset 8 of 13" width="491" height="491"></div></div></button></div></div><div data-test="carousel-item-8" class="css-15xv5ui"><div data-test="slide-item-wrap" spacing="0" width="491px" height="491px" class="css-1i8w078"><button type="button" class="assetWrapper css-nyt3ir" tabindex="-1" data-index="0" data-test="0" width="491" height="491" aria-label="Gallery asset 9 of 13"><div data-test="image-wrap" class="css-1bgzf1l" data-ready="true"><div relative="true" data-test="img-zoom-wrap" class="css-1bn8s1b"><img itemprop="image" draggable="false" src="https://res.garmin.com/transform/image/upload/b_rgb:FFFFFF,c_pad,dpr_1.0,f_auto,h_500,q_auto,w_500/c_pad,h_500,w_500/v1/Product_Images/en/products/010-02582-21/v/sc-03-xl-e6f25b7c-ff0b-462d-875b-5b64e78d03d7?pgw=1" class="css-fwsz2x" alt="Gallery asset 9 of 13" width="491" height="491"></div></div></button></div></div><div data-test="carousel-item-9" class="css-15xv5ui"><div data-test="slide-item-wrap" spacing="0" width="491px" height="491px" class="css-1i8w078"><button type="button" class="assetWrapper css-nyt3ir" tabindex="-1" data-index="0" data-test="0" width="491" height="491" aria-label="Gallery asset 10 of 13"><div data-test="image-wrap" class="css-1bgzf1l" data-ready="true"><div relative="true" data-test="img-zoom-wrap" class="css-1bn8s1b"><img itemprop="image" draggable="false" src="https://res.garmin.com/transform/image/upload/b_rgb:FFFFFF,c_pad,dpr_1.0,f_auto,h_500,q_auto,w_500/c_pad,h_500,w_500/v1/Product_Images/en/products/010-02582-21/v/sc-04-xl-0fb3ff31-8f74-46c0-9ef9-c01aca9d0bc0?pgw=1" class="css-fwsz2x" alt="Gallery asset 10 of 13" width="491" height="491"></div></div></button></div></div><div data-test="carousel-item-10" class="css-15xv5ui"><div data-test="slide-item-wrap" spacing="0" width="491px" height="491px" class="css-1i8w078"><button type="button" class="assetWrapper css-nyt3ir" tabindex="-1" data-index="0" data-test="0" width="491" height="491" aria-label="Gallery asset 11 of 13"><div data-test="image-wrap" class="css-1bgzf1l" data-ready="true"><div relative="true" data-test="img-zoom-wrap" class="css-1bn8s1b"><img itemprop="image" draggable="false" src="https://res.garmin.com/transform/image/upload/b_rgb:FFFFFF,c_pad,dpr_1.0,f_auto,h_500,q_auto,w_500/c_pad,h_500,w_500/v1/Product_Images/en/products/010-02582-21/v/sc-05-xl-38fbf9ee-43f1-4a6b-8b9f-c2d25c0fe0d4?pgw=1" class="css-fwsz2x" alt="Gallery asset 11 of 13" width="491" height="491"></div></div></button></div></div><div data-test="carousel-item-11" class="css-15xv5ui"><div data-test="slide-item-wrap" spacing="0" width="491px" height="491px" class="css-1i8w078"><button type="button" class="assetWrapper css-nyt3ir" tabindex="-1" data-index="0" data-test="0" width="491" height="491" aria-label="Gallery asset 12 of 13"><div data-test="image-wrap" class="css-1bgzf1l" data-ready="true"><div relative="true" data-test="img-zoom-wrap" class="css-1bn8s1b"><img itemprop="image" draggable="false" src="https://res.garmin.com/transform/image/upload/b_rgb:FFFFFF,c_pad,dpr_1.0,f_auto,h_500,q_auto,w_500/c_pad,h_500,w_500/v1/Product_Images/en/products/010-02582-21/v/sc-06-xl-8221e144-c9b2-4675-8eb4-f6c90180c523?pgw=1" class="css-fwsz2x" alt="Gallery asset 12 of 13" width="491" height="491"></div></div></button></div></div><div data-test="carousel-item-12" class="css-15xv5ui"><div data-test="slide-item-wrap" spacing="0" width="491px" height="491px" class="css-1i8w078"><button type="button" class="assetWrapper css-nyt3ir" tabindex="-1" data-index="0" data-test="0" width="491" height="491" aria-label="Gallery asset 13 of 13"><div data-test="image-wrap" class="css-1bgzf1l" data-ready="true"><div relative="true" data-test="img-zoom-wrap" class="css-1bn8s1b"><img itemprop="image" draggable="false" src="https://res.garmin.com/transform/image/upload/b_rgb:FFFFFF,c_pad,dpr_1.0,f_auto,h_500,q_auto,w_500/c_pad,h_500,w_500/v1/Product_Images/en/products/010-02582-21/v/sc-07-xl-b8ef6695-1632-429c-af8b-659221f79702?pgw=1" class="css-fwsz2x" alt="Gallery asset 13 of 13" width="491" height="491"></div></div></button></div></div></div></div></div><button type="button" shape="none" color="#FFFFFF" size="54" class="css-7a26vr" offset="0" direction="right" aria-label="Next" data-test="nav-next"><svg data-test="svg-image" class="css-1p2w2m3" viewBox="0 0 24 24" preserveAspectRatio="xMidYMid"><path d="M8.59,16.59L13.17,12L8.59,7.41L10,6l6,6l-6,6L8.59,16.59z"></path></svg></button></div>'

soup = BeautifulSoup(html, 'html.parser')
img_tags = soup.find_all('img')
for i, img_tag in enumerate(img_tags):
    src = img_tag['src']
    new_src = src.replace('h_500', 'h_1000').replace(
        'w_500', 'w_1000').replace('f_auto', 'f_jpg').replace('q_auto', 'q_100')
    filename = str(i+1) + '.jpg'
    with urllib.request.urlopen(new_src) as url:
        with open(filename, 'wb') as f:
            f.write(url.read())
