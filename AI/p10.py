#p10
resume=input("paste Resume Text here:").lower()
if "he:"in resume or "she" in resume or "male" in resume or "Female" in resume:
    print("Potential Geneder bias detected i resume")

else:
    print("NO gender bias detected!")
