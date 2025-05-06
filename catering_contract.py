# take the info to apply to the contract
client = input("Enter client's name: ")
caterer = "King Catering"
date = input("Enter the date of the event (DD/MM/YYYY): ")
ini_time = input("Enter the hour of the beginning of the event (HH:MM): ")
end_time = input("Enter the hour of the end of the event (HH:MM): ")
guests = input("Enter the number of attendees of the event: ")

# Print the entering opening statement
print("Catering contract " + caterer + " \nThis Catering Contract is entered into between " + caterer +
      " (Caterer) and " + client + " (Client)(together, 'Parties') and sets forth the agreement between the Parties "
      "relating th catering services to be provided by th Caterer for Client fot the event"
      " identified in this Contract."
      )
# Print the contract clauses
print("1. Events Details. Client is hiring Caterer to provide food and beverages, and related services, for the "
      "following event:\n Event Date: " + date + "\n Event start time (for guests): " + ini_time + "\n Event end time"
      "(for guests): " + end_time + "\n Estimated guest number: " + guests
      )
