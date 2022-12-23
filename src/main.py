import qrcode


I = input("Type in the url which you want to visit: ")  #write your url here
print("Your QRCode is One Step To Be Saved!:", I)  #This messages shows that the QR Code has been downloaded ans saved


def generate(data, img_name=(input('Enter Desired Filename With Extension, e.g. qrCode.png: '))):

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