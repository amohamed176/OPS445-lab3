#!/usr/bin/env python3
'''Lab 3 Inv 2 - Free Disk Space Function'''
# Author ID: amohamed176

import subprocess

def free_space():
    # Run the command to get the available free space on the root directory
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", 
                         stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE, 
                         shell=True)
    output, error = p.communicate()
    
    # Ensure that output is decoded and stripped of newlines
    if error:
        return f"Error: {error.decode('utf-8').strip()}"
    
    return output.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
