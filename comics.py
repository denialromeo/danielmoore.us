import json

from PIL import Image

JSON = 'comics.json'

def get_dim(img):
    im = Image.open(img);
    return f"{im.size[0]}x{im.size[1]}"

def first_slide(page):
    return ('<div class="gallery comic-gallery" itemscope="" itemtype="http://schema.org/ImageGallery">\n'
            '<figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">'
            '<a href="{img_link}" itemprop="contentUrl" data-size="{dim}">'
            '<img style="border: 1px solid black;" src="{img_link}"/>'
            '</a>'
            '<figcaption itemprop="caption description">'
            '<p><i>{title}</i> by {author}</p>'
            # '<p><a href="{amazon}">Amazon</a></p>'
            '</figcaption>'
            '</figure>\n').format(dim=get_dim(page["link"]), img_link='/' + page["link"], **page)

def slides(comics_json):
    s = first_slide(comics_json["pages"][0])
    for i in range(1, len(comics_json["pages"])):
        s += ('<figure itemprop="associatedMedia" style="display:none" itemscope itemtype="http://schema.org/ImageObject">'
              '<a href="{img_link}" itemprop="contentUrl" data-size="{dim}">'
              '<img src="{img_link}"/>'
              '</a>'
              '<figcaption itemprop="caption description">'
              '<p><i>{title}</i> by {author}</p>'
              # '<p><a href="{amazon}">Amazon</a></p>'
              '</figcaption>'
              '</figure>\n').format(img_link='/' + comics_json["pages"][i]["link"], dim=get_dim(comics_json["pages"][i]["link"]), **(comics_json["pages"][i]))
    s += '</div>'
    return s

if __name__ == '__main__':
    with open(JSON) as data_file:
        comics_json = json.load(data_file)
        print(slides(comics_json))