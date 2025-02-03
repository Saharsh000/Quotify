# new addition
import discord
from utils import random_color

# Expanded dictionary of emotion keywords and their corresponding responses.
emotion_responses = {
    # Positive Emotions
    "happy": "I'm really happy to hear you're feeling happy! Keep shining!",
    "joy": "Your joy is contagious—spread that happiness around!",
    "excited": "Your excitement is inspiring! Enjoy every moment!",
    "thrilled": "It sounds like you're thrilled! Let that energy keep you going!",
    "elated": "Elated vibes are the best vibes. Keep smiling!",

    # Negative Emotions
    "sad": "I'm sorry you're feeling down. Remember, even the darkest night will end and the sun will rise.",
    "depressed": "I know it feels heavy right now. Don't hesitate to talk to someone who cares.",
    "anxious": "It sounds like you're anxious. Take a deep breath, and remember that you're not alone.",
    "worried": "I understand you're worried. Sometimes sharing your thoughts can help ease the burden.",
    "angry": "Anger can be overwhelming. Try taking a moment to breathe deeply.",
    "frustrated": "I know things can be frustrating. Hang in there, and take one step at a time.",

    # Mixed or Overwhelmed Emotions
    "stressed": "Don't forget to take some time for yourself. A little self-care goes a long way!",
    "tired": "It sounds like you're tired. Make sure to get some rest—you deserve it.",
    "exhausted": "Your body and mind need a break. Take some time to recharge.",
    "overwhelmed": "When everything feels too much, take a deep breath. One step at a time is enough.",
    "lonely": "Feeling lonely is tough. Remember, you are important, and there are people who care about you.",
    "bored": "Boredom can be a sign to try something new! Maybe explore a new hobby or take a short break.",
    "confused": "It's okay to feel confused sometimes. Take a moment to reflect, and clarity will come.",
    "disappointed": "Disappointment is part of the journey. Better days are ahead—hang in there!",
    "hopeless": "When hope feels distant, remember that every day brings a new chance to start over.",

    # Additional Emotions
    "melancholy": "Melancholy can be a reflective emotion. Allow yourself time to process and heal.",
    "heartbroken": "I'm sorry you're heartbroken. Healing takes time, and you're not alone in this.",
    "pensive": "Sometimes, being pensive is a sign of deep thought. Just remember to also take time to smile.",
    "insecure": "Feeling insecure can be tough. Remember, you are unique and have so much to offer.",
    "lonely": "Loneliness is hard. Remember that reaching out for a chat can help lighten your day.",
    "despair": "Despair can be overwhelming. If you're feeling this way often, consider talking to someone who understands.",
    "miserable": "I'm sorry you're feeling miserable. Even small steps can help turn things around.",
    "shocked": "It sounds like you're shocked. Take a moment to process, and know that it's okay to feel this way."
}

def register_emotion(bot):
    # Add an event listener for on_message.
    @bot.listen('on_message')
    async def on_message(message: discord.Message):
        # Avoid replying to the bot's own messages.
        if message.author.bot:
            return

        # Convert the message content to lowercase for matching.
        content = message.content.lower()

        # Check each emotion keyword for a match in the message.
        for emotion, response in emotion_responses.items():
            if emotion in content:
                await message.channel.send(embed=discord.Embed(
                    description=response,
                    color=random_color()
                ))
                break  # Stop after the first matching emotion.
