import colorgram

colors = colorgram.extract('Damien_Hirst_polkadots.jpg', 24)
rgb_colors = []
first_color = colors[0].rgb

print(first_color)
# for color in colors:
#     rgb_colors.append(color.rgb)
