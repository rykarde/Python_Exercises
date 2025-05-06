
# Collect user profile data.
first_name = input("What's your first name? ")
last_name = input("What's your last name? ")
email = input("Enter your email (unknown@example.com): ")


# Construct a personalized page header for the logged in user.
header_title = "<h1>" + first_name + " " + last_name + "'s profile</h1>\n"
header_subtitle = "<h2>Hello, " + first_name + "!</h2>\n"
header_content = "<p>" + email + "</p>\n"
page_header = header_title + header_subtitle + header_content

# Construct the main profile page content.
section_title = "<h2>About " + first_name + "</h2>\n"
section_text = "<p>This is a cool bio.</p>\n"
like_button = "<button>Like</button>\n"
section_footer = "<p>Notifications: 4</p>"
page_content = section_title + section_text + like_button + section_footer

# The final HTML body combines all the elements, in order.
print("The HTML string for your profile page is:")
print(page_header + page_content)
