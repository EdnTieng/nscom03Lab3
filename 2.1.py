# Function to generate a parity bit
def generate_parity_bit(data, parity_type='even'):
    """
    Generates a parity bit for the binary data.

    :param data: A list of binary values (0s and 1s).
    :param parity_type: 'even' for even parity or 'odd' for odd parity.
    :return: The original data with the parity bit appended.
    """
    # Count the number of 1s in the data
    count_ones = sum(data)
    
    # Generate the parity bit based on the parity type
    if parity_type == 'even':
        # For even parity, the number of 1s (including the parity bit) should be even
        parity_bit = 0 if count_ones % 2 == 0 else 1
    else:
        # For odd parity, the number of 1s (including the parity bit) should be odd
        parity_bit = 1 if count_ones % 2 == 0 else 0
    
    # Append the parity bit to the data
    data_with_parity = data + [parity_bit]
    
    print(f"Original data: {data}, Parity bit: {parity_bit}, Data with parity: {data_with_parity}")
    return data_with_parity

# Function to check the parity of the received message
def check_parity(data_with_parity, parity_type='even'):
    """
    Checks the parity of a binary message with a parity bit.

    :param data_with_parity: A list of binary values (0s and 1s) including the parity bit.
    :param parity_type: 'even' for even parity or 'odd' for odd parity.
    :return: True if parity is correct, False if parity is incorrect.
    """
    # Separate the parity bit from the data
    data = data_with_parity[:-1]  # Data without the parity bit
    parity_bit = data_with_parity[-1]  # The parity bit
    
    # Count the number of 1s in the data
    count_ones = sum(data)
    
    # Check parity
    if parity_type == 'even':
        # For even parity, the number of 1s (including the parity bit) should be even
        is_valid = (count_ones + parity_bit) % 2 == 0
    else:
        # For odd parity, the number of 1s (including the parity bit) should be odd
        is_valid = (count_ones + parity_bit) % 2 == 1
    
    print(f"Received data: {data_with_parity}, Valid parity: {is_valid}")
    return is_valid

# Example usage
if __name__ == "__main__":
    # Binary data to send
    message = [1, 0, 1, 1, 0, 1]  # This is the original message (in binary)
    
    # Generate even parity
    data_with_parity = generate_parity_bit(message, parity_type='even')
    
    # Check the parity at the receiver
    is_valid_parity = check_parity(data_with_parity, parity_type='even')
    
    print(f"Is the received parity valid? {is_valid_parity}")
