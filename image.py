from PIL import Image, ImageDraw, ImageFont
import textwrap
imageSize = (800, 450)
fontSize = 35
textOffset = (25, 25)
backgroundColour = "white"
albumCoverSize = (400, 400)


def generateImage(songName: str, artistName: str, albumName: str):
    img = Image.new('RGB', imageSize, color=backgroundColour)
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype("Gotham-Font/GothamMedium.ttf", fontSize)
    textToWrite = [textwrap.wrap(i, width=550//fontSize)
                   for i in [songName, artistName, albumName]]
    textToWrite = sum(textToWrite, [])

    d.multiline_text(textOffset, "\n".join(
        textToWrite), font=font, fill=(0, 0, 0))
    albumCover = Image.open("testAlbumCover.jpg").resize(albumCoverSize)
    albumOffset = (img.height-albumCover.height)//2
    img.paste(albumCover, (img.width-albumCover.width-albumOffset, albumOffset))
    img.save('outputImage.png')


generateImage("Blade", "Karma", "Anger Management")


def getImage(token: str, layout="compact"):
    pass
