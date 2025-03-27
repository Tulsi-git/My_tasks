import csv
from datetime import datetime

class InterviewTracker:
    def __init__(self):
        self.interviews = []
    
    def add_interview(self, sid, domain, batch, name, date, time, duration, 
                      round_number, company, client, location, mode):
       

        interview = {
            "SID": sid,
            "Domain": domain,
            "Batch": batch,
            "Name": name,
            "Date": date,
            "Time": time,
            "Duration": duration,
            "Round": round_number,
            "Company": company,
            "Client": client,
            "Location": location,
            "Mode": mode
        }
        self.interviews.append(interview)
    
    def export_to_csv(self, filename=None):
      
        # If no filename is provided, create a dynamic filename
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"interview_tracking.csv"
        
        # Ensure we have interviews to export
        if not self.interviews:
            print("No interviews to export.")
            return
        
        # Open the file and write the data
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            # Use the keys of the first interview as fieldnames
            fieldnames = list(self.interviews[0].keys())
            
            # Create a CSV writer object
            csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write the header
            csv_writer.writeheader()
            
            # Write each interview entry
            for interview in self.interviews:
                csv_writer.writerow(interview)
        
        print(f"Interview tracking data exported to {filename}")
    
    def display_interviews(self):
        """
        Display all interviews in the console
        """
        if not self.interviews:
            print("No interviews recorded.")
            return
        
        for idx, interview in enumerate(self.interviews, 1):
            print(f"\nInterview {idx}:")
            for key, value in interview.items():
                print(f"{key}: {value}")


    # Create an instance of InterviewTracker
tracker = InterviewTracker()
    
tracker.add_interview(
    sid="555",
    domain="Python",
    batch="B18",
    name="Thulasi",
    date="2024-03-26",
    time="10:00 ",
    duration="45 mins",
    round_number="R2",
    company="TechCorp",
    client="ABC Solutions",
    location="Bangalore",
    mode="WFH"
)
    
tracker.add_interview(
    sid="556",
    domain="DE",
    batch="B19",
    name="Sandhya",
    date="2024-03-27",
    time="02:00 ",
    duration="60 mins",
    round_number="R3",
    company="DataInnovate",
    client="XYZ Enterprises",
    location="Chennai",
    mode="WFO"
)

tracker.display_interviews()


tracker.export_to_csv()


    
    