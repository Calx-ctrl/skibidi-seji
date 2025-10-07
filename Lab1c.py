def vowel_count():
    textn = input("Input string: ") 
    vowels = 'AEIOUaeiou'
    vowels_counted = sum(1 for char in textn if char in vowels)
    return vowels_counted

vowels_counted = vowel_count()

def make_shirt(size: str = "Large", message="I love Python"):
    print(f"Shirt size: {size}")
    print(f"Message: {message}")
    print(f"The size of the shirt is {size} and the message is '{message}'")

def merge_strings(*args):
    merged = ' '.join(args)
    return merged

def setup_application(app_name, version, **kwargs):
    config = {
        "app_name": app_name,
        "version": version        
    }
    config.update(kwargs)
    return config


# Program output
print("1. Vowel Count:", vowels_counted)
make_shirt()  # Default arguments
make_shirt(size="Medium", message="Code Everyday!") 
print("\n3. Merged String:", merge_strings("Hello", "from", "Python"))
print("\n4. Application Setup Example:")
app_config = setup_application("MyApp", "1.0", debug=True, port=3000, environment="production")
print(app_config)
# Lab1c.py