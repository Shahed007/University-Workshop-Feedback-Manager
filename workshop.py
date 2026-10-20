# University Workshop Feedback Manager

raw_feedback = " THE SPEAKER WAS GREAT but THE ROOM WAS COLD "

# Question 1: Clean and standardize the feedback.
cleaned = raw_feedback.strip().lower()
cleaned = cleaned.replace("speaker", "presenter")
cleaned = " ".join(cleaned.split())
final_feedback = cleaned.title()
# print(f"Cleaned feedback: {final_feedback}")

# Question 2: Write, read, and append feedback.
# feedback_list = [
#     final_feedback,
#     "The workshop examples were useful and clear.",
#     "The room was noisy but the activities were helpful."
# ]

# with open("feedback.txt", "w", encoding="utf-8") as file:
#     for message in feedback_list:
#         file.write(message + "\n")

# print("\nInitial feedback:")
# with open("feedback.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         print(line.strip())

# with open("feedback.txt", "a", encoding="utf-8") as file:
#     file.write("The presenter answered questions patiently.\n")

# print("\nUpdated feedback:")
# with open("feedback.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         print(line.strip())



# Question 3: Handle common file errors safely.
# print("\nException-handling demonstration:")
# try:
#     with open("feedback.txt", "r", encoding="utf-8") as file:
#         print(file.read(), end="")
# except FileNotFoundError:
#     print("File not found. Please create feedback.txt first.")
# except PermissionError:
#     print("Permission denied. Close the file and try again.")
# finally:
#     print("Operation completed.")



# Question 4: Count feedback entries that contain 'great'.
with open("feedback.txt", "r", encoding="utf-8") as file:
    all_feedback = file.readlines()

total_feedback = len(all_feedback)
great_count = sum(1 for line in all_feedback if "great" in line.lower())

summary = (
    "=== Workshop Feedback Summary ===\n"
    f"Total Feedback: {total_feedback}\n"
    f"Mentions of 'Great': {great_count}\n"
)

with open("summary.txt", "w", encoding="utf-8") as file:
    file.write(summary)

print("\n" + summary)