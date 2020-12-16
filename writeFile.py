import os
# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("Users", "carlesonbrandt", "Desktop", "BootCamp", "Module_3", "GitHub_Repo", "Election_Analysis", "analysis","pythonwrite.txt")
file_to_save = os.path.join("analysis","pythonwrite.txt")

# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Counties in the election\n_____________________\nArapahoe\nDenver\nJefferson")

# Close the file
outfile.close()