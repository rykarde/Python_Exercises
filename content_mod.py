words_count = int(input("How many word does the post have?: "))
sentiment = input("What is the sentiment of the post(negative/neutral/positive): ")
account_age_in_days = int(input("What is the account age in days: "))

is_suspicious_length = words_count <= 3 or words_count >= 200
is_useful_post = sentiment != "negative" and account_age_in_days >= 30 and not is_suspicious_length
is_trusted_user = account_age_in_days >= 30


# trusted accounts
if is_useful_post and is_trusted_user:
    print("This post is not spam")

# Spam check
if sentiment == "negative" and account_age_in_days <= 7:
    print("This post as been flagged as potential spam")

