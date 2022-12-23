import qrcode


I = input("Type in the url which you want to visit: ")  #write your url here
print("Your QRCode is now Saved!:", I)


def generate(data, img_name="qrCode.png"):

    """_summary_

    Args:
        data (_type_): _description_
        img_name (str, optional): _description_. Defaults to "qrCode.png".

    Returns:
        _type_: _description_
    """

    img = qrcode.make(data)
    img.save(img_name)
    return img

generate(I)