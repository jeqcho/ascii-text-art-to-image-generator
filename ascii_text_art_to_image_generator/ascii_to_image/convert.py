from PIL import Image
import io


def convert_ascii_to_image(ascii_content, ramp_choice=0):
    ascii_content = ascii_content.split('\n')

    # 70 levels of gray
    gray_ramps = [
        "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. ",
        '@%#*+=-:. ',
        "@&%#(/*,. "
    ]
    # an array of arrays holding the luminosity of a tile (ie pixel)
    gray_ramp = gray_ramps[ramp_choice]
    num_rows = len(ascii_content)
    num_cols = max([len(row) for row in ascii_content])
    img_data = []
    for idx, row in enumerate(ascii_content):
        img_data.append([])
        for char in row:
            try:
                img_data[idx].append(gray_ramp.index(char)*255/len(gray_ramp))
            except ValueError:
                img_data[idx].append(255)

    tile_width = 7
    scale = 0.43
    tile_height = int(tile_width / scale)
    width = num_cols*tile_width
    height = num_rows*tile_height
    im = Image.new('L', (width, height))
    pix = im.load()
    # pix[col,row]
    for row_idx, row in enumerate(img_data):
        for col_idx, luminosity in enumerate(row):
            for i in range(tile_height):
                for j in range(tile_width):
                    pix[col_idx*tile_width+j, row_idx*tile_height+i] = int(luminosity)

    b = io.BytesIO()
    im.save(b, "PNG")
    return b
