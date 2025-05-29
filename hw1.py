def main():
    # Step 1: Receive Input
    full_name = input("Enter your full name: ")
    email = input("Enter your email address: ")

    # Step 2: Clean and Format the Full Name
    full_name = full_name.strip().title()
    if not full_name.replace(" ", "").isalpha():
        print("Invalid characters in name")
        return
    else:
        name_parts = full_name.split()
        if len(name_parts) < 2:
            print("Please enter both first name and surname.")
            return
        first_name = name_parts[0]
        last_name = name_parts[-1]

    # Step 3: Clean and Validate Email
    email = email.strip().casefold()
    valid_domains = ["@gmail.com", "@school.co.uk"]

    if (not any(email.endswith(domain) for domain in valid_domains) or
        email.count("@") != 1 or
        "." not in email[email.find("@"):]):
        print("Invalid email structure or domain.")
        return

    # Step 4: Auto-Generate a Username
    domain_part = email.split("@")[1].split(".")[0]
    username = f"{first_name[:3].lower()}{last_name[-3:].lower()}{domain_part[:2].lower()}"

    # Step 5: Center Output Nicely
    print("*" + f" Name Cleaned: {full_name} ".center(38, " ") + "*")
    print("*" + f" Email Validated: {email} ".center(38, " ") + "*")
    print("*" + f" Username: {username} ".center(38, " ") + "*")

    # Step 6: Motivational Quote Encoding
    quote = input("Enter a motivational quote: ")
    quote_bytes = quote.encode('utf-8')
    print(f"\nYour quote in bytes: {quote_bytes}")
    print(f"Decoded back: {quote_bytes.decode('utf-8')}")


# Run the program
if __name__ == "__main__":
    main()

