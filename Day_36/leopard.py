# Importing libraries
import streamlit as st
from PIL import Image

# Adding web title
st.title('Leopard, A Sleek Predator')

# Adding image
size_factor = st.slider("Adjust Image Size", 0.1, 2.0, 1.0)
image1 = Image.open('image.jpg')
image1 = image1.resize((int(image1.width * size_factor), int(image1.height * size_factor)))
st.image(image1, caption='Leopard', use_column_width=True)

# Adding story
st.write('''
         In the heart of the untamed savannah, where the tall grasses whispered secrets to the wind, there prowled a sleek predator—the elusive leopard named Zara. Cloaked in a coat of golden rosettes, she moved with the grace of a dancer, leaving the grass to sway in her wake.

Zara was no ordinary feline; she was a master of the art of stealth, an embodiment of the shadows that danced under the moonlight. Her sleek form glided through the night, her eyes gleaming like twin orbs of amber, reflecting the silent determination of a born hunter.

As the sun dipped below the horizon, painting the sky in hues of orange and pink, Zara emerged from her hidden lair. The savannah, bathed in the soft glow of twilight, became her canvas. Her spotted coat merged seamlessly with the golden hues of the grass, rendering her nearly invisible.

The moon, a silent witness to her nocturnal endeavors, cast a silvery glow on the landscape. Zara's ears twitched, attuned to the symphony of the night—the distant calls of other creatures, the rustle of leaves, and the rhythmic beat of her own heart. She was the mistress of this nocturnal ballet.

With sinuous movements, Zara set out on her silent prowl. Her padded paws made no sound as she navigated the terrain, her eyes fixed on the distant flicker of movement—a herd of unsuspecting impalas grazing under the moon's gentle gaze.

In the blink of an eye, Zara launched into action. A blur of spotted elegance, she closed the gap between predator and prey with breathtaking speed. The impalas, sensing a shadow in their midst, stirred with alarm, but it was too late. Zara's powerful jaws closed around her chosen target, and the dance of life and death unfolded in the moonlit theater of the savannah.

With the grace of a consummate performer, Zara fed on her catch, savoring the taste of the hunt. She was a sleek predator, a creature perfectly adapted to the rhythm of the night. As the moon continued its journey across the sky, Zara melted back into the shadows, leaving only the echo of her presence and the memory of a dance in the heart of the untamed wilderness.''')

# Adding Video
video1 = open('video.mp4', 'rb')
st.video(video1)


# # Add Audio
# audio1 = open('audio.mp3', 'rb')
# st.audio(audio1)
