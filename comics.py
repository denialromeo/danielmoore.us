import json
import os

from PIL import Image

DIR = 'assets/img/comics/sandman-loki'
TITLE = 'The Sandman'
AUTHOR = 'Neil Gaiman'

def get_dim(img):
    im = Image.open(img);
    return f"{im.size[0]}x{im.size[1]}"

def first_slide(img_link, title, author):
    return ('<div class="gallery comic-gallery" itemscope="" itemtype="http://schema.org/ImageGallery">\n'
            '<figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">'
            f'<a href="{img_link}" itemprop="contentUrl" data-size="{get_dim(img_link)}">'
            f'<img style="border: 1px solid black;" src="{img_link}"/>'
            '</a>'
            '<figcaption itemprop="caption description">'
            f'<p><i>{title}</i> by {author}</p>'
            '</figcaption>'
            '</figure>\n')

def slides(directory, title, author):
    imgs = [directory + '/' + f for f in os.listdir(directory)]
    s = first_slide(imgs[0], title, author)
    for img_link in imgs[1:]:
        s += ('<figure itemprop="associatedMedia" style="display:none" itemscope itemtype="http://schema.org/ImageObject">'
              f'<a href="{img_link}" itemprop="contentUrl" data-size="{get_dim(img_link)}">'
              f'<img src="{img_link}"/>'
              '</a>'
              '</figcaption>'
              '</figure>\n')
    s += '</div>'
    return s

if __name__ == '__main__':
    print(slides(DIR, TITLE, AUTHOR))