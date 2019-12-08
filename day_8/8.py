from colorama import Fore


def count_digit(data, digit):
    return data.count(digit)


def find_layer_with_least_0(layers):
    layer_indices_with_count = [(index, count_digit(layer, '0')) for index, layer in enumerate(layers)]
    return layers[min(layer_indices_with_count, key=lambda item: item[1])[0]]


def get_layers(data: str, width, height):
    layer_size = (width * height)
    layer_count = len(data) // layer_size

    layers = []
    for i in range(layer_count):
        layers.append(data[i*layer_size:i*layer_size + layer_size])

    return layers


def decode_image(layers, width, height):
    image = [ [ 2 for i in range(width) ] for j in range(height) ]

    for layer in reversed(layers):
        for y in range(height):
            for x in range(width):
                color = layer[y * width + x]
                if color != '2':
                    image[y][x] = color

    return image


def print_image(image, width, height):
    for y in range(height):
        line = ""
        for x in range(width):
            color = image[y][x]
            if color == '2':
                line += " "
            elif color == '1':
                line += f"{Fore.WHITE}\u2588"
            elif color == '0':
                line += f"{Fore.BLACK}\u2588"

        print(line)


if __name__ == '__main__':
    print(decode_image(get_layers("0222112222120000", 2, 2), 2, 2))

    input = open("8_input.txt", 'r').readline()
    width = 25
    height = 6

    layers = get_layers(input, width, height)

    least_0 = find_layer_with_least_0(layers)
    print(count_digit(least_0, '1') * count_digit(least_0, '2'))

    print_image(decode_image(layers, width, height), width, height)
