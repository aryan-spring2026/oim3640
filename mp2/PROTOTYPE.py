import string

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

def read_file(filename):
    path = "lyrics/" + filename

    file = open(path, "r", encoding="utf-8")
    text = file.read()
    file.close()
    
    return text

def analyze_song(filename):
    text = read_file(filename)
    words = get_words(text)
    word_counts = count_words(words)

    high_count, low_count = count_energy_words(words)
    energy_label = get_energy_label(high_count, low_count)

    print("=" * 50)
    print("Song file:", filename)
    print("Total words:", len(words))
    print("Unique words:", len(word_counts))
    print("High energy word count:", high_count)
    print("Low energy word count:", low_count)
    print("Energy label:", energy_label)

    print("\nTop 10 words:")
    top_words = get_top_words(word_counts, 10)

    for word, count in top_words:
        print(word, ":", count)

def get_song_word_set(filename):
    text = read_file(filename)
    words = get_words(text)
    word_set = set(words)
    return word_set

def compare_songs(filename1, filename2):
    words1 = get_song_word_set(filename1)
    words2 = get_song_word_set(filename2)

    shared_words = words1 & words2
    all_words = words1 | words2

    if len(all_words) == 0:
        similarity_score = 0
    else:
        similarity_score = len(shared_words) / len(all_words)
    
    percentage = similarity_score * 100

    print("Song Comparison")
    print("Song 1:", filename1)
    print("Song2:", filename2)
    print("Shared Unique Words:", len(shared_words))
    print("Similarity Score:", round(percentage, 2), "%")

    print("\nSample Shared Words:")
    shared_word_list = list(shared_words)
    shared_word_list.sort()

    for word in shared_word_list[:15]:
        print("-", word)

    print("\nRecommendation:")

    if percentage >= 10:
        print("Strong pairing for a DJ deck.")
    elif percentage >= 5:
        print("Moderate pairing. Could work better as a transition")
    else:
        print("Weak pairing. These songs may not fit together.")

def main():
    print("DJ Lyric Deck Analyzer")
    print("1. Analyze One Song")
    print("2. Compare Two Songs")

    choice = input("Choose An Option: ")

    if choice == "1":
        filename = input("Enter the lyric file name: ")
        analyze_song(filename)

    elif choice == "2":
        filename1 = input("Enter the first lyric file name: ")
        filename2 = input("Enter the second lyric file name: ")
        compare_songs(filename1, filename2)

    else:
        print("Invalid.")

main()