my_str = """**AITA for Feeding My Neighbors' Cat While They Went on a Spa Day?**

Every Saturday morning like clockwork, my neighbors head out for their weekly spa day, leaving their cat, Mr. Whiskers, alone in their lavish apartment. I noticed Mr. Whiskers eyeing me longingly from their window, his plaintive meows tugging at my heartstrings like a feline siren's song.

Unable to resist the call of the meows, I took it upon myself to drop by, armed with a key they'd given me long ago for emergencies. I couldn't bear to see poor Mr. Whiskers pining for attention and food. So, I began to regularly pop in to check on him and ensure his food bowl was never empty, all while enjoying the pleasure of his purring company.

However, the plot thickened when my neighbors unexpectedly returned home early one fateful day. Caught red-handed in the act of providing unauthorized cat-sitting services, I was met with a considerable amount of shock and suspicion.

My neighbors, perplexed and slightly amused, demanded an explanation for my covert cat care. As I stumbled over my words, attempting to justify my actions with an awkward mix of guilt and goodwill, the tension in the air became palpable.

They couldn't comprehend why I, a neighbor with zero formal pet-sitting agreement, felt entitled to tend to Mr. Whiskers in their absence. I, on the other hand, argued that my impromptu caregiving sessions were an act of true compassion and neighborly camaraderie.

After some back-and-forth, my neighbors were torn between laughter at the bizarre situation and a lingering unease at my unsanctioned involvement in their cat's well-being. Ultimately, they accepted my apology but made it explicitly clear that future spa days would not require any unauthorized cat-sitting interventions.

Reflecting on the absurdity of the situation, I couldn't help but wonder: am I the asshole for feeding Mr. Whiskers behind my neighbors' backs, albeit with the best of intentions? Or was my unexpected foray into impromptu pet care simply a case of misunderstood neighborly goodwill?"""

from gtts import gTTS
from pydub import AudioSegment

tts_obj = gTTS(text = my_str, lang='en', slow=False)
tts_obj.save("test.mp3")

audio = AudioSegment.from_mp3("test.mp3")

def change_speed(sound, speed=1.0):
    # Speed up the audio without changing pitch
    sound_stretched = sound.speedup(playback_speed=speed)

    return sound_stretched

# Change speed without changing pitch (1.5x speed)
faster_audio = change_speed(audio, speed=1.25)

# Export the modified audio to a new MP3 file
faster_audio.export("test_faster.mp3", format="mp3")
