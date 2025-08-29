fever = input("Do you have fever? (yes/no): ")
cough = input("Do you have cough? (yes/no): ")

if fever== "yes" and cough== "yes":
    print("Diagnosis: you may have fever")
elif fever== "yes":
    print("Diagnosis: you may have viral")
elif cough== "yes":
    print("Diagnosis: you may have common cold")
else:
    print("Diagnosis: you are healthy")
