import string
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LYRICS_FOLDER = os.path.join(BASE_DIR, "lyrics")

def clean_text(text):
    text = text.lower()

    cleaned_text = ""
    for char in text:
        if char not in string.punctuation:
            cleaned_text += char
    
    return cleaned_text

def get_words(text):
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    return words

def count_words(words):
    word_counts = {}

    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1

    return word_counts

def get_top_words(word_counts, number_of_words):
    word_list = list(word_counts.items())

    word_list.sort(key=get_count, reverse=True)

    return word_list[:number_of_words]

def get_count(item):
    return item[1]

def get_top_words(word_counts, number_of_words):
    word_list = list(word_counts.items())
    word_list.sort(key=get_count, reverse=True)
    return word_list[:number_of_words]

def count_energy_words(words):
    high_energy_words = ["dance", "party", "club", "night", "jump", "move", "fire", "wild", "fast", "shake", "bass", "drop"]
    low_energy_words = ["love", "alone", "cry", "slow", "dream", "heart", "sad", "miss", "feel", "soft", "broken", "calm", "lonely", "empty", "cold", "lost", "need", "without"]

    high_count = 0
    low_count = 0

    for word in words:
        if word in high_energy_words:
            high_count += 1

        if word in low_energy_words:
            low_count += 1
    
    return high_count, low_count

def get_energy_label(high_count, low_count):
    total = high_count + low_count

    if total == 0:
        return "Balanced Energy"
    
    high_ratio = high_count / total

    if high_ratio > 0.75:
        return "High Energy"
    elif high_ratio >= 0.45:
        return "Transition Song"
    else:
        return "Low Energy"

def get_theme_scores(words):
    themes = {
        "Nightlife": ["night", "club", "party", "dance", "lights", "city", "neon"],
        "Romance": ["love", "heart", "kiss", "baby", "together", "feel"],
        "Heartbreak": ["cry", "alone", "miss", "broken", "sad", "lost", "without"],
        "Confidence": ["fire", "strong", "power", "bulletproof", "loud", "wild"],
        "Energy": ["run", "move", "fast", "jump", "shake", "drop"]
    }

    theme_scores = {}

    for theme in themes:
        theme_scores[theme] = 0

        for word in words:
            if word in themes[theme]:
                theme_scores[theme] += 1

    return theme_scores

def get_main_theme(theme_scores):
    highest_theme = "Unknown"
    highest_score = 0

    for theme in theme_scores:
        if theme_scores[theme] > highest_score:
            highest_theme = theme
            highest_score = theme_scores[theme]

    if highest_score == 0:
        return "No Clear Theme"
    
    return highest_theme

def read_file(filename):
    path = os.path.join(LYRICS_FOLDER, filename)

    file = open(path, "r", encoding="utf-8")
    text = file.read()
    file.close()
    
    return text

def format_song_name(filename):
    name = filename.replace(".txt", "")
    name = name.replace("_", " ")
    name = name.title()
    return name

def analyze_song(filename):
    text = read_file(filename)
    words = get_words(text)
    word_counts = count_words(words)

    high_count, low_count = count_energy_words(words)
    energy_label = get_energy_label(high_count, low_count)
    theme_scores = get_theme_scores(words)
    main_theme = get_main_theme(theme_scores)

    print("=" * 50)
    print("Song:", format_song_name(filename))
    print("Total words:", len(words))
    print("Unique words:", len(word_counts))
    print("High energy word count:", high_count)
    print("Low energy word count:", low_count)
    print("Energy label:", energy_label)
    print("Main Theme:", main_theme)

    print("\nTop 10 words:")
    top_words = get_top_words(word_counts, 10)

    for word, count in top_words:
        print(word, ":", count)

def get_song_word_set(filename):
    text = read_file(filename)
    words = get_words(text)
    word_set = set(words)
    return word_set

def get_song_profile(filename):
    text = read_file(filename)
    words = get_words(text)

    word_set = set(words)

    high_count, low_count = count_energy_words(words)
    energy_label = get_energy_label(high_count, low_count)

    theme_scores = get_theme_scores(words)
    main_theme = get_main_theme(theme_scores)

    profile = {
        "filename": filename,
        "words": words,
        "word_set": word_set,
        "energy": energy_label,
        "theme": main_theme
    }

    return profile

