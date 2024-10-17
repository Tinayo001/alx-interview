def minOperations(n):
    if n <= 0:
        return 0
    
    # Calculate the maximum number of H characters we can paste after one copy-all operation
    max_pasted = 1 << 30  # Assuming 32-bit integer limit
    
    # Calculate the number of full copies we can do
    full_copies = n // max_pasted
    
    # Calculate remaining H characters after full copies
    remaining = n % max_pasted
    
    # Add one for the final paste operation
    total_operations = full_copies + remaining + 1
    
    return total_operations

