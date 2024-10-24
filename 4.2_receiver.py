import socket

# Receiver function to verify checksum using XOR and binary complement
def receiver(packet):
    received_values = packet  # Extract the values (without the checksum)
    received_checksum = packet[-1]  # Extract the received checksum

    # Step 1: Compute the sum of all received values, including the checksum
    total_sum = sum(received_values)
    
    # Step 2: Convert the sum to binary and perform XOR on the parts
    bin_sum = format(total_sum, 'b')  # Convert sum to binary string
    if len(bin_sum) > 4:
        first_part = int(bin_sum[-4:], 2)  # First 4 bits
        second_part = int(bin_sum[:-4], 2)  # Bits past the 4th bit
        wrapped_sum = first_part ^ second_part  # Perform XOR
    else:
        wrapped_sum = total_sum  # If sum is <= 4 bits, no need for XOR
    
    # Step 3: Calculate the checksum as the binary complement of the wrapped sum
    computed_checksum = (~wrapped_sum) & 0xF  # Binary complement within 4 bits
    
    print(f"Receiver -> Received Values: {received_values}, Decimal Sum: {total_sum}, Wrapped Sum: {wrapped_sum}, Received Checksum: {received_checksum}, Computed Checksum: {computed_checksum}")
    
    # Compare the received checksum with the computed checksum
    if computed_checksum == 0:
        print("Packet is accepted.")
    else:
        print("Packet is rejected due to errors.")


# Listening for the packet
def listen_for_packet(ip='127.0.0.1', port=12345):
    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Bind to the address and port
        s.bind((ip, port))
        
        # Listen for incoming connections
        s.listen(1)
        print(f"Listening for packets on {ip}:{port}...")
        
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            
            # Receive the packet
            data = conn.recv(1024)
            if data:
                # Convert the received data back to a list of integers
                packet = list(map(int, data.decode('utf-8').split(',')))
                
                # Process the packet to verify checksum
                receiver(packet)

if __name__ == "__main__":
    listen_for_packet()