def compare_songs(filename1, filename2):
    song1 = get_song_profile(filename1)
    song2 = get_song_profile(filename2)

    words1 = song1["word_set"]
    words2 = song2["word_set"]

    shared_words = words1 & words2
    all_words = words1 | words2

    if len(all_words) == 0:
        word_similarity = 0
    else:
        word_similarity = len(shared_words) / len(all_words)

    word_percentage = word_similarity * 100

    compatibility_score = 0

    if word_percentage >= 10:
        compatibility_score += 3
    elif word_percentage >= 5:
        compatibility_score += 2
    elif word_percentage > 0:
        compatibility_score += 1

    if song1["energy"] == song2["energy"]:
        compatibility_score += 3
    elif song1["energy"] == "Transition Song" or song2["energy"] == "Transition Song":
        compatibility_score += 2
    else:
        compatibility_score += 1

    if song1["theme"] == song2["theme"]:
        compatibility_score += 3
    elif song1["theme"] != "No Clear Theme" and song2["theme"] != "No Clear Theme":
        compatibility_score += 2
    else:
        compatibility_score += 1

    print("=" * 50)
    print("Smart Song Comparison")
    print("=" * 50)

    print("Song 1:", format_song_name(filename1))
    print("Energy:", song1["energy"])
    print("Theme:", song1["theme"])

    print()

    print("Song 2:", format_song_name(filename2))
    print("Energy:", song2["energy"])
    print("Theme:", song2["theme"])

    print()

    print("Shared Unique Words:", len(shared_words))
    print("Word Similarity:", round(word_percentage, 2), "%")
    print("Compatibility Score:", compatibility_score, "out of 9")

    print("\nSample Shared Words:")
    shared_word_list = list(shared_words)
    shared_word_list.sort()

    for word in shared_word_list[:15]:
        print("-", word)

    print("\nRecommendation:")

    if compatibility_score >= 7:
        print("Strong DJ Pairing --> songs would work well in the same deck.")
    elif compatibility_score >= 5:
        print("Moderate DJ Pairing --> songs could work as transitions.")
    else:
        print("Weak DJ Pairing --> songs do not work well together.")

def suggest_deck_order(song_files):
    profiles = []

    for filename in song_files:
        profile = get_song_profile(filename)
        profiles.append(profile)

    high_energy = []
    transition = []
    low_energy = []
    neutral = []

    for profile in profiles:
        if profile["energy"] == "High Energy":
            high_energy.append(profile)
        elif profile["energy"] == "Transition Song":
            transition.append(profile)
        elif profile["energy"] == "Low Energy":
            low_energy.append(profile)
        else:
            neutral.append(profile)

    deck_order = high_energy + transition + neutral + low_energy

    print("=" * 60)
    print("Suggested DJ Deck Order")
    print("=" * 60)

    for i in range(len(deck_order)):
        profile = deck_order[i]

        print(str(i + 1) + ".", format_song_name(profile["filename"]))
        print(" Energy:", profile["energy"])
        print(" Theme:", profile["theme"])

        if profile["energy"] == "High Energy":
            print(" Reason: Good for building excitment and momentum.")
        elif profile["energy"] == "Transition Song":
            print(" Reason: Useful for connecting different moods.")
        elif profile["energy"] == "Low Energy":
            print(" Reason: Better for end of the deck.")
        else:
            print(" Reason: Can be used flexibly depending on the mood of your set.")

        print()

def main():
    print("=" * 60)
    print("DJ Lyric Deck Analyzer")
    print("=" * 60)

    song_files = []

    for filename in os.listdir(LYRICS_FOLDER):
        if filename.endswith(".txt"):
            song_files.append(filename)

    if len(song_files) == 0:
        print("No lyric files found in the lyrics folder.")
        return
    
    print("\nSong Analysis")
    print("-" * 60)

    for filename in song_files:
        analyze_song(filename)
        print()
    
    print("=" * 60)
    print("Pairwise Based on Song Comparison")
    print("=" * 60)

    for i in range(len(song_files)):
        for j in range(i + 1, len(song_files)):
            compare_songs(song_files[i], song_files[j])
            print()

    print()
    suggest_deck_order(song_files)

main()