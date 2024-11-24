import os
import csv

path = r'website/DataSet/numbers'
array = [num for num in os.listdir(path)]


with open('number.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    csv_writer.writerow(['Number', 'Links'])
    
    for arr in array:
        arr = str(arr)
        video_path = os.path.join(path, arr)  
        if os.path.isdir(video_path):
            links = [video_path]
        
            for link in links:
                csv_writer.writerow([arr, link]) 

path = r'website/DataSet/operators/'
array = [num for num in os.listdir(path)]


with open('operator.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    csv_writer.writerow(['Operator', 'Links'])
    
    for arr in array:
        arr = str(arr)
        video_path = os.path.join(path, arr)  
        if os.path.isdir(video_path):
            links = [video_path]
        
            for link in links:
                csv_writer.writerow([arr, link]) 