class LuhnValidator:
    def __init__(self):
        self.stack = []

    def push_digit(self, digit):
        """Push a digit onto the stack."""
        self.stack.append(digit)

    def pop_digit(self):
        """Pop a digit from the stack."""
        if self.stack:
            return self.stack.pop()
        return None

    def validate(self, card_number):
        """Validate the card number using the Luhn algorithm."""
        card_number = ''.join(filter(str.isdigit, card_number))
        if len(card_number) < 2:
            return False
        digits = [int(digit) for digit in reversed(card_number)]
        for i in range(1, len(digits), 2):
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9
        return sum(digits) % 10 == 0

if __name__ == "__main__":
    validator = LuhnValidator()
    
    test_card_numbers = [
        "4539 1488 0343 6467",  
        "6011 1111 1111 1117",  
        "3782 8224 6310 005",    
        "1234 5678 9012 3456", 
        "4532 1488 0343 6467",  
        "1234 5678 9012 345"    
    ]

    for card_number in test_card_numbers:
        is_valid = validator.validate(card_number)
        print(f"Card Number: {card_number} - Valid: {is_valid}")