def is_pic(pic_name):
    ext_name = ['jpeg', 'jpg', 'png', 'bmp']
    if pic_name.split('.')[-1] in ext_name:
        return True
    return False
