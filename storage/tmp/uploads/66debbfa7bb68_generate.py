# Install this PIP module: pip install faker

from faker import Faker
import random

fake = Faker()

# Generate 100 random user records
user_records = []
serial_number = 9
for _ in range(6):
    # Generate a username that starts with '018', '017', or '015'
    username_prefix = random.choice(['01518473834'])
    username = f"{username_prefix}{serial_number:01d}"  # Serial number padded to 8 digits

    # Generate a fake email address
    #email = fake.email()

    # Generate user record
    user_record = (
        'NULL',  # Assuming 'id' is an auto-incremented field
        '5',  # Assuming 'group_id' is optional
        f"'{username}'",  # Generate a username
        "'$2y$10$4UX0v1u0jfItuu1jvAIh/uMr35mfa0FDLubHOo5helXMOPF4coY2.'",  # Set all passwords to a fixed hash
        f"'NULL'",  # Generate a fake email address
        f"'MD Monuhor'",  ########## Generate a random first name
        f"'Ali {serial_number:01d}'",  ########## Generate a random last name
        'NULL',  # Assuming 'nid' is optional
        'NULL',  # Assuming 'nid_front_image' is optional
        'NULL',  # Assuming 'nid_back_image' is optional
        "'01518473834'",  ######### Assuming 'referer' is optional
        f"'{fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d')}'",  # Generate a random date of birth formatted as YYYY-MM-DD
        'NULL',  # Assuming 'address_1' is optional
        'NULL',  # Assuming 'state' is optional
        'NULL',  # Assuming 'city' is optional
        '0',  # Generate a random value for 'is_ref' (0 or 1)
        'NULL',  # Assuming 'gender' is optional
        'NULL',  # Assuming 'country' is optional
        'NULL',  # Assuming 'avatar' is optional
        '1',  # Set 'active' to 1
        'NULL',  # Assuming 'login_attempt' is set to 0 by default
        'NULL',  # Assuming 'last_login' is optional
        'CURRENT_TIMESTAMP',  # Set 'created_at' to the current timestamp
        'NULL',  # Assuming 'updated_at' is optional
        'NULL',  # Assuming 'reminder' is optional
        'NULL',  # Assuming 'activation' is optional
        'NULL',  # Assuming 'temp_pass' is optional
        'NULL',  # Assuming 'remember_token' is optional
        '0',  # Assuming 'device_token' is optional
        'NULL',  # Assuming 'last_activity' is optional
        'NULL'  # Assuming 'config' is optional
    )
    user_records.append(f"({', '.join(map(str, user_record))})")
    serial_number += 1

# Create the SQL query
query = f"INSERT INTO `tb_users` (`id`, `group_id`, `username`, `password`, `email`, `first_name`, `last_name`, `nid`, `nid_front_image`, `nid_back_image`, `referer`, `birth_of_day`, `address_1`, `state`, `city`, `is_ref`, `gender`, `country`, `avatar`, `active`, `login_attempt`, `last_login`, `created_at`, `updated_at`, `reminder`, `activation`, `temp_pass`, `remember_token`, `device_token`, `last_activity`, `config`) VALUES {', '.join(user_records)};"

print(query)
