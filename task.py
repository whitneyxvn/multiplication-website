# 📘 BookBuddy v1.0
print("=" * 30)
print("       📚 BOOKBUDDY REPORT")
print("=" * 30)

# Step 1: Get user input
full_name = input("Enter your full name: ").strip()
book_title = input("Book title: ").strip()
author = input("Author: ").strip()
pages = input("Number of pages: ").strip()
quote = input("Your favorite quote from the book: ").strip()
summary = input("Write a one-line summary of the book: ").strip()
rating = input("Rate the book (1-5 stars): ").strip()

print("\nLoading summary...\n")

# Step 2: Process input
formatted_name = full_name.upper()
name_parts = full_name.split()
initials = ""
for part in name_parts:
    if part:  # Check to avoid empty strings
        initials += part[0].upper() + "."

formatted_title = book_title.title()
short_title = formatted_title[:20] + "..." if len(formatted_title) > 20 else formatted_title
formatted_author = author.title()

# Clean the summary
clean_summary = summary.replace("bad", " ").replace("boring", " ").strip()

# Format the quote using escape characters
formatted_quote = f"\t\"{quote}\""

# Format rating
if rating.isnumeric():
    rating_stars = int(rating)
    if 1 <= rating_stars <= 5:
        stars_display = "★" * rating_stars + "☆" * (5 - rating_stars)
    else:
        stars_display = "Invalid rating"
else:
    stars_display = "Invalid rating"

# Step 3: Print Report
print("=" * 30)
print(f"Student: {formatted_name} ({initials})")
print(f"Book: \"{short_title}\" by {formatted_author}")
print(f"Pages: {pages}")
print("\nFavorite Quote:")
print(formatted_quote)
print("\nQuick Summary:")
print(f"\t{clean_summary}")
print(f"\nRating: {stars_display}")
print("-" * 30)
print("“Well done! You’ve logged your book like a pro!”")
