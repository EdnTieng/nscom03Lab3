# Function to perform binary division (XOR operation) for CRC
def binary_division(dividend, divisor):
    # Copy the dividend so we can modify it
    remainder = list(dividend)

    # Loop over the dividend and perform XOR where the divisor fits
    for i in range(len(dividend) - len(divisor) + 1):
        # Only proceed if the current bit is 1 (we don't divide by 0)
        if remainder[i] == 1:
            # XOR the divisor with the current part of the dividend
            for j in range(len(divisor)):
                remainder[i + j] ^= divisor[j]

    # The remainder will be the last bits of the modified dividend
    return remainder[-(len(divisor) - 1):]


# Function for simulating CRC including remainder generation
def simulate_crc(frame, generator):
    # Convert the binary strings to lists for easy manipulation
    frame = list(map(int, frame))
    generator = list(map(int, generator))

    # Calculate the number of zeros to append
    zeros_to_append = len(generator) - 1

    # Append zeros to the frame (message)
    message_with_zeros = frame + [0] * zeros_to_append

    # Perform the binary division (XOR) and calculate remainder
    remainder = binary_division(message_with_zeros, generator)

    # Replace the appended zeros with the remainder
    transmitted_frame = frame + remainder

    return frame, generator, message_with_zeros, remainder, transmitted_frame
# Example input from the image: frame = '1101011011', generator = '10011'
frame = '1101011011'
generator = '10011'

# Simulating the process
frame_result, generator_result, message_with_zeros, remainder_result, transmitted_frame = simulate_crc(frame, generator)

# Display the results
print("Frame:", frame_result)
print("Generator:", generator_result)
print("Message after appending zeros:", message_with_zeros)
print("Remainder:", remainder_result)
print("Transmitted Frame (Frame + Remainder):", transmitted_frame)