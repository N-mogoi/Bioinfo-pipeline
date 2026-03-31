# pipeline.py
# Quality Control Step
def quality_control(data):
    print("Performing quality control checks...")
    if len(data) == 0:
        print("Error: Data is empty!")
    elif len(data) < 10:
        print("Warning: Insufficient data for analysis!")
    else:
        print("Data quality check passed!")
    # Additional checks can go here
    print("Quality control complete.")
