from faker import Faker
fake = Faker()

fake.name()
# 'Lucy Cechtelar'

fake.address()

fake.text()

print(fake.name())
print(fake.address())
print(fake.text())


def create_fake_users(n):
    """Generate fake users."""
    faker = Faker()
    for i in range(n):
        user = User(name=faker.name(),
                    age=random.randint(20, 80),
                    address=faker.address().replace('\n', ', '),
                    phone=faker.phone_number(),
                    email=faker.email())
        db.session.add(user)
    db.session.commit()
    print(f'Added {n} fake users to the database.')


create_fake_users(20)
