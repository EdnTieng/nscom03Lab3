# Function to generate a 2D parity block
def generate_2d_parity(data, parity_type='even'):
    """
    Generates 2D parity for a block of binary data.

    :param data: A 2D list (matrix) of binary values (0s and 1s).
    :param parity_type: 'even' for even parity or 'odd' for odd parity.
    :return: The data with added row and column parity bits.
    """
    num_rows = len(data)
    num_cols = len(data[0])
    
    # Step 1: Calculate row parity
    for row in data:
        count_ones = sum(row)
        if parity_type == 'even':
            parity_bit = 0 if count_ones % 2 == 0 else 1
        else:
            parity_bit = 1 if count_ones % 2 == 0 else 0
        row.append(parity_bit)  # Add row parity bit
    
    # Step 2: Calculate column parity
    col_parity = []
    for col in range(num_cols):
        count_ones = sum(data[row][col] for row in range(num_rows))
        if parity_type == 'even':
            parity_bit = 0 if count_ones % 2 == 0 else 1
        else:
            parity_bit = 1 if count_ones % 2 == 0 else 0
        col_parity.append(parity_bit)
    
    # Calculate the parity for the parity row itself
    count_ones = sum(row[-1] for row in data)  # Parity bits from each row
    if parity_type == 'even':
        last_parity_bit = 0 if count_ones % 2 == 0 else 1
    else:
        last_parity_bit = 1 if count_ones % 2 == 0 else 0
    col_parity.append(last_parity_bit)  # Final column parity
    
    # Step 3: Add the column parity as the last row
    data.append(col_parity)
    
    print(f"Generated 2D parity matrix: {data}")
    return data

# Function to check the 2D parity block
def check_2d_parity(data_with_parity, parity_type='even'):
    """
    Checks the 2D parity of a block of binary data with parity bits.

    :param data_with_parity: A 2D list (matrix) of binary values (0s and 1s) including parity bits.
    :param parity_type: 'even' for even parity or 'odd' for odd parity.
    :return: True if parity is correct, False if parity is incorrect.
    """
    num_rows = len(data_with_parity) - 1  # Exclude the last row (parity row)
    num_cols = len(data_with_parity[0]) - 1  # Exclude the last column (parity column)
    
    # Step 1: Check row parity
    for row in range(num_rows):
        count_ones = sum(data_with_parity[row][:num_cols])  # Sum all but the parity bit
        parity_bit = data_with_parity[row][num_cols]  # Row parity bit
        if parity_type == 'even':
            if (count_ones + parity_bit) % 2 != 0:
                print(f"Row {row} parity check failed.")
                return False
        else:
            if (count_ones + parity_bit) % 2 != 1:
                print(f"Row {row} parity check failed.")
                return False
    
    # Step 2: Check column parity
    for col in range(num_cols):
        count_ones = sum(data_with_parity[row][col] for row in range(num_rows))
        parity_bit = data_with_parity[num_rows][col]  # Column parity bit
        if parity_type == 'even':
            if (count_ones + parity_bit) % 2 != 0:
                print(f"Column {col} parity check failed.")
                return False
        else:
            if (count_ones + parity_bit) % 2 != 1:
                print(f"Column {col} parity check failed.")
                return False
    
    # Step 3: Check the final parity bit
    count_ones = sum(data_with_parity[row][num_cols] for row in range(num_rows))  # Parity bits in the column
    final_parity_bit = data_with_parity[num_rows][num_cols]  # Bottom-right parity bit
    if parity_type == 'even':
        if (count_ones + final_parity_bit) % 2 != 0:
            print("Final parity check failed.")
            return False
    else:
        if (count_ones + final_parity_bit) % 2 != 1:
            print("Final parity check failed.")
            return False
    
    print("2D Parity check passed.")
    return True

# Example usage
if __name__ == "__main__":
    # Binary data block (matrix)
    data = [
        [1, 0, 1, 1],
        [0, 1, 1, 0],
        [1, 0, 0, 1]
    ]
    
    # Generate 2D parity
    data_with_parity = generate_2d_parity(data, parity_type='even')
    
    # Check the 2D parity at the receiver
    is_valid_parity = check_2d_parity(data_with_parity, parity_type='even')
    
    print(f"Is the received 2D parity valid? {is_valid_parity}")
