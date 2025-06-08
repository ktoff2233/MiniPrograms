class DFA:
    def __init__(self):
        self.state = 'q0'  # Starting state
        self.accepting_state = 'q3'

    def transition(self, current_state, input_symbol):
        if current_state == 'q0':
            if input_symbol == '0':
                return 'q0'
            elif input_symbol == '1':
                return 'q1'
        elif current_state == 'q1':
            if input_symbol == '0':
                return 'q2'
            elif input_symbol == '1':
                return 'q2'
        elif current_state == 'q2':
            if input_symbol == '0':
                return 'q3'
            elif input_symbol == '1':
                return 'q3'
        elif current_state == 'q3':
            if input_symbol == '0':
                return 'q0'
            elif input_symbol == '1':
                return 'q1'
        return None  # Invalid transition

    def accepts(self, input_string):
        self.state = 'q0'  # Reset to the starting state
        for symbol in input_string:
            self.state = self.transition(self.state, symbol)
            if self.state is None:
                return False  # Invalid transition
        return self.state == self.accepting_state  # Check if in accepting state

# Test the DFA
dfa = DFA()

# List of test strings
test_strings = [
    '1',        # Rejected
    '11',       # Rejected
    '00',       # Rejected
    '0101',     # Accepted
    '1110',     # Accepted
    '00001',    # Rejected
    '00101',    # Accepted
    '1001',     # Accepted
    '1111',     # Accepted
    '000111',   # Accepted
    '1010',     # Accepted
    '010010',   # Accepted
    '11100',    # Accepted
    '000001',   # Rejected
    '0100101'    # Rejected
]
# Run the tests
for test in test_strings:
    result = dfa.accepts(test)
    print(f"Input: {test} - {'Accepted' if result else 'Rejected'}")