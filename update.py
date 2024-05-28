try:
    with open('monitored-repo/all-actions.txt') as infile, open('all-aws-events.txt') as outfile:
        for line in infile:
            line = line.strip()
            if ':' in line:
                service, action = line.split(':', 1)
                swapped_line = f"{action}:{service}\n"
                outfile.write(swapped_line)
    print(f"AWS event names were saved")
except FileNotFoundError:
    print(f"The file 'monitored-repo/all-actions.txt' was not found.")
