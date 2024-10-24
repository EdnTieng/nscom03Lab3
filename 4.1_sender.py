import socket

# Function to compute the checksum using XOR and binary complement
def sender(values):
    # Step 1: Compute the sum of all values
    total_sum = sum(values)
    
    # Step 2: Convert the sum to binary and extract the parts for XOR
    bin_sum = format(total_sum, 'b')  # Convert sum to binary string
    
    # Step 3: XOR the first 4 bits with the bits past the 4th bit
    if len(bin_sum) > 4:
        first_part = int(bin_sum[-4:], 2)  # First 4 bits
        second_part = int(bin_sum[:-4], 2)  # Bits past the 4th bit
        wrapped_sum = first_part ^ second_part  # Perform XOR
    else:
        wrapped_sum = total_sum  # If sum is <= 4 bits, no need for XOR
    
    # Step 4: Calculate the checksum as the binary complement of the wrapped sum
    checksum = (~wrapped_sum) & 0xF  # Binary complement within 4 bits
    
    # Append checksum to the packet
    packet = values + [checksum]
    
    print(f"Sender -> Values: {values}, Decimal Sum: {total_sum}, Wrapped Sum: {wrapped_sum}, Checksum: {checksum}")
    return packet

# Sending packet over the network
def send_packet(packet, ip='127.0.0.1', port=12345):
    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the receiver
        s.connect((ip, port))
        
        # Convert the packet to a string and send it
        message = ','.join(map(str, packet))  # Converting list to a comma-separated string
        s.sendall(message.encode('utf-8'))    # Send the packet
        print(f"Packet sent to {ip}:{port}")

if __name__ == "__main__":
    values_to_send = [7, 11, 12, 0, 6]  # The message to send
    packet = sender(values_to_send)  # Generate packet with checksum
    send_packet(packet)  # Send the packet to the receiver
