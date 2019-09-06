import json

JSON = 'comics.json'

def first_slide(**comics_json):
    return ('<div class="gallery comic-gallery" itemscope="" itemtype="http://schema.org/ImageGallery">\n'
            '<figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">'
            '<a href="{images[0]}" itemprop="contentUrl" data-size="{size}">'
            '<img style="border: 1px solid black;" src="{images[0]}"/>'
            '</a>'
            '<figcaption itemprop="caption description">'
            '<p><i>{title}</i> by {author}</p>'
            '<p><a href="{amazon}">Amazon</a></p>'
            '</figcaption>'
            '</figure>\n').format(**comics_json)

def slides(**comics_json):
    s = first_slide(**comics_json)
    for i in range(1, len(comics_json["images"])):
        s += ('<figure itemprop="associatedMedia" style="display:none" itemscope itemtype="http://schema.org/ImageObject">'
              '<a href="{img_link}" itemprop="contentUrl" data-size="{size}">'
              '<img src="{img_link}"/>'
              '</a>'
              '<figcaption itemprop="caption description">'
              '</figcaption>'
              '</figure>\n').format(img_link=comics_json["images"][i], **comics_json)
    s += '</div>'
    return s

if __name__ == '__main__':
    with open(JSON) as data_file:
        comics_json = json.load(data_file)
        print(slides(**comics_json))
