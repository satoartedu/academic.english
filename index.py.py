import random

# アカデミックなフレーズ集
phrases = {
    "意見を述べる": [
        "I believe that...",
        "In my opinion...",
        "From my perspective..."
    ],
    "反論する": [
        "I see your point, but...",
        "I respectfully disagree because...",
        "However, I would like to challenge that by saying..."
    ],
    "質問を受ける": [
        "That's an interesting question.",
        "Thank you for your question.",
        "I would be happy to answer that."
    ],
    "説明を求める": [
        "Could you clarify what you mean by...?",
        "Could you elaborate on that?",
        "Can you explain further?"
    ]
}

# 英単語の学習データ
vocabulary = {
    "Analyze": "to examine something in detail in order to understand it better or discover more about it",
    "Synthesize": "to combine different ideas or information to make a new understanding",
    "Methodology": "a system of methods used in a particular area of study or activity",
    "Comprehend": "to understand or grasp something fully",
    "Interpret": "to explain the meaning of something in a particular way",
    "Hypothesis": "a proposed explanation for something based on limited evidence, used as a starting point for further investigation",
    "Data": "facts, figures, or information used to support a conclusion or decision",
    "Theory": "a system of ideas intended to explain something"
}

# クイズ形式でフレーズを復習する関数
def quiz_phrases():
    print("クイズ開始！以下のフレーズの使い方を学びます。")
    for category, phrases_list in phrases.items():
        print(f"\nカテゴリー: {category}")
        random.shuffle(phrases_list)  # フレーズをシャッフル
        correct_answer = phrases_list[0]  # 正しいフレーズ
        print("質問: 以下のフレーズの意味を尋ねます。")
        print(f"1. {phrases_list[0]}")

        answer = input("このフレーズの意味は何ですか？: ").strip()

        if answer.lower() == correct_answer.lower():
            print("正解です！\n")
        else:
            print(f"残念、正解は '{correct_answer}' です。\n")

# 英単語学習モード
def learn_vocabulary():
    print("英単語学習モード: 以下の単語と意味を学びます。")
    for word, meaning in vocabulary.items():
        print(f"{word}: {meaning}")
    input("\n次に進むにはEnterキーを押してください...\n")

# フレーズ学習モード
def learn_phrases():
    print("フレーズ学習モード: 各カテゴリーのフレーズを学びます。")
    for category, phrases_list in phrases.items():
        print(f"\nカテゴリー: {category}")
        for phrase in phrases_list:
            print(f"- {phrase}")
        input("\n次に進むにはEnterキーを押してください...\n")

# メインメニュー
def main():
    while True:
        print("アカデミック英語学習アプリ")
        print("1. フレーズを学ぶ")
        print("2. 英単語を学ぶ")
        print("3. フレーズのクイズで復習する")
        print("4. 英単語のクイズで復習する")
        print("5. 終了")
        choice = input("選択してください: ").strip()

        if choice == "1":
            learn_phrases()
        elif choice == "2":
            learn_vocabulary()
        elif choice == "3":
            quiz_phrases()
        elif choice == "4":
            quiz_vocabulary()
        elif choice == "5":
            print("アプリを終了します。")
            break
        else:
            print("無効な選択です。もう一度試してください。")

# 英単語のクイズ
def quiz_vocabulary():
    print("英単語クイズ開始！以下の単語の意味を答えましょう。")
    words = list(vocabulary.keys())
    random.shuffle(words)  # 単語をシャッフル
    for word in words:
        correct_answer = vocabulary[word]
        print(f"\n質問: '{word}' の意味は何ですか？")
        answer = input("答えを入力してください: ").strip()

        if answer.lower() == correct_answer.lower():
            print("正解です！\n")
        else:
            print(f"残念、正解は '{correct_answer}' です。\n")

if __name__ == "__main__":
    main()
