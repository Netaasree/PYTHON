width = input("Flag width:\n")
width = int(width)
height = input("Flag height:\n")
height = int(height)
half_width = int(width / 2)
half_height = int(height / 2)
upper_row = '#' * half_width + '-' * half_width + '\n'
lower_row = '-' * width + '\n'
print(upper_row * half_height, end='')
print(lower_row * half_height, end='')

