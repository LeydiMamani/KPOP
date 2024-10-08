from googletrans import Translator

# Crear una instancia del traductor
translator = Translator()

# Texto a traducir
text = """
Emily and Harry were sitting in the park. They have seen each other there a few times before. Harry looked at Emily and said, “Hi Emily!”. “Oh, hello Harry!” she replied. “It is nice to meet you”, said Harry.
“It is nice to meet you too, Harry. How are you today?”
“I am good, thank you! How are you?”
“Great thanks. How old are you, Harry?” – Emily asked – “I am 21 years old. How old are you?”
“I am 70 years old; I am ancient haha.” She replied laughing. “You are not ancient! You are probably very wise.” Said Harry – “Yes, I am. Old people are very wise!” Emily replied.
“Yes, that’s true! My grandfather is very old and very wise. He always gives me good advice if I have a problem.” He said.
Emily saw a stroller next to Harry and asked: “That’s nice. Who is this?”. “This is Josh, he is a baby. We are brothers.” He replied.
“He is a very cute baby. How old is he?”
“He is 2 years old.”. Then Emily said: “He is an adorable baby!”
"""

# Traducir el texto al español
translated_text = translator.translate(text, src='en', dest='es').text

# Mostrar el texto traducido
print(translated_text)
