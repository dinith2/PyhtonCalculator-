from PIL import Image, ImageDraw

image_width = 400
image_height = 400
image = Image.new("RGB", (image_width, image_height), "white")
draw = ImageDraw.Draw(image)

head_radius = 80
body_height = 150
leg_height = 150
b
head_center = (image_width // 2, head_radius)
draw.ellipse((head_center[0] - head_radius, head_center[1] - head_radius,
              head_center[0] + head_radius, head_center[1] + head_radius),
             fill="lightblue", outline="black")

body_top = head_center[1] + head_radius
draw.rectangle((head_center[0] - 10, body_top, head_center[0] + 10, body_top + body_height),
               fill="lightblue", outline="black")

# Draw  legs
leg_bottom = body_top + body_height
draw.rectangle((head_center[0] - 30, leg_bottom, head_center[0] - 10, leg_bottom + leg_height),
               fill="lightblue", outline="black")
draw.rectangle((head_center[0] + 10, leg_bottom, head_center[0] + 30, leg_bottom + leg_height),
               fill="lightblue", outline="black")

# Display the image
image.show()