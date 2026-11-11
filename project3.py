# ============================================
# DecodeLabs - Artificial Intelligence
# Project 3: AI Recommendation Logic
# ============================================

# Sample items with their categories
items = {
    "Python Course": ["python", "programming", "ai"],
    "Machine Learning Course": ["machine learning", "python", "ai"],
    "Deep Learning Course": ["deep learning", "python", "ai"],
    "Data Science Course": ["data science", "python", "data"],
    "Web Development Course": ["html", "css", "javascript", "web"],
    "Graphic Design Course": ["design", "graphics", "creative"],
}


# Display available interests
print("=" * 50)
print("      AI RECOMMENDATION SYSTEM")
print("=" * 50)

print("\nAvailable interests:")
print("python")
print("programming")
print("ai")
print("machine learning")
print("deep learning")
print("data science")
print("data")
print("html")
print("css")
print("javascript")
print("web")
print("design")
print("graphics")
print("creative")


# Take user input
user_input = input(
    "\nEnter your interests separated by commas: "
)

# Clean user input
user_preferences = [
    preference.strip().lower()
    for preference in user_input.split(",")
]


# Calculate similarity and recommendations
recommendations = []

for item_name, item_features in items.items():

    # Count matching preferences
    match_count = 0

    for preference in user_preferences:
        if preference in item_features:
            match_count += 1

    # Calculate similarity score
    if match_count > 0:
        score = match_count / len(user_preferences)
        recommendations.append(
            (item_name, score, match_count)
        )


# Sort recommendations by similarity score
recommendations.sort(
    key=lambda x: x[1],
    reverse=True
)


# Display recommendations
print("\n" + "=" * 50)
print("RECOMMENDED ITEMS")
print("=" * 50)

if recommendations:

    for item_name, score, match_count in recommendations:

        print(
            f"{item_name} "
            f"- Similarity Score: {score:.2f} "
            f"- Matches: {match_count}"
        )

else:

    print(
        "Sorry! No matching recommendations found."
    )


print("\nThank you for using the AI Recommendation System!")