import json

def load_faqs(path="data/faqs_en.json"):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def find_answer(question, faqs):
    q_lower = question.lower()
    for faq in faqs:
        # シンプルな部分一致で検索
        if any(kw in q_lower for kw in faq["keywords"]):
            return faq["answer"]
    return "Sorry, I couldn't find an answer to your question. Please ask something else or check official tourism sites."

def main():
    faqs = load_faqs()
    print("Welcome to Japan Tourism Info Bot (Alpha)\nType your question (in English) or 'exit' to quit.")
    while True:
        user_input = input("\nQ: ")
        if user_input.lower() in ("exit", "quit"):
            print("Thank you for using Japan Tourism Info Bot!")
            break
        answer = find_answer(user_input, faqs)
        print(f"A: {answer}")

if __name__ == "__main__":
    main()
