def score_idea(idea):
    # This is a fake scoring logic, we’ll replace it with AI soon
    keywords = ["AI", "health", "education", "automation", "climate"]
    score = 5
    for word in keywords:
        if word.lower() in idea.lower():
            score += 1
    return min(score, 10)

if __name__ == "__main__":
    print("🚀 Startup Idea Validator")
    idea = input("Enter your startup idea: ")
    score = score_idea(idea)
    print(f"\nYour idea scored: {score}/10")
