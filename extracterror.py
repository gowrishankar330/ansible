def extract_errors(log_file_path):
    with open(log_file_path, 'r') as f:
        for line in f:
            if 'ERROR' in line:
                print(line.strip())

# Example usage
extract_errors('app.log')